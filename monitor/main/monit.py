import sys
import os

sys.path.append(os.path.abspath('../report'))

from get_report import logLastReport, logListReports, logLastReportAverage
from create_report import createReportAverage
# sys.path.append(os.path.abspath('../log'))
# from logger_config import setup_logger


    
def main():
    # logLastReport()
    # logListReports()
    createReportAverage(1)
    # logLastReportAverage()
    
    

if __name__ == "__main__":
    main()