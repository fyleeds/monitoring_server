import sys
import os

sys.path.append(os.path.abspath('../reports/report'))
from log_report import logLastReport, logListReports
from create_report import  report_path, reports_path,createReport

sys.path.append(os.path.abspath('../reports/report_average'))
from create_report_average import report_average_path,reports_average_path,createReportAverage

sys.path.append(os.path.abspath('../config'))
from create_folder import configs_path,config_path,createConfig
    
def main():
    
    paths = [reports_path,reports_average_path,configs_path]
    for path in paths:
        os.makedirs(path)
    
    createConfig(config_path)
    createReport(report_path)
    # createReportAverage(1,reports_path,report_average_path)
    
    logLastReport(reports_path)
    # logListReports(reports_path)
    # logLastReport(reports_average_path)
    # logListReports(reports_average_path)

    
    

if __name__ == "__main__":
    main()