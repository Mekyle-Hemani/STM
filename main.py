import importlib.util
import subprocess
import sys
import colourprint
import time

def checkPackage(package):
    colourprint.print_colored(f"Verifying installation of {package}...", colourprint.YELLOW)
    if importlib.util.find_spec(package) is None:
        colourprint.print_colored(f"{package} is not installed. Do you want to install it? (y/n): ", colourprint.BLUE)
        choice = input().strip().lower()
        if choice == 'y':
            subprocess.run([sys.executable, "-m", "pip", "install", package])
            colourprint.print_colored(f"{package} is installed", colourprint.GREEN)
        else:
            colourprint.print_colored("Quiting... ", colourprint.RED)
            exit()
    else:
        colourprint.print_colored(f"{package} is installed", colourprint.GREEN)

checkPackage("tkinter")

import recieve
import imager

def checkSubsystems():
    out=True
    if recieve.setup() == False:
        colourprint.print_colored("STM communication failed", color_code=colourprint.RED)
        out=False
    else:
        colourprint.print_colored("STM communication established", color_code=colourprint.BLUE)

    time.sleep(3)
    return out

def startImaging():
    return recieve.startSTM()

def getTime(): return time.strftime("Date: %d-%m-%Y Time: %H:%M:%S", time.localtime())
    

if checkSubsystems():
    colourprint.print_colored("STM subsystems ready", color_code=colourprint.GREEN)
    if startImaging():
        colourprint.print_colored(f"STM grabbing data process started at {getTime()}", color_code=colourprint.GREEN)

        recieve.checkElectronDistanceProcess()

        while True:
            if recieve.doneImage:
                break

        colourprint.print_colored(f"STM done grabbing data at {getTime()}", color_code=colourprint.GREEN)

        colourprint.print_colored(f"Starting imaging process at {getTime()}", color_code=colourprint.BLUE)

        imager.image(recieve.data)