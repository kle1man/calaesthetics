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
    # finds the total numbers of pages
    totalpages = (len(items) + 9) // 10
    # outputs the page number before the items
    print(f"\nPage {pagenumber}/{totalpages}")
    # iterates through the items array to display menu items
    for i, item in enumerate(items[startindex:endindex], start = startindex + 1):
        # adds increasing numbers before printing the items to make selection easier for the user
        print(f"{i}: {item}")

# uses the displaymenu() function to create a navigatable menu with selectable items 
def navigatemenu(items):
    # defaults the page number to 1
    pagenumber = 1
    # finds the total number of pages needed to display all items inputted
    totalpages = (len(items) + 9) // 10
    # infinite loop to ensure valid input
    while True:
        # hooks the displaymenu() function to display all of the items on a specific page
        displaymenu(items, pagenumber)
        # gathers user input
        action = input("Enter action (n = next page, b = previous page, cancel = cancel menu, exit = exit program): ")
        # next page
        if action == "n":
            pagenumber = min(pagenumber + 1, totalpages)
        # previous page
        elif action == "b":
            pagenumber = max(pagenumber - 1, 1)
        # exit clause
        elif action == "exit":
            print("Logged out.")
            exit()
        # cancel clause
        elif action == "cancel":
            return None
        # if the input is a digit, returns the menu item corresponding to it
        elif action.isdigit():
            index = int(action) - 1
            if index >= 0 and index <= len(items):
                return items[index]
        # if no valid input is provided, loops again
        else:
            print("Invalid input. Try again.")
