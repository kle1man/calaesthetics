# exercises.py: auxilliary functions for the addition and modification of exercises within workouts

# imports operating system functions for file paths
import os

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
