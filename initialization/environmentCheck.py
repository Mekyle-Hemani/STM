import subprocess, sys
import colourprint

def checkEnvironment():
    libraries = ["xorg", "openbox"]
    
    for lib in libraries:
        try:
            subprocess.check_call(['dpkg-query', '-l', lib], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            colourprint.print_colored(f"{lib} is already installed.", colourprint.BLUE)
        except subprocess.CalledProcessError:
            colourprint.print_colored(f"{lib} is not installed. Installing...", colourprint.BLUE)
            try:
                subprocess.check_call(['sudo', 'apt', 'install', '-y', lib])
                colourprint.print_colored(f"{lib} has been installed.", colourprint.BLUE)
            except subprocess.CalledProcessError as e:
                colourprint.print_colored(f"Failed to install {lib}: {e}", colourprint.RED)
                sys.exit(1)