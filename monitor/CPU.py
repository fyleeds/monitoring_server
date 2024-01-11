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

# Créer une instance de logger pour ce fichier
logger = setup_logger()

def getCpuTimes():
    return psutil.cpu_times()

def getCpuTimeUser():  
    cpu_time_user = round(getCpuTimes().user,2)
    cpu_time_user_str =  "User time spend: "+ str(cpu_time_user) + " seconds"
    logger.info(cpu_time_user_str)
    return cpu_time_user_str

def getCpuTimeSystem():  
    cpu_time_system = round(getCpuTimes().system,2)
    cpu_time_system_str = "System time spend: "+ str(cpu_time_system) + " seconds"
    logger.info(cpu_time_system_str)
    return cpu_time_system_str

def getCpuTimeIdle():  
    cpu_time_idle = round(getCpuTimes().idle,2)
    cpu_time_idle_str =  "Idle time spend: "+ str(cpu_time_idle) + " seconds"
    logger.info(cpu_time_idle_str)
    return cpu_time_idle_str

def getCpusPercent():
    cpus_percent =  psutil.cpu_percent(interval=1, percpu=True)
    i=1
    for cpu_percent in cpus_percent:
        if cpu_percent != 0:
            cpu_percent_str = "CPU " + str(i) + " utilization: " + str(cpu_percent) +" % "
            logger.info(cpu_percent_str)
            return cpu_percent_str
        i = i + 1
    return ""

def getCpuPercent():
    cpu_percent_str = "CPU utilization: " + str( psutil.cpu_percent(interval=1) ) +" % "
    logger.info(cpu_percent_str)
    return cpu_percent_str

def getCpuCount():
    cpu_count_str = "Number of Logical CPU : "+ str(psutil.cpu_count())
    logger.info(cpu_count_str)
    return cpu_count_str

def getCpuStats():
    return psutil.cpu_stats()

def getCtxSwitches():
    context_switches_str = "Number of context switches :" + str(getCpuStats().ctx_switches)
    logger.info(context_switches_str)
    return context_switches_str
    
def getInterrupts():
    interrupt_str = "Number of interruptions :" + str(getCpuStats().interrupts)
    logger.info(interrupt_str)
    return interrupt_str

def getSoftInterrupts():
    soft_interrupt_str = "Number of software interruptions "+ str(getCpuStats().soft_interrupts)
    logger.info(soft_interrupt_str)
    return soft_interrupt_str

def getCpuFreq():
    return psutil.cpu_freq(percpu=False)
def getCurrentCpuFreq():
    current_cpu_freq_str = "Current CPU frequence :" + str(getCpuFreq().current)+"Mhz"
    logger.info(current_cpu_freq_str)
    return current_cpu_freq_str
def getMinCpuFreq():
    min_cpu_freq_str = "Min CPU frequence :" + str(getCpuFreq().min) +"Mhz"
    logger.info(min_cpu_freq_str)
    return min_cpu_freq_str
def getMaxCpuFreq():
    max_cpu_freq_str = "Max CPU frequence :" + str(getCpuFreq().max)+"Mhz"
    logger.info(max_cpu_freq_str)
    return max_cpu_freq_str

def getCpusFreq():
    i=1
    for cpu_freq in psutil.cpu_freq(percpu=True):
        if cpu_freq != 0:
            current_cpu_freq_str = "Current CPU "+ str(i) +" frequence :" + str(cpu_freq.current)+"Mhz"
            min_cpu_freq_str = "Min CPU "+ str(i) +" frequence :" + str(cpu_freq.min) +"Mhz"
            max_cpu_freq_str = "Max CPU "+ str(i) +" frequence :" + str(cpu_freq.max)+"Mhz"
            
            # Logger les informations
            log_message = ", ".join([current_cpu_freq_str, min_cpu_freq_str, max_cpu_freq_str])
            logger.info(log_message)
            
            return (current_cpu_freq_str,min_cpu_freq_str,max_cpu_freq_str)
        i = i + 1
    return ""

def getLoadAvg():
    i=1
    for loadavg in [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]:
        if loadavg != 0:
            if i == 1 :
                loadavg_str = "Load average from 1 min : "+ str(i) +"frequence :" + str(loadavg)+"%"
                logger.info(loadavg_str)
                return loadavg_str
            if i == 2 :
                loadavg_str = "Load average from 10 min : "+ str(i) +"frequence :" + str(loadavg)+"%"
                logger.info(loadavg_str)
                return loadavg_str
            if i == 3 :
                loadavg_str = "Load average from 15 min : "+ str(i) +"frequence :" + str(loadavg)+"%"
                logger.info(loadavg_str)
                return loadavg_str
        i = i+1
    return ""

def main():

    getCpuTimeUser()
    getCpuTimeSystem()
    getCpuTimeIdle()
    getCpusPercent()
    getCpuPercent()
    getCpuCount()
    getCtxSwitches()
    getInterrupts()
    getSoftInterrupts()
    getCpuFreq()
    getCurrentCpuFreq()
    getMinCpuFreq()
    getMaxCpuFreq()
    getLoadAvg()
    getCpusFreq()
    

if __name__ == "__main__":

    main()