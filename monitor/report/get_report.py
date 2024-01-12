import sys 
import os
from datetime import datetime,timezone,timedelta
import pytz

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("get_report_logger")

path = "../../var/monit"
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
            logger.info(report_name)
            logger.info("Report is in the time range")
            list_reports.append(report_name)
    return list_reports

def getDateTimeReport(report_name):
    date_report = tz.localize(datetime.strptime(" ".join(report_name.split(".")[0].split("_")[len(report_name.split(".")[0].split("_"))-2:]), "%d-%m-%Y %H-%M-%S"))
    return date_report
  
def getLastReport():
    list_reports = []
    # datetime most_recent_date 
    # for report_name in getListReports():
    #     getLastDateTimeReport(getDateTimeReport(report_name)
    #     if date1 > date2:
    #         return date1
    #     else:
    #         return date2


    #     logger.info(list)

def main():
    getLastReport()
if __name__ == "__main__":
    main()