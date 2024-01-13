import sys
import os

sys.path.append(os.path.abspath('../report'))

from get_report import logLastReport, logListReports, logLastReportAverage

# sys.path.append(os.path.abspath('../log'))
# from logger_config import setup_logger


    
def main():
    # logLastReport()
    # logListReports()
    logLastReportAverage()
    
    

if __name__ == "__main__":
    main()