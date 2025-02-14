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
            rhapi.__("1/8-Winner-Finale") + " 6 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 3),
                HeatPlanSlot(SeedMethod.INPUT, 14),
                HeatPlanSlot(SeedMethod.INPUT, 19),
                HeatPlanSlot(SeedMethod.INPUT, 30)
            ]
        ),
        HeatPlan(
            rhapi.__("1/8-Winner-Finale") + " 7 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 5),
                HeatPlanSlot(SeedMethod.INPUT, 12),
                HeatPlanSlot(SeedMethod.INPUT, 21),
                HeatPlanSlot(SeedMethod.INPUT, 28),
                HeatPlanSlot(SeedMethod.INPUT, 35)
            ]
        ),        HeatPlan(
            rhapi.__("1/8-Winner-Finale") + " 8 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 7),
                HeatPlanSlot(SeedMethod.INPUT, 10),
                HeatPlanSlot(SeedMethod.INPUT, 13),
                HeatPlanSlot(SeedMethod.INPUT, 26)
            ]
        ),


    if total_pilots>18: