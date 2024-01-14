import sys
import os

sys.path.append(os.path.abspath('../report'))

from log_report import logLastReport, logListReports, logLastReportAverage
from create_report import createReportAverage, createReport
# sys.path.append(os.path.abspath('../log'))
# from logger_config import setup_logger


    
def main():

    createReport()
    createReportAverage(1)
    logLastReportAverage()
    logLastReport()
    logListReports()
    
    

if __name__ == "__main__":
    main()