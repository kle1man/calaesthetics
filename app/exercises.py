# exercises.py: auxilliary functions for the addition and modification of exercises within workouts

# imports operating system functions for file paths
import os
# imports datetime functions for file naming
import datetime

# sorts the contents of "exercisedb.txt" in order to ensure organization in menus
def sortexercises():
    # gets the directory name of this file, and sets a filepath to the "exercisedb.txt" file in data/
    sourcefile = os.path.join(os.path.dirname(__file__), '../data/exercisedb.txt')
    # opens the "exercisedb.txt" file in read mode
    with open(sourcefile, 'r') as file:
        # reads all the lines in "exercisedb.txt" and assigns them to the exercises variable
        exercises = file.readlines()
    # sorts the exercises pulled from the file and assigns them to the sortedexercises variable
    sortedexercises = sorted(exercises, key=lambda x: x.split(':')[0])
    # opens the "exercisedb.txt" file in write mode
    with open(sourcefile, 'w') as file:
        # writes all of the sorted lines back into the "exercisedb.txt" file
        file.writelines(sortedexercises)

# creates a new workout history file with the current date as the filename
def createworkoutfile(name, duration):
    # sets the directory path to the "history" folder within the "data" directory
    sourcefolder = os.path.join(os.path.dirname(__file__), '../data/history/')
    # gets the current date in the format "YYYYMMDD"
    currentdate = datetime.datetime.now().strftime("%Y%m%d")
    # creates the filepath by combining the source folder path with the current date as the filename
    filepath = os.path.join(sourcefolder, f"{currentdate}.txt")
    # opens the newly created file in write mode
    with open(filepath, 'w') as file:
        # writes the workout name to the file
        file.write(name)
        # checks if duration is not empty before writing it to the file
        if duration != "":
            file.write(f"\n{duration}")
    # returns filepath for ease of use in other functions
    return filepath

# writes the inputted date to a workout file, creating it during the process
def writeworkoutdata(filepath, data):
    # opens the file in append mode
    with open(filepath, 'a') as file:
        # writes the data passed in as a parameter to the file
        file.write(f"\n{data}")
