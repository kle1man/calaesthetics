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

# takes a username and password as input and creates a new account by appending the credentials to the "credentials.txt" file
def createaccount(username, password):
    # gets the directory name of this file, and sets a filepath to the "credentials.txt" file in data/
    sourcefile = os.path.join(os.path.dirname(__file__), '../data/credentials.txt')
    # opens the "credentials.txt" file in append mode
    with open(sourcefile, 'a') as file:
        # writes the username and password inputted as parameters to the file, seperated by a colon
        file.write(f"{username}:{password}\n")

def deleteaccount(username):
    # gets the directory name of this file, and sets a filepath to the "credentials.txt" file in data/
    sourcefile = os.path.join(os.path.dirname(__file__), '../data/credentials.txt')
    # reads the contents of the "credentials.txt" file and stores them in a list
    with open(sourcefile, 'r') as file:
        lines = file.readlines()
    # opens the "credentials.txt" file in write mode
    with open(sourcefile, 'w') as file:
        # iterates over every line in the file
        for line in lines:
            # splits each line at the colon and saves the strings to username and password variables
            storedusername, _ = line.strip().split(':')
            # if the stored username does not match the username to be deleted, writes the line back to the file
            if storedusername != username:
                file.write(line)
