import sys 
import os
import json
# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../measures'))

from CPU import createCpuObject
from DISK import createDiskObject
from RAM import createRamObject
from TCP import createTcpObject

sys.path.append(os.path.abspath('../var/log'))
# Créer une instance de logger pour ce fichier
logger = setup_logger()

def createJsonObject():
    return {
        "cpu": createCpuObject(),
        "disk": createDiskObject(),
        "ram": createRamObject(),
        "tcp": createTcpObject()
    }

def createJsonFile():
    with open('../var/log/report.json', 'w') as outfile:
        logger.info("Creating json file %s",createJsonObject())
        json.dump(createJsonObject(), outfile)
    logger.info("Json file created")