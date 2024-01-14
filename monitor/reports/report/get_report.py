import sys 
import os
from datetime import datetime,timedelta
import pytz

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
logger = setup_logger("get_report_logger")

sys.path.append(os.path.abspath('../storage'))
from get_storage import getListStorage,getJsonFile

tz= pytz.timezone('Europe/Paris')
date =  datetime.now(tz)

def getReportRamInfos(path,report_name):
    return getJsonFile(path+report_name)["ram"].items()

def getReportCpuInfos(path,report_name):
    return getJsonFile(path+report_name)["cpu"].items()

def getLastReportName(path):
    date2 = datetime(1970,1,1,0,0,0,0,tzinfo=tz)
    for report_name in getListStorage(path):
        date1 = getDateTimeReport(report_name)
        if (date1 > date2):
            date2 = date1
            most_recent_report = report_name
    return most_recent_report

def getDateTimeReport(report_name):
    return tz.localize(datetime.strptime(" ".join(report_name.split(".")[0].split("_")[len(report_name.split(".")[0].split("_"))-2:]), "%d-%m-%Y %H-%M-%S"))

def getListReportsLastHours(hours,path):
    list_reports = []
    date_wanted = date - timedelta(hours=hours)
    for report_name in getListStorage(path):
        if getDateTimeReport(report_name) > date_wanted:
            list_reports.append(report_name)
    return list_reports

# def main():


# if __name__ == "__main__":
#     main()