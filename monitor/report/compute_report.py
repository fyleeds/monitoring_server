import sys 
import os
from get_report import getListReportsLastHours,getReportRamInfos,getReportCpuInfos
from collections import defaultdict


sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("compute_report_logger")
    
def isSubValueImportantCpu(key, value):
    if isinstance(value, dict) and key == "cpuFreq":
        return True
    return False

def isValueImportantCpu(key):
    if "cpuPercent" in key:
        return True
    return False

def getSumReports(list_reports):
    sum_dicts = defaultdict(lambda: defaultdict(float))

    for report_name in list_reports:
        for key, value in getReportRamInfos(report_name):
            sum_dicts["ram"][key] += value

        for key, value in getReportCpuInfos(report_name):
            if isSubValueImportantCpu(key, value):
                if isinstance(sum_dicts["cpu"][key], float):
                    # Initialize as a new defaultdict if it's currently a float
                    sum_dicts["cpu"][key] = defaultdict(float)
                for sub_key, sub_value in value.items():
                    sum_dicts["cpu"][key][sub_key] += sub_value

            elif not isinstance(value, dict) and isValueImportantCpu(key):
                sum_dicts["cpu"][key] += value

    tcp_data = {"": ""}
    return sum_dicts["cpu"], sum_dicts["ram"], tcp_data

def getAverageReport(hours):
    sum_dicts = defaultdict(lambda: defaultdict(float))
    list_reports = getListReportsLastHours(hours)
    length = len(list_reports)
    if length == 0:
        return None, None, None
    else:
        sum_dicts["cpu"], sum_dicts["ram"], tcp_data = getSumReports( list_reports)

        # Calculating averages
        for key, value in sum_dicts["ram"].items():
            sum_dicts["ram"][key] = value / length

        for key, value in sum_dicts["cpu"].items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    sum_dicts["cpu"][key][sub_key] = sub_value / length
            else:
                sum_dicts["cpu"][key] = value / length

        tcp_data = {"": ""}
        return sum_dicts["cpu"], sum_dicts["ram"], tcp_data

           
def main():
    getAverageReport(10)

if __name__ == "__main__":
    main()