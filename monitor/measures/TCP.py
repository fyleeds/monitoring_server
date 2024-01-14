
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
    if config["ports"] is not None and config["ports"].items is not None:
        for type,port in config["ports"].items():
            port_str = str(port)
            if isinstance(getPortConnectionsValue,dict):
                for port_connected in getPortConnectionsValue():
                    if port == port_connected:
                        ports_dict[type][port_str] = True
                    else:
                        ports_dict[type][port_str] = False
            else:
                if port == getPortConnectionsValue():
                        ports_dict[type][port_str] = True
                else:
                    ports_dict[type][port_str] = False    
    return ports_dict

def getPortConnectionsValue():
    return getStatusConnections().port

def getTcpObject():
    return checkConfig()
