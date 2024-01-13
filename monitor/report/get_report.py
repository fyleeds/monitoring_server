import sys 
import os
from datetime import datetime,timezone,timedelta
import pytz
import json

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("get_report_logger")

path = "../../var/monit/reports"
tz= pytz.timezone('Europe/Paris')
date =  datetime.now(tz)

def getListReportsLog():
    list_reports = [file.name for file in os.scandir(path)]
    logger.info(list_reports)

def getListReports():
    list_reports = [file.name for file in os.scandir(path)]
    return list_reports

def getListReportsLastHours(hours):
    list_reports = []
    date_wanted = date - timedelta(hours=hours)
    for report_name in getListReports():
        if getDateTimeReport(report_name) > date_wanted:
            list_reports.append(report_name)
    return list_reports

def getDateTimeReport(report_name):
    date_report = tz.localize(datetime.strptime(" ".join(report_name.split(".")[0].split("_")[len(report_name.split(".")[0].split("_"))-2:]), "%d-%m-%Y %H-%M-%S"))
    return date_report

def openReportAsStr(report_name):
    with open(path+"/"+report_name) as report:
        return report.read()
    
def openReportAsDict(report_name):
    return json.loads(openReportAsStr(report_name))

def logReport(report_name):
    with open(path+"/"+report_name) as report:
        logger.info("Checking %s : %s",report_name,report.read())

def getLastReport():
    date2 = datetime(1970,1,1,0,0,0,0,tzinfo=tz)
    for report_name in getListReports():
        date1 = getDateTimeReport(report_name)
        if (date1 > date2):
            most_recent_report = report_name
    logReport(most_recent_report)
    return most_recent_report

def main():
    getLastReport()
    
if __name__ == "__main__":
    main()