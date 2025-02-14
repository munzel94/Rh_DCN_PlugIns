import logging
from eventmanager import Evt
from Results import RaceClassRankMethod
from RHUI import UIField, UIFieldType
from RHRace import StartBehavior

logger = logging.getLogger(__name__)

# Berechnung der Gesamtanzahl an Runden und der Gesamtzeit
def calculate_totals(runs):
    total_lap_count = sum(run["lapCount"] for run in runs)
    total_result_time = sum(run["resultTime"] for run in runs)
    return total_lap_count, total_result_time

# Erzeugt einen String mit Laufdetails
def generate_run_string(runs, rhapi):
    run_parts = [
        f"[{run['heatID']}] {run['lapCount']}/{rhapi.utils.format_time_to_str(run['resultTime'])}"
        for run in runs
    ]
    return " ".join(run_parts)

# Ermittelt die Top-X-Läufe
def get_top_x_runs(runs, x):
    sorted_runs = sorted(runs, key=lambda r: (-r["lapCount"], r["resultTime"]))
    return sorted_runs[:x]

# Hauptberechnungsfunktion
def dcn_Quali(rhapi, race_class, args):
    if 'runs' not in args or not args['runs'] or int(args['runs']) < 1:
        return False, {}

    runs_limit = int(args['runs'])
    run_time_limit = int(args['maxRunTime']) * 1000

    heats = rhapi.db.heats_by_class(race_class.id)
    race_format = rhapi.db.raceformat_by_id(race_class.format_id)

    pilot_results = {}

    # Heats und Rennen durchlaufen
    for heat in heats:
        races = rhapi.db.races_by_heat(heat.id)
        for race in races:
            runs = rhapi.db.pilotruns_by_race(race.id)
            for run in runs:
                if run.pilot_id not in pilot_results:
                    pilot_results[run.pilot_id] = []

                start_lap = 2 if race_format and race_format.start_behavior == StartBehavior.STAGGERED else 1
                laps = rhapi.db.laps_by_pilotrun(run.id)

                run_laps = 0
                run_time = 0

                # Runden auswerten
                laps = [x for x in laps if not x.deleted]
                for lap in laps[start_lap:]:
                    logger.info(f"Checking lap: {lap.id}, lap_time: {lap.lap_time}, run_time: {run_time}")
                    if run_time + lap.lap_time < run_time_limit:
                        run_time += lap.lap_time
                        run_laps += 1
                        logger.info(f"Lap counted. Total laps: {run_laps}, total time: {run_time}")
                    else:
                        logger.info(f"Lap skipped. Total time would exceed limit: {run_time + lap.lap_time}")


                lap_result = {"heatID": heat.display_name.split('/')[0].strip(), "lapCount": run_laps, "resultTime": run_time}
                pilot_results[run.pilot_id].append(lap_result)

    # Top-Ergebnisse ermitteln
    pilot_top_results = {}
    for pilot_id, results in pilot_results.items():
        pilot_top_results[pilot_id] = get_top_x_runs(results, runs_limit)

    leaderboard = []
    for pilot_id, results in pilot_top_results.items():
        pilot = rhapi.db.pilot_by_id(pilot_id)
        if pilot:
            total_lap_count, total_result_time = calculate_totals(results)
            leaderboard.append({
                'pilot_id': pilot.id,
                'callsign': pilot.callsign,
                'team_name': pilot.team,
                'sumTopLaptimes_raw': total_result_time,
                'sumTopLaptimes': rhapi.utils.format_time_to_str(total_result_time),
                'sumLapsCount': total_lap_count,
                'singleResultsStr': generate_run_string(results,rhapi),
            })

    # Sortiere Leaderboard
    leaderboard = sorted(leaderboard, key=lambda x: (-x['sumLapsCount'], x['sumTopLaptimes_raw']))

    # Metadaten für die Anzeige
    meta = {
        'method_label': f"Best {runs_limit} Heats",
        'rank_fields': [
            {'name': 'sumLapsCount', 'label': "Gesamt Runden"},
            {'name': 'sumTopLaptimes', 'label': "Gesamtzeit"},
            {'name': 'singleResultsStr', 'label': "Gewertete Heats"}
        ]
    }
    return leaderboard, meta

# Registrierung der Ranking-Methoden
def register_handlers(args):
    args['register_fn'](
        RaceClassRankMethod(
            "Best X Heats",
            dcn_Quali,
            {
                'runs': 3,
                'maxRunTime': 120
            },
            [
                UIField('runs', "Anzahl der besten Läufe", UIFieldType.BASIC_INT, placeholder="3"),
                UIField('maxRunTime', "Maximale Zeit pro Lauf (Sekunden)", UIFieldType.BASIC_INT, placeholder="120")
            ]
        )
    )

# Plugin-Initialisierung
def initialize(rhapi):
    logger.info("Initializing DCN-Quali Plugin")
    rhapi.events.on(Evt.CLASS_RANK_INITIALIZE, register_handlers)
