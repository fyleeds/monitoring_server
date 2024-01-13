
import sys
import os 
import psutil

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("cpu_logger")


def getLoadsAvg():
    logger.debug("getLoadsAvg")
    load_avg = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    return {"1min": load_avg[0], "5min": load_avg[1], "15min": load_avg[2]}

def getCpuTimesValue():
    return psutil.cpu_times()

def getCpuTimeUserValue():
    return round(getCpuTimesValue().user, 2)

def getCpuTimeSystemValue():
    return round(getCpuTimesValue().system, 2)

def getCpuTimeIdleValue():
    return round(getCpuTimesValue().idle, 2)

def getCpuPercentValue():
    return psutil.cpu_percent(interval=1)

def getCpuCountValue():
    return psutil.cpu_count()

def getCpuStatsValue():
    return psutil.cpu_stats()

def getCpuFreqValue():
    return psutil.cpu_freq(percpu=False)

def getCpusFreqValue():
    return psutil.cpu_freq(percpu=True)

# Create a JSON object with CPU stats
def getCpuObject():
    return {
        "cpuTimeUser": getCpuTimeUserValue(),
        "cpuTimeSystem": getCpuTimeSystemValue(),
        "cpuTimeIdle": getCpuTimeIdleValue(),
        "cpuPercent": getCpuPercentValue(),
        "cpuCount": getCpuCountValue(),
        "cpuStats": getCpuStatsValue()._asdict(),  # Convert namedtuple to dictionary
        "cpuFreq": getCpuFreqValue()._asdict(),    # Convert namedtuple to dictionary
        "loadAvg": getLoadsAvg()   # Convert namedtuple to dictionary
    }