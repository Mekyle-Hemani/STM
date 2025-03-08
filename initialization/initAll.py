import initialization.packageCheck
import os
if os.name != "nt":
    import initialization.environmentCheck

def checkAll():
    if os.name != "nt":
        initialization.environmentCheck.checkEnvironment()
    else:
        import colourprint
        colourprint.print_colored("OS is Windows. Environment dependencies installations skipped...", colourprint.ORANGE)

    dependencies = ["tkinter", "serial"]
    result=True
    for item in dependencies:
        initialization.packageCheck.checkPackage(item)
    return result