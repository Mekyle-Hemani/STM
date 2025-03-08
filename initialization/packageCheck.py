import importlib.util
import sys
import subprocess
import colourprint

def checkPip():
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "python3-pip"], check=True)
        colourprint.print_colored("pip installed successfully!", colourprint.GREEN)
    except subprocess.CalledProcessError:
        colourprint.print_colored("Failed to install pip. Please install it manually.", colourprint.RED)
        exit()

def checkPackage(package):
    colourprint.print_colored(f"Verifying installation of {package}...", colourprint.YELLOW)

    if package == "tkinter":
        try:
            subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
            colourprint.print_colored("tkinter installed successfully!", colourprint.GREEN)
        except subprocess.CalledProcessError:
            colourprint.print_colored("Failed to install tkinter. Please install it manually.", colourprint.RED)
        return

    if importlib.util.find_spec(package) is None:
        colourprint.print_colored(f"{package} is not installed. Do you want to install it? (y/n): ", colourprint.BLUE)
        choice = input().strip().lower()
        if choice == 'y':
            if importlib.util.find_spec("pip") is None:
                colourprint.print_colored("pip is not installed. Installing pip first...", colourprint.YELLOW)
                checkPip()
            colourprint.print_colored("pip is installed", colourprint.GREEN)

            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            colourprint.print_colored(f"{package} is installed", colourprint.GREEN)
        else:
            colourprint.print_colored("Quiting... ", colourprint.RED)
            exit()
    else:
        colourprint.print_colored(f"{package} is installed", colourprint.GREEN)