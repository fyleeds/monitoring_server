import sys
import os

base_path = "../etc/monit/"

# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../storage'))
from create_folder import getListDir

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("config_logger")

from create_config import base_path

def getConfig(path):
    if getListDir(path) == []:
        logger.info("No config file found : Creating default config file...")
        
        logger.info("Config file loaded")

    return logger