import initialization.packageCheck
import os
if os.name != "nt":
    import initialization.environmentCheck

def checkAll():
    result=True
    if os.name != "nt":
        initialization.environmentCheck.checkEnvironment()
    else:
        import colourprint
        colourprint.print_colored("OS is Windows. Environment dependencies installations skipped...", colourprint.ORANGE)

    dependencies = ["tkinter", "serial", "serial.tools.list_ports"]
    exceptions = {"serial.tools.list_ports": "pyserial"}
    
    for item in dependencies:
        initialization.packageCheck.checkPackage(item, exceptions)
    return result