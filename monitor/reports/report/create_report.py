import sys 
import os
import json
import uuid
from datetime import datetime
import pytz

sys.path.append(os.path.abspath('../measures'))
from CPU import getCpuObject
# from DISK import getDisksObject
from RAM import getRamObject
from TCP import getTcpObject

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
logger = setup_logger("create_report_logger")

id_str = str(uuid.uuid4())
date_str = datetime.now( pytz.timezone('Europe/Paris')).strftime("%d-%m-%Y_%H-%M-%S")

report_name = "report_monit_"+ id_str +"_" + date_str + ".json"
base_path = "../../var/monit"
reports_path = base_path + "/reports/"
report_path = reports_path + report_name


def createReportObject(cpu,ram,tcp):

    return {
        "id": id_str,
        "timestamp": date_str,
        "cpu": cpu,
        "ram": ram,
        "network": tcp,
    }
    # "disk": getDisksObject()

def createReport(path): 
    with open(path, 'w') as outfile:
        json.dump(createReportObject(getCpuObject(),getRamObject(),getTcpObject()), outfile)
    logger.info("Report file created at %s",path)