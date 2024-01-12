import sys 
import os
import json
import uuid
from datetime import datetime,timezone
import pytz

# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../measures'))

from CPU import getCpuObject
# from DISK import getDisksObject
from RAM import getRamObject
from TCP import getTcpObject

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("create_report_logger")

id_str = str(uuid.uuid4())
date_str = datetime.now( pytz.timezone('Europe/Paris')).strftime("%d-%m-%Y_%H-%M-%S")

def createReportObject():

    return {
        "id": id_str,
        "timestamp": date_str,
        "cpu": getCpuObject(),
        "ram": getRamObject(),
        "tcp": getTcpObject(),
    }
    # "disk": getDisksObject()

def createReport():
    reportname = "report_"+ id_str +"_" + date_str + ".json"
    reportpath = "../../var/monit/" + reportname
    
    with open(reportpath, 'w') as outfile:
        json.dump(createReportObject(), outfile)
    logger.info("Json file created at %s",reportpath)


    
def main():
    createReport()

if __name__ == "__main__":
    main()