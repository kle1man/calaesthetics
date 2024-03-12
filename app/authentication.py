# authentication.py: login system functions

# imports operating system functions for file paths
import os

# reads the contents of "credentials.txt" and returns a dictionary containing username-password pairs
def readcredentials():
    credentials = {}
    # gets the directory name of this file, and sets a filepath to the "credentials.txt" file in data/
    sourcefile = os.path.join(os.path.dirname(__file__), '../data/credentials.txt')
    # opens the "credentials.txt" file in read mode
    with open(sourcefile, 'r') as file:
        # iterates over every line in the file
        for line in file:
            # splits each line at the colon and saves the strings to username and password variables
            username, password = line.strip().split(':')
            # adds the username-password pair to the credentials dictionary
            credentials[username] = password
        # returns the credentials dictionary
        return credentials

# takes a username and password as input and authenticates them against the "credentials.txt" file
def authenticate(username, password):
    # calls the readcredentials() function to get the dictionary of username-password pairs
    credentials = readcredentials()
    # checks if the username passed in as a parameter exists in the credentials dictionary, and if the paired password matches the password parameter
    if username in credentials and credentials[username] == password:
        return True
    # if an exact match isn't found..
    else:
        return False
