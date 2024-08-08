"""custom module for logging"""
from datetime import datetime
import os.path

# INIT CONSTANTS
LOG_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\db\\log.txt'

def logData(data):
    """Logs data to a text file

    Args:
        data (str): data
    """

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    fp = open(LOG_FILE_PATH, "a+")
    fp.write(f"{timestamp} :: {data}\n")
    fp.close()