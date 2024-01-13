# On importe la lib argparse
import argparse
import sys
import os 
import time
import psutil

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("cpu_logger")

# Création d'un objet ArgumentParser
# parser = argparse.ArgumentParser()

# # On ajoute la gestion de l'option -n ou --name
# # "store" ça veut dire qu'on attend un argument à -n

# # on va stocker l'argument dans une variable
# parser.add_argument( help="Usage: python bs_server.py [OPTION]..."
#                     "Run a server"
#                     "Mandatory arguments to long options are mandatory for short options too."
#                     "-h, --help                  Help of the command"
# )

# # Permet de mettre à jour notre objet ArgumentParser avec les nouvelles options
# # 
# if (parser.parse_args()):
#     args = parser.parse_args()
# else : 
#     pass
# print(args.port)

# if (args.port < 0 or args.port> 65535):
#     print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
#     sys.exit(1)
# elif (args.port >= 0 and args.port<= 1024):
#     print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
#     sys.exit(2)



def getLoadsAvg():
    logger.debug("getLoadsAvg")
    load_avg = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    return {"1min": load_avg[0], "5min": load_avg[1], "15min": load_avg[2]}

def getCpuTimesValue():
    return psutil.cpu_times()

def getCpuTimeUserValue():
    return round(getCpuTimesValue().user, 2)

def getCpuTimeSystemValue():
    return round(getCpuTimesValue().system, 2)

def getCpuTimeIdleValue():
    return round(getCpuTimesValue().idle, 2)

def getCpuPercentValue():
    return psutil.cpu_percent(interval=1)

def getCpuCountValue():
    return psutil.cpu_count()

def getCpuStatsValue():
    return psutil.cpu_stats()

def getCpuFreqValue():
    return psutil.cpu_freq(percpu=False)

def getCpusFreqValue():
    return psutil.cpu_freq(percpu=True)

# Create a JSON object with CPU stats
def getCpuObject():
    return {
        "cpuTimeUser": getCpuTimeUserValue(),
        "cpuTimeSystem": getCpuTimeSystemValue(),
        "cpuTimeIdle": getCpuTimeIdleValue(),
        "cpuPercent": getCpuPercentValue(),
        "cpuCount": getCpuCountValue(),
        "cpuStats": getCpuStatsValue()._asdict(),  # Convert namedtuple to dictionary
        "cpuFreq": getCpuFreqValue()._asdict(),    # Convert namedtuple to dictionary
        "loadAvg": getLoadsAvg()   # Convert namedtuple to dictionary
    }