import sys 
import os
import json
import uuid
from datetime import datetime
import pytz
from compute_report import getAverageReport
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

def createReportObject(cpu,ram,tcp):

    return {
        "id": id_str,
        "timestamp": date_str,
        "cpu": cpu,
        "ram": ram,
        "tcp": tcp,
    }
    # "disk": getDisksObject()

def createReport(cpu,ram,tcp,is_average=False):
    if is_average:
        reportname = "report_average_" + id_str +"_" + date_str + ".json"
        reportpath = "../../var/monit/reports_average/" + reportname
    else:
        reportname = "report_"+ id_str +"_" + date_str + ".json"
        reportpath = "../../var/monit/reports/" + reportname
        
    with open(reportpath, 'w') as outfile:
        json.dump(createReportObject(cpu,ram,tcp), outfile)
        
    if is_average:
        logger.info("Average report file created at %s",reportpath)
    else:
        logger.info("Report file created at %s",reportpath)

def createReportAverage(hours):
    cpu,ram,tcp= getAverageReport(hours)
    return createReport(cpu,ram,tcp,True)
    

# def main():
#     # createReport(getCpuObject(),getRamObject(),getTcpObject(),False)
#     # createReportAverage(1)
    
# if __name__ == "__main__":
#     main()