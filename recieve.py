import time
import serial
import serial.tools.list_ports

doneImage=False
data = []

def setup():
    ports = list(serial.tools.list_ports.comports())
    com_ports = [port.device for port in ports]
    #Establish communication with the first COM port
    return True

def startSTM():
    #Turn the onboard LED on
    return True

def checkElectronDistanceProcess():
    global doneImage
    global data
    time.sleep(3)
    doneImage=True

    import random
    data = [[random.uniform(0, 5) for _ in range(90)] for _ in range(160)]

    #Turn the onboard LED on