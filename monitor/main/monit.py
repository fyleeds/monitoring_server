import sys
import os

sys.path.append(os.path.abspath('../report'))

from get_report import logLastReport

# sys.path.append(os.path.abspath('../log'))
# from logger_config import setup_logger


    
def main():
    logLastReport()
    

if __name__ == "__main__":
    main()