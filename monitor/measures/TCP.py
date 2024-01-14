
import sys
import os
import psutil
from collections import defaultdict

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("tcp_logger")

sys.path.append(os.path.abspath('../config'))
from get_config import getConfig,config_path

def getConnections():
    return psutil.net_connections(kind='tcp')

def getStatusConnections():
    for connection in getConnections():
        if connection.status == psutil.CONN_ESTABLISHED:
            return connection.laddr
        
def checkConfig():
    config = getConfig(config_path)
    ports_dict = defaultdict(lambda: defaultdict(bool))
    if config["ports"]["tcp"] == []:
        logger.error("No port specified in config file")
        sys.exit(1)
    else:
        logger.info("Port specified in config file")
        for port in config["ports"]["tcp"]:
            port_str = str(port)
            logger.info("Port %s",port)
            if port in getPortConnectionsValue():
                logger.info("Port %s is open",port)
                ports_dict["ports"][port_str] = True
            else:
                logger.error("Port %s is not open",port)
                ports_dict["ports"][port_str] = False
    return ports_dict

def getPortConnectionsValue():
    return getStatusConnections().port

def getTcpObject():
    return checkConfig()
