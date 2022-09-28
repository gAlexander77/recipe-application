from os import mkdir
from os.path import isdir
from datetime import datetime


LOGS: str = "./log"
if not isdir(LOGS):
    mkdir(LOGS)


def log(message: str, path: str):
    stamp: str = datetime.now().strftime("%I:%M:%S - %b %d, %Y")
    output: str = f"[{stamp}]: {message}"
    print(output)
    with open(path, "at+", 0o660) as file:
        print(output, file=file)

def msg(message: str): 
    return log(message, f"{LOGS}/api.log")

def err(message: str, error: Exception=None):
    return log(message, f"{LOGS}/err.log")
