import initialization.packageCheck

def checkAll():
    dependencies = ["tkinter", "serial"]
    result=True
    for item in dependencies:
        initialization.packageCheck.checkPackage(item)
    return result