import sys
import os
import json

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("config_create_logger")

configs_path = "/etc/monit/"
config_name = "monit_conf.json"
config_path = configs_path + config_name

def createConfig(path):
    config_data = {'ports': {'tcp': 80 , 'ssh': 22}}
    with open(path, 'w') as outfile:
        json.dump(config_data,outfile)
    logger.info("Config file created at %s",path)