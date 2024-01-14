import os


from monitor.storage.check_storage import isDirMonitExist

def makeDirReports(base_path):
    if not isDirMonitExist(base_path):
       os.makedirs(base_path+"reports_average")
       os.makedirs(base_path+"reports")
    elif not isDirMonitExist(base_path + "reports_average"):
       os.makedirs(base_path+"reports_average")
    elif not isDirMonitExist(base_path + "reports"):
       os.makedirs(base_path+"reports")

def makeDir(base_path):
    if not isDirMonitExist(base_path):
       os.makedirs(base_path)
       
