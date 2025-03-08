import importlib.util
import sys
import subprocess
import colourprint

def checkPip():
    try:
        subprocess.run([sys.executable, "-m", "ensurepip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        colourprint.print_colored("pip installed successfully!", colourprint.GREEN)
    except subprocess.CalledProcessError:
        colourprint.print_colored("Failed to install pip. Please install it manually.", colourprint.RED)
        exit()

def checkPackage(package):
    colourprint.print_colored(f"Verifying installation of {package}...", colourprint.YELLOW)
    if importlib.util.find_spec(package) is None:
        colourprint.print_colored(f"{package} is not installed. Do you want to install it? (y/n): ", colourprint.BLUE)
        choice = input().strip().lower()
        if choice == 'y':
            if importlib.util.find_spec("pip") is None:
                colourprint.print_colored("pip is not installed. Installing pip first...", colourprint.YELLOW)
                checkPip()
            colourprint.print_colored("pip is installed", colourprint.GREEN)

            subprocess.run([sys.executable, "-m", "pip", "install", package])
            colourprint.print_colored(f"{package} is installed", colourprint.GREEN)
        else:
            colourprint.print_colored("Quiting... ", colourprint.RED)
            exit()
    else:
        colourprint.print_colored(f"{package} is installed", colourprint.GREEN)