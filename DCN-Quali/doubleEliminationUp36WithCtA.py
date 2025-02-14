import logging
import RHUtils
import random
from eventmanager import Evt
from HeatGenerator import HeatGenerator, HeatPlan, HeatPlanSlot, SeedMethod
from RHUI import UIField, UIFieldType, UIFieldSelectOption
logger = logging.getLogger(__name__)

def getTotalPilots(rhapi, generate_args):
    input_class_id = generate_args.get('input_class')

    if input_class_id:
        if generate_args.get('total_pilots'):
            total_pilots = int(generate_args['total_pilots'])
        else:
            race_class = rhapi.db.raceclass_by_id(input_class_id)
            class_results = rhapi.db.raceclass_results(race_class)
            if class_results and type(class_results) == dict:
                # fill from available results
                total_pilots = len(class_results['by_race_time'])
            else:
                # fall back to all pilots
                total_pilots = len(rhapi.db.pilots)
    else:
        # use total number of pilots
        total_pilots = len(rhapi.db.pilots)

    return total_pilots

def generateLadder(rhapi, generate_args=None):
    total_pilots = getTotalPilots(rhapi, generate_args)

    if total_pilots == 0:
        logger.warning("Unable to seed ladder: no pilots available")
        return False
    if total_pilots>24:
            return [
        HeatPlan(
            rhapi.__("Winner") + " 1(E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 8),
                HeatPlanSlot(SeedMethod.INPUT, 9),
                HeatPlanSlot(SeedMethod.INPUT, 24),
                HeatPlanSlot(SeedMethod.INPUT, 25),
                HeatPlanSlot(SeedMethod.INPUT, 36)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 2 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 6),
                HeatPlanSlot(SeedMethod.INPUT, 11),
                HeatPlanSlot(SeedMethod.INPUT, 22),
                HeatPlanSlot(SeedMethod.INPUT, 27)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 3 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 4),
                HeatPlanSlot(SeedMethod.INPUT, 13),
                HeatPlanSlot(SeedMethod.INPUT, 20),
                HeatPlanSlot(SeedMethod.INPUT, 29),
                HeatPlanSlot(SeedMethod.INPUT, 34)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 4 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 2),
                HeatPlanSlot(SeedMethod.INPUT, 15),
                HeatPlanSlot(SeedMethod.INPUT, 18),
                HeatPlanSlot(SeedMethod.INPUT, 31)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 5 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 1),
                HeatPlanSlot(SeedMethod.INPUT, 16),
                HeatPlanSlot(SeedMethod.INPUT, 17),
                HeatPlanSlot(SeedMethod.INPUT, 32),
                HeatPlanSlot(SeedMethod.INPUT, 33)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 6 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 3),
                HeatPlanSlot(SeedMethod.INPUT, 14),
                HeatPlanSlot(SeedMethod.INPUT, 19),
                HeatPlanSlot(SeedMethod.INPUT, 30)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 7 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 5),
                HeatPlanSlot(SeedMethod.INPUT, 12),
                HeatPlanSlot(SeedMethod.INPUT, 21),
                HeatPlanSlot(SeedMethod.INPUT, 28),
                HeatPlanSlot(SeedMethod.INPUT, 35)
            ]
        ),        HeatPlan(
            rhapi.__("Winner") + " 8 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 7),
                HeatPlanSlot(SeedMethod.INPUT, 10),
                HeatPlanSlot(SeedMethod.INPUT, 13),
                HeatPlanSlot(SeedMethod.INPUT, 26)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 9 (E1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 1)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 10 (E1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 3)
            ]
        ),
                HeatPlan(
            rhapi.__("Looser") + " 11 (E1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 5),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 5)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 12 (E1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 7),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 7)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 13 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 1)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 14 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 3)
            ]
        ),
         HeatPlan(
            rhapi.__("Winner") + " 15 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 5),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 5)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 16 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 7),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 7)
            ]
        ),
          HeatPlan(
            rhapi.__("Looser") + " 17 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 8),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 8)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 18 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 13),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 13),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 9),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 9)
            ]
        ),
                HeatPlan(
            rhapi.__("Looser") + " 19 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 10),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 10)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 20 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 15),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 15),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 11),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 11)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 21 (E3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 13),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 13)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 22 (E3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 16),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 16),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 17),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 17)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 23 (E3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 15),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 15)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 24 (E3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 18),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 18),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 19),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 19)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 25 (E4)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 20),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 20),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 21),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 21)
            ]
        ),        
        HeatPlan(
            rhapi.__("Looser") + " 26 (E4)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 22),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 22),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 23),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 23)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 27 (E5)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 24),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 24),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 25),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 25)
            ]
        ),
        HeatPlan(
            rhapi.__("Winner") + " 28 (E6)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 20),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 20),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 22),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 22)
            ]
        ),
        HeatPlan(
            rhapi.__("Looser") + " 29 (E6)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 26),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 26)
            ]
        ),
                HeatPlan(
            rhapi.__("Finale") + " 30 (E7)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 28),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 28)
            ]
        )]