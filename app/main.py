# main.py: main application logic (mostly user inputs)

# import modules
from app import authentication

# handles the user input associated with logging into the application
def login():
    print("Please input your credentials to log in.")
    # infinite loop until correct credentials are entered
    while True:
        # takes user input for their username and password
        username = input("Username: ")
        password = input("Password: ")
        # runs inputted values through the authentication algorithm
        if authentication.authenticate(username, password):
            print("Login successful.")
            # exits the loop if authentication passes
            break
        # if authentication fails, loops again
        else:
            print("Login failed. Please try again.")
