import os

def getListDir(dir):
    return [file.name for file in os.scandir(dir)]
