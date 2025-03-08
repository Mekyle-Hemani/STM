import importlib.util
import sys
import subprocess
import colourprint

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