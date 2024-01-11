# On importe la lib argparse
import argparse
import sys
import os
import time
import psutil

# Ajouter le chemin vers log_folder à sys.path
sys.path.append(os.path.abspath('../var/log'))

from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger()


def getMemory():
    return psutil.virtual_memory()

def getTotalMemory():
    total_memory_str  = "Total Memory : " + str("{:,}".format(getMemory().total))+" bytes"
    logger.info (total_memory_str)
    return total_memory_str
def getAvailableMemory():
    available_memory_str  = "Available Memory : " + str("{:,}".format(getMemory().available))+" bytes"
    logger.info (available_memory_str)
    return available_memory_str
def getAvailableMemoryPercent():
    available_memory_percent_str  = "Available Memory : " + str(getMemory().percent)+" %"
    logger.info (available_memory_percent_str)
    return available_memory_percent_str

def getCacheBuffers():
    cache_buffers_str  = "Cache system metadata. : " + str("{:,}".format(getMemory().buffers))+" bytes"
    logger.info (cache_buffers_str)
    return cache_buffers_str

def getCache():
    cache_str  = "Cache : " + str("{:,}".format(getMemory().cached))+" bytes"
    logger.info (cache_str)
    return cache_str

def main():
    getTotalMemory()
    getAvailableMemory()
    getAvailableMemoryPercent()
    getCacheBuffers()
    getCache()
    

if __name__ == "__main__":
    main()