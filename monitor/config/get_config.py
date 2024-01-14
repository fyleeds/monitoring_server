import sys
import os
import json

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("config_get_logger")

from create_config import createConfig,config_path

def getConfig(config_path):
    if not os.path.exists(config_path):
        createConfig(config_path)
    else :
        with open(config_path) as report:
            return json.loads(report.read())
