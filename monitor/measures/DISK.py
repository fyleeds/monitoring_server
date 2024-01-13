# On importe la lib argparse
import argparse
import sys
import os
import time
import psutil

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("disk_logger")

def getDisksPartitionsInternal():
    return psutil.disk_partitions(all=False)

def getUsageDisk(path):
    return psutil.disk_usage(path)

def getDisksObject():
    return [ {"device":disk.device,"mountpoint":disk.mountpoint,"fstype":disk.fstype,"totalMemory": getUsageDiskValue(disk.device),"availableMemory": getAvailableMemoryValue(disk.device),"availableMemoryPercent": getAvailableMemoryPercentValue(disk.device),"usedMemory": getUsedMemoryValue(disk.device),"totalDiskValue": getTotalDiskValue(disk.device)} for disk in getDisksPartitionsInternal()]

def getUsageDiskValue(path):
    return psutil.disk_usage(path)

def getTotalDiskValue(path):
    return getUsageDisk(path).total

def getUsedMemoryValue(path):
    return getUsageDisk(path).used

def getAvailableMemoryValue(path):
    return getUsageDisk(path).free

def getAvailableMemoryPercentValue(path):
    return getUsageDisk(path).percent

