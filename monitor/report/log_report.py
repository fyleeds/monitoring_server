import sys
import os

from get_report import path_reports, path_reports_average, getLastReportAverageName, getLastReportName

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("get_report_logger")


def logReport(report_name):
    with open(path_reports+"/"+report_name) as report:
        logger.info("Checking %s : %s",report_name,report.read())

def logReportAverage(report_name):
    with open(path_reports_average+"/"+report_name) as report:
        logger.info("Checking %s : %s",report_name,report.read())

def logListReports():
    logger.info([file.name for file in os.scandir(path_reports)])

def logLastReport():
    logReport(getLastReportName())
    
def logLastReportAverage():
    logReportAverage(getLastReportAverageName())