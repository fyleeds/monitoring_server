import os
import json

def getListStorage(dir):
    return [file.name for file in os.scandir(dir)]

def getFile(path):
    with open(path) as report:
        return report.read()
    
def getJsonFile(path):
    with open(path) as report:
        return json.loads(report.read())