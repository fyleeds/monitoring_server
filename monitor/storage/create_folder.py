import os

from monitor.storage.check_storage import isDirMonitExist

def makeDir(path):
    if not isDirMonitExist(path):
       os.makedirs(path)
       
