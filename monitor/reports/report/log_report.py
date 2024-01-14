import sys
import os

from get_report import getLastReportName

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
logger = setup_logger("log_report_logger")

sys.path.append(os.path.abspath('../storage'))
from get_storage import getListStorage

def logReport(report_path):
    with open(report_path) as report:
        logger.info("Checking : %s",report.read())

def logListReports(path):
    logger.info(getListStorage(path))

def logLastReport(path):
    logReport(path + getLastReportName(path))