import sys 
import os
import uuid
from datetime import datetime
import pytz
import json
from compute_report import getAverageReport

sys.path.append(os.path.abspath('../report'))
from create_report import createReportObject

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
logger = setup_logger("create_report_average_logger")

id_str = str(uuid.uuid4())
date_str = datetime.now( pytz.timezone('Europe/Paris')).strftime("%d-%m-%Y_%H-%M-%S")

report_name = "report_monit_average_"+ id_str +"_" + date_str + ".json"
base_path = "../../var/monit"
reports_average_path = base_path + "/reports_average/"
report_average_path = reports_average_path + report_name

def createReportAverage(hours,reports_path,report_average_path):
    cpu,ram,tcp= getAverageReport(hours,reports_path)
    with open(report_average_path, 'w') as outfile:
        json.dump(createReportObject(cpu,ram,tcp), outfile)
    logger.info("Average report file created at %s",report_average_path)