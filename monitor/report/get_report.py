import sys 
import os
from datetime import datetime,timedelta
import pytz


sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("get_report_logger")

# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../storage'))
from get_storage import getListStorage,getJsonFile

base_path = "../../var/monit"
path_reports = base_path + "/reports/"
path_reports_average = base_path + "/reports_average/"

tz= pytz.timezone('Europe/Paris')
date =  datetime.now(tz)

def getReportRamInfos(report_name):
    return getJsonFile(path_reports+report_name)["ram"].items()

def getReportCpuInfos(report_name):
    return getJsonFile(path_reports+report_name)["cpu"].items()

def getLastReportName():
    date2 = datetime(1970,1,1,0,0,0,0,tzinfo=tz)
    for report_name in getListStorage(path_reports):
        date1 = getDateTimeReport(report_name)
        if (date1 > date2):
            most_recent_report = report_name
    return most_recent_report

def getLastReportAverageName():
    date2 = datetime(1970,1,1,0,0,0,0,tzinfo=tz)
    for report_name in getListStorage(path_reports_average):
        date1 = getDateTimeReport(report_name)
        if (date1 > date2):
            most_recent_report = report_name
    return most_recent_report

def getDateTimeReport(report_name):
    date_report = tz.localize(datetime.strptime(" ".join(report_name.split(".")[0].split("_")[len(report_name.split(".")[0].split("_"))-2:]), "%d-%m-%Y %H-%M-%S"))
    return date_report

def getListReportsLastHours(hours):
    list_reports = []
    date_wanted = date - timedelta(hours=hours)
    for report_name in getListStorage(path_reports):
        if getDateTimeReport(report_name) > date_wanted:
            list_reports.append(report_name)
    return list_reports

# def main():


# if __name__ == "__main__":
#     main()