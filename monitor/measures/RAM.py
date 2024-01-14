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
