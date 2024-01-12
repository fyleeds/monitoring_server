# On importe la lib argparse
import argparse
import sys
import os
import time
import psutil

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("tcp_logger")


def getConnections():
    return psutil.net_connections(kind='tcp')

def getStatusConnections():
    for connection in getConnections():
        if connection.status == psutil.CONN_ESTABLISHED:
            return connection.laddr
        
def getPortConnections():
    port_opened_str = "Port opened : " + str(getStatusConnections().port)
    logger.info(port_opened_str)
    return port_opened_str

def getPortConnectionsValue():
    return getStatusConnections().port

# Create a JSON object with TCP connections stats
def getTcpObject():
    return {
        "ports": getPortConnectionsValue()
    }
