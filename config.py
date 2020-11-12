from io import open
from importlib import import_module
from app.Exceptions.exceptions import *

def config():
    try:
        config = open("CONFIG.txt", "r+")
        lines = config.readlines()
        config.seek(0)
        all_modules_installed = True
        for line in lines:
            if line[0] != "#":
                try:
                    new_line = check_dependency(line)
                except ModuleNotInstalledError as e:
                    print(str(e.args[0]) + " is not installed. Please install and try again.")
                    new_line = str(e.args[0]) + "=FALSE"
                    all_modules_installed = False
                config.write(new_line + "\n")
            else:
                config.write(line)
        return all_modules_installed
    except IOError:
        raise ConfigFileMissingError("No Config File")

# TODO Ask user if they would like to install the package with pip
def check_dependency(config_line):
    components = config_line.split("=")
    try:
        import_module(components[0])
        return components[0] + "=" + "TRUE"
    except ImportError:
        raise ModuleNotInstalledError(components[0])


    

