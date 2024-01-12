import sys 
import os
from get_report import getListReportsLastHours


sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("compute_report_logger")


def getAverageReport(hours):
    list_reports = getListReportsLastHours(hours)
def main():
    getAverageReport(1)

if __name__ == "__main__":
    main()