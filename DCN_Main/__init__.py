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
            if class_results and isinstance(class_results, dict):
                total_pilots = len(class_results.get('by_race_time', []))
            else:
                total_pilots = len(rhapi.db.pilots)
    else:
        total_pilots = len(rhapi.db.pilots)
    
    return total_pilots

def generateDCNMain(rhapi, generate_args):
      return [
        HeatPlan(
            rhapi.__("Race") + " 1 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 1),
                HeatPlanSlot(SeedMethod.INPUT, 16),
                HeatPlanSlot(SeedMethod.INPUT, 24),
                HeatPlanSlot(SeedMethod.INPUT, 32),
                HeatPlanSlot(SeedMethod.INPUT, 33)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 2 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 8),
                HeatPlanSlot(SeedMethod.INPUT, 9),
                HeatPlanSlot(SeedMethod.INPUT, 17),
                HeatPlanSlot(SeedMethod.INPUT, 25)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 3 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 6),
                HeatPlanSlot(SeedMethod.INPUT, 11),
                HeatPlanSlot(SeedMethod.INPUT, 19),
                HeatPlanSlot(SeedMethod.INPUT, 27)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 4 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 4),
                HeatPlanSlot(SeedMethod.INPUT, 13),
                HeatPlanSlot(SeedMethod.INPUT, 21),
                HeatPlanSlot(SeedMethod.INPUT, 29),
                HeatPlanSlot(SeedMethod.INPUT, 36)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 5 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 3),
                HeatPlanSlot(SeedMethod.INPUT, 14),
                HeatPlanSlot(SeedMethod.INPUT, 22),
                HeatPlanSlot(SeedMethod.INPUT, 30),
                HeatPlanSlot(SeedMethod.INPUT, 35)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 6 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 5),
                HeatPlanSlot(SeedMethod.INPUT, 12),
                HeatPlanSlot(SeedMethod.INPUT, 20),
                HeatPlanSlot(SeedMethod.INPUT, 28)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 7 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 7),
                HeatPlanSlot(SeedMethod.INPUT, 10),
                HeatPlanSlot(SeedMethod.INPUT, 18),
                HeatPlanSlot(SeedMethod.INPUT, 26)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 8 (E1)",
            [
                HeatPlanSlot(SeedMethod.INPUT, 2),
                HeatPlanSlot(SeedMethod.INPUT, 15),
                HeatPlanSlot(SeedMethod.INPUT, 23),
                HeatPlanSlot(SeedMethod.INPUT, 31),
                HeatPlanSlot(SeedMethod.INPUT, 34)
            ]
        ),
                HeatPlan(
            rhapi.__("Race") + " 9 (DE1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 3), 
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 4)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 10 (DE1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 5),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 7), 
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 0)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 11 (DE1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 2), 
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 7)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 12 (DE1)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 5),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 7),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 6), 
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 5, 3)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 13 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 1)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 14 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 3)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 15 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 5),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 5)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 16 (E2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 6),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 7),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 7)
            ]
        ),

        HeatPlan(
            rhapi.__("Race") + " 17 (DE2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 8),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 9),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 15)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 18 (DE2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 10),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 11),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 13)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 19 (DE2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 15),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 9),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 8),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 14)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 20 (DE2)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 13),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 11),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 10),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 12)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 21 (DE3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 18),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 16),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 17),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 19)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 22 (DE3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 16),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 18),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 19),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 17)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 23 (E3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 12),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 13),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 13)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 24 (E3)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 14),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 15),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 15)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 25 (DE4)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 22),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 20),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 21),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 23)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 26 (DE4)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 23),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 21),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 20),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 22)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 27 (DE5)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 24),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 24),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 25),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 25)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 28 (E4)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 22),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 22),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 23),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 23)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 29 (DE6)",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 26),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 26),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 27)
            ]
        ),
        HeatPlan(
            rhapi.__("Final"),
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 28),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 27),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 28)
            ]
        )
    ]

def heat_listener(args):
    heat_id = args.get("heat_id")
    if heat_id is None:
        logger.error("Fehlendes 'heat_id' im Event-Argument: %s", args)
        return
    
    heat = db.heat_by_id(heat_id)
    if heat is None:
        logger.error("Kein Heat gefunden mit ID: %s", heat_id)
        return
    
    logger.info("Heat gefunden: %s", heat)

def register_handlers(args):
    for generator in [
        HeatGenerator(
            "DCN Mains",
            generateDCNMain,
            None,
            None,
        )
    ]:
        args['register_fn'](generator)

def initialize(rhapi):
    rhapi.events.on(Evt.HEAT_GENERATOR_INITIALIZE, register_handlers)