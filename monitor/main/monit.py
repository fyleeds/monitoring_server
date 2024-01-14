import sys
import os
import argparse

sys.path.append(os.path.abspath('../reports/report'))
from log_report import logLastReport, logListReports
from create_report import  report_path, reports_path,createReport

sys.path.append(os.path.abspath('../reports/report_average'))
from create_report_average import report_average_path,reports_average_path,createReportAverage

sys.path.append(os.path.abspath('../config'))
from create_config import configs_path,config_path,createConfig

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("monit_logger")

sys.path.append(os.path.abspath('../arguments'))
from create_arguments import createArguments
from check_arguments import checkAvg

parser = argparse.ArgumentParser()


def main():
    paths = [reports_path,reports_average_path,configs_path]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    
    createArguments(parser)
    args = parser.parse_args()
    if args.check:
        createReport(report_path)
    elif args.list:
        logListReports(reports_path)
        logger.info("List of reports sended")
    elif args.last :
        logLastReport(reports_path)
        logger.info("Last report sended")
    elif checkAvg(args):
        createReportAverage(args.get_avg,reports_path,report_average_path)
        logLastReport(reports_average_path)
        logger.info("Report average for %s hours created at %s",args.get_avg,report_average_path)
    
if __name__ == "__main__":
    main()