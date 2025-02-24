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
    

if checkSubsystems():
    colourprint.print_colored("STM subsystems ready", color_code=colourprint.GREEN)

    