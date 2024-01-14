import os 

def isDirMonitExist(dir):
    if not os.path.exists(dir):
        return False
    else:
        return True
