import argparse
import sys
import os

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("check_arguments_logger")

def checkAvg(args):
    if args.get_avg <= 0:
        logger.error("The average time (-get_avg) cannot be negative or equal to 0.")
        sys.exit(1)
    elif args == None:
        logger.error("No argument given.")
        sys.exit(1)
    elif args.get_avg > 0:
        logger.info("The average time (-get_avg) is %s",args.get_avg)
        return True
    return False