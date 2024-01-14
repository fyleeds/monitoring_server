import sys
import os
import json

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("config_logger")

from create_config import createConfig,config_path

def getConfig(config_path):
    if os.path.exists(config_path):
        createConfig(config_path)
        logger.info("No config file found : Default config has been created.")
    else :
        logger.info("Config file loaded")
        with open(config_path) as report:
            return json.loads(report.read())
