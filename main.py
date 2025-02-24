import recieve
import imager
import colourprint
import time

def checkSubsystems():
    out=True
    if recieve.setup() == False:
        colourprint.print_colored("STM communication failed", color_code=colourprint.RED)
        out=False
    else:
        colourprint.print_colored("STM communication established", color_code=colourprint.BLUE)

    time.sleep(3)

    if imager.setup() == False:
        colourprint.print_colored("STM imaging software failed", color_code=colourprint.RED)
        out=False
    else:
        colourprint.print_colored("STM imaging software established", color_code=colourprint.BLUE)
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