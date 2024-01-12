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

def getDisks():
    i=1
    for disk in getDisksPartitionsInternal():
        device_path_str = "Device path "+ str(i) + " : "+ disk.device
        mountpoint_str = "Mountpoint path "+ str(i) + " : "+ disk.mountpoint
        fstype = "Fstype "+ str(i) + " : "+ disk.fstype
        i = i + 1
        total_memory_str = getTotalDisk(disk.device)
        used_memory_str = getUsedMemory(disk.device)
        available_memory_str = getAvailableMemory(disk.device)
        available_memory_percent_str  = getAvailableMemoryPercent(disk.device)
        # Logger les informations
        log_message = ", ".join([device_path_str, mountpoint_str, fstype, total_memory_str, used_memory_str, available_memory_str, available_memory_percent_str])
        logger.info(log_message)
        
        return (device_path_str,mountpoint_str,fstype)

    return ""

def getUsageDisk(path):
    return psutil.disk_usage(path)

def getTotalDisk(path):
    total_memory_str  = "Total Memory : " + str("{:,}".format(getUsageDisk(path).total))+" bytes"
    logger.info (total_memory_str)
    return total_memory_str

def getUsedMemory(path):
    used_memory_str  = "Used Memory : "  + str("{:,}".format(getUsageDisk(path).used))+" bytes"
    logger.info (used_memory_str)
    return used_memory_str

def getAvailableMemory(path):
    available_memory_str  = "Available Memory : "  + str("{:,}".format(getUsageDisk(path).total))+" bytes"
    logger.info (available_memory_str)
    return available_memory_str

def getAvailableMemoryPercent(path):
    available_memory_percent_str  = "Available Memory : "  + str("{:,}".format(getUsageDisk(path).total))+" %"
    logger.info (available_memory_percent_str)
    return available_memory_percent_str

def getDisksObject():
    for disk in getDisksPartitionsInternal():
        return {"totalMemory": getUsageDiskValue(disk.device),"availableMemory": getAvailableMemoryValue(disk.device),"availableMemoryPercent": getAvailableMemoryPercentValue(disk.device),"usedMemory": getUsedMemoryValue(disk.device),"totalDiskValue": getTotalDiskValue(disk.device)}

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

