import os

from check_storage import isDirMonitExist

def makeDir(path):
    if not isDirMonitExist(path):
       os.makedirs(path)
       
