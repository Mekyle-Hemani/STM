import time

doneImage=False
data = []

def setup():
    return True

def startSTM():
    return True

def checkElectronDistanceProcess():
    global doneImage
    global data
    time.sleep(3)
    doneImage=True

    import random
    data = [[random.uniform(0, 5) for _ in range(90)] for _ in range(160)]