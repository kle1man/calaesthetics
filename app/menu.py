# menu.py: handles the displaying and navigation of a menu interface, along with item selection

# imports operating system functions for file paths
import os

# reads the data from a file and inputs the header into an array
def readdata(filename):
    # for now, this will only be used for the exercise database, so this if statement is neccesary for expansion later on (so different filenames can be inputted)
    if filename == "exercisedb.txt":
        filename = os.path.join(os.path.dirname(__file__), '../data/exercisedb.txt')
    data = []
    # opens the inputted file in read mode
    with open(filename, 'r') as file:
        # iterates through every line in the file
        for line in file:
            # splits the line so that the header can be separated
            linesplit = line.strip().split(':')
            # assigns the separated header to a variable
            header = linesplit[0]
            # appends the header to the data array
            data.append(header)
    # returns the array of headers
    return data
