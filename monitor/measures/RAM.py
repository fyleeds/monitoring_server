# On importe la lib argparse
import argparse
import sys
import os
import time
import psutil
import json

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("ram_logger")


def getMemory():
    return psutil.virtual_memory()

# def getTotalMemory():
#     total_memory_str  = "Total Memory : " + str("{:,}".format(getMemory().total))+" bytes"
#     logger.info (total_memory_str)
#     return total_memory_str
# def getAvailableMemory():
#     available_memory_str  = "Available Memory : " + str("{:,}".format(getMemory().available))+" bytes"
#     logger.info (available_memory_str)
#     return available_memory_str
# def getUsedMemoryPercent():
#     available_memory_percent_str  = "Available Memory : " + str(getMemory().percent)+" %"
#     logger.info (available_memory_percent_str)
#     return available_memory_percent_str

# def getCacheBuffers():
#     cache_buffers_str  = "Cache system metadata. : " + str("{:,}".format(getMemory().buffers))+" bytes"
#     logger.info (cache_buffers_str)
#     return cache_buffers_str

# def getCache():
#     cache_str  = "Cache : " + str("{:,}".format(getMemory().cached))+" bytes"
#     logger.info (cache_str)
#     return cache_str

def getTotalMemory():
    return getMemory().total
def getAvailableMemory():
    return getMemory().available
def getUsedMemoryPercent():
    return getMemory().percent
def getCacheBuffers():
    return getMemory().buffers
def getCache():
    return getMemory().cached

def getRamObject():
    return {"totalMemory": getTotalMemory(),"availableMemory": getAvailableMemory(),"usedMemoryPercent": getUsedMemoryPercent(),"cacheBuffers": getCacheBuffers(),"cache": getCache()}
