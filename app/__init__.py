# __init__.py: initializes and imports all modules of the program; serves as the file to run the application

# import system and operating system function
import sys
import os

# gets the directory path of the "__init__.py" file
currentdirectory = os.path.dirname(os.path.realpath(__file__))

# adds the parent directory of the "__init__.py" file to the Python path
parentdirectory = os.path.abspath(os.path.join(currentdirectory, ".."))
sys.path.append(parentdirectory)

# import modules
from app import main
from app import exercises

# includes all the code from "main.py" so that it becomes executable
if __name__ == "__main__":
    # sorts exercise database at launch to ensure working menus
    exercises.sortexercises()
    # runs the initial login function from "main.py"
    main.login()
