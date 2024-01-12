import sys 
import os


sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("manage_report_logger")

path = "../../var/monit"

def listReportsLogs():
    list_reports = [file.name for file in os.scandir(path)]
    logger.info(list_reports)

def listReports():
    list_reports = [file.name for file in os.scandir(path)]
    return list_reports

def lastReport():
    for file in os.scandir(path):
        logger.info(file.name)
        return file.name
    # last_report = os.scandir(path)[len(os.scandir(path))-1]
    # logger.info(last_report.name)
    # return last_report.name

def main():
    lastReport()
if __name__ == "__main__":
    main()