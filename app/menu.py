# menu.py: handles the displaying and navigation of a menu interface, along with item selection

# imports operating system functions for file paths
import os

# reads the data from a file and inputs the header into an array
def readdata(filename):
    # for now, this will only be used for the exercise database, so this if statement is neccesary for expansion later on (so different filenames can be inputted)
    if filename == "exercisedb.txt":
        filename = os.path.join(os.path.dirname(__file__), '../data/exercisedb.txt')
    # initializes data array for header input
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

# displays the menu with items corresponding to a specific page number inputted as a parameter
def displaymenu(items, pagenumber):
    # sets the startindex to the item that should be the first line on the page
    startindex = (pagenumber - 1) * 10
    # sets the end index to 10 after the start index to display 10 items per page
    endindex = startindex + 10
    # iterates through the items array to display menu items
    for i, item in enumerate(items[startindex:endindex], start = startindex + 1):
        # adds increasing numbers before printing the items to make selection easier for the user
        print(f"{i}: {item}")
    # outputs the page number after the items
    print(f"Page {pagenumber}")

def navigatemenu(items):
    pagenumber = 1
    totalpages = (len(items) + 9) // 10
    while True:
        displaymenu(items, pagenumber)
        action = input("Enter action (n = next page, b = previous page, cancel = cancel menu, exit = exit program): ")
        if action == "n":
            pagenumber = min(pagenumber + 1, totalpages)
        elif action == "b":
            pagenumber = max(pagenumber - 1, 1)
        elif action == "cancel":
            return None
        elif action == "exit":
            exit()
        elif action.isdigit():
            index = int(action) - 1
            if index >= 0 and index <= len(items):
                return items[index]
        else:
            print("Invalid input. Try again.")
