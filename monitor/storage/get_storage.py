import os

def getListStorage(dir):
    return [file.name for file in os.scandir(dir)]
