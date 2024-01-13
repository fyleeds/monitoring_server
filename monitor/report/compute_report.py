import sys 
import os
from get_report import getListReportsLastHours,openReportAsDict
from collections import defaultdict


sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("compute_report_logger")


def getAverageReport(hours):
    
    sum_dicts = defaultdict(lambda: defaultdict(float))
    i=0
    list_reports = getListReportsLastHours(hours)
    if list_reports == None:
        return None,None,None
    else :
        for report_name in list_reports:
            report = openReportAsDict(report_name)
            
            for key, value in report["ram"].items():
                    sum_dicts["ram"][key] += value

            for key, value in report["cpu"].items():
                if key == "cpuFreq" or key == "loadAvg":
                    for sub_key, sub_value in value.items(): 
                        sum_dicts["cpu"][f"{key}_{sub_key}"] += sub_value
                elif key == "cpuPercent":
                    sum_dicts["cpu"][key] += value

            i = i + 1
        for key, value in sum_dicts["ram"].items():
            sum_dicts["ram"][key] = value / i
        for key, value in sum_dicts["cpu"].items():
            sum_dicts["cpu"][key] = value / i
        tcp_data = {"": ""}
        
        return sum_dicts["cpu"],sum_dicts["ram"],tcp_data

           
def main():
    getAverageReport(10)

if __name__ == "__main__":
    main()