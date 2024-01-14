import argparse
import sys
import os

sys.path.append(os.path.abspath('../log'))
from logger_config import setup_logger
# Créer une instance de logger pour ce fichier
logger = setup_logger("create_arguments_logger")


def createArguments(parser):
    parser.add_argument("-get_avg", type=int, default=1, help=" Writes a report_average file saved in the folder /var/reports/report_average based on the reports created in the number hours you have given as argument (must be a int), when no argument given write an average report based on 1 hour")
    parser.add_argument("-check",action='store_true',help="Write a report saved in the folder /var/reports/report recording theses values with specific units : CPU Metrics: cpuTimeUser, cpuTimeSystem, cpuTimeIdle: Seconds; cpuPercent: Percentage; cpuCount: Count; cpuStats - ctx_switches, interrupts, soft_interrupts, syscalls: Count; cpuFreq - current, min, max: MHz; loadAvg - 1min 5min 15min: Load Average; RAM Metrics: totalMemory, availableMemory, cacheBuffers, cache: Bytes; usedMemoryPercent: Percentage; Network Metrics: tcp - Port numbers: Boolean status true/false; Disk Information: totalSpace, usedSpace, freeSpace: Bytes; readSpeed, writeSpeed: MB/s Megabytes per second or IOPS")
    parser.add_argument("-list", action='store_true', help="List all reports")
    parser.add_argument("-last", action='store_true', help="Send the last report")
    return parser
