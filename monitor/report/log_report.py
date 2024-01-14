import sys
import os

from get_report import path_reports, path_reports_average, getLastReportAverageName, getLastReportName

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("log_report_logger")

# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../storage'))
from get_storage import getListStorage


def logReport(report_name):
    with open(path_reports+report_name) as report:
        logger.info("Checking %s : %s",report_name,report.read())

def logReportAverage(report_name):
    with open(path_reports_average+report_name) as report:
        logger.info("Checking %s : %s",report_name,report.read())

def logListReports():
    logger.info(getListStorage(path_reports))

def logLastReport():
    logReport(getLastReportName())
    
def logLastReportAverage():
    logReportAverage(getLastReportAverageName())