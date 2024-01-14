import sys
import os

base_path = "../../etc/monit/"

# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../storage'))
from create_folder import makeDir,getListDir

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("config_logger")

from get_config import base_path

config_name = "monit.conf"
config_path = base_path + config_name

def createConfigFolder():
    makeDir(base_path)
    
def createReport():
    with open(config_path, 'w') as outfile:
        json.dump(createReportObject(getCpuObject(),getRamObject(),getTcpObject()), outfile)
    logger.info("Report file created at %s",reportpath)