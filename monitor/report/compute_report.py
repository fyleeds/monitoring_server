import sys 
import os
from manage_report import listReports
from datetime import datetime,timezone,timedelta
import pytz

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("compute_report_logger")


def getAverageReport(hours):
    # .strftime("%d-%m-%Y_%H-%M-%S")
    list_reports = listReports()
    tz= pytz.timezone('Europe/Paris')
    date_wanted = datetime.now(tz) - timedelta(hours=hours)
    for report_name in list_reports:
        date_report = tz.localize(datetime.strptime(" ".join(report_name.split(".")[0].split("_")[len(report_name.split(".")[0].split("_"))-2:]), "%d-%m-%Y %H-%M-%S"))
        if date_report > date_wanted:
            logger.info(report_name)
            logger.info(date_report)
            logger.info(date_wanted)
            logger.info("Report is in the time range")
def main():
    getAverageReport(1)

if __name__ == "__main__":
    main()