# main.py: main application logic (mostly user inputs)

# import modules
from app import authentication

# handles the user input associated with logging into the application
def login():
    print("Please input your credentials to log in. If you don't have an account, please type \"create\".")
    # infinite loop until correct credentials are entered
    while True:
        # takes user input for their username
        username = input("Username (or \"create\"): ")
        # enters an if statement to gather information if the user chooses to create a new account
        if username == "create":
            print("\nWelcome to the account creation portal, please enter the credentials you would like to use.")
            # takes user input for their new credentials
            newusername = input("Username: ")
            newpassword = input("Password: ")
            # runs auxilliary function to create an account
            authentication.createaccount(newusername, newpassword)
            print("Successfully created a new account. You are now logged in.")
            # sends the user to the menu once they have succesfully created an account
            menu()
        # takes user input for their password
        password = input("Password: ")
        # runs inputted values through the authentication algorithm
        if authentication.authenticate(username, password):
            print("Login successful.")
            # proceeds to the navigation menu if authentication passes
            menu()
        # if authentication fails, loops again
        else:
            print("Login failed. Please try again.")

# prints a menu of options for the user to navigate through the program; takes input for said navigation
def menu():
    print("\nActions Menu\n1: Log workout\n2: Workout history")
    # infinite loop until valid navigation option is entered
    while True:
        while True:
            # try-catch statement to ensure users can only input an integer
            try:
                selection = int(input("Type the number correlated to the option you wish to select (or \"0\" to log out and exit the application): "))
                break
            except ValueError:
                print("Invalid input. Please try again.")
        # exit clause
        if selection == 0:
            print("Logged out.")
            exit()
        # enters workout logging page
        elif selection == 1:
            logworkout()
        # enters workout history page
        elif selection == 2:
            print("Workout history (to be implemented later)")
            menu() # temporary, just sends the user back to the menu if they try to access an unimplemented section
        # if the given input is invalid, loops again
        else:
            print("Invalid input. Please try again.")

# gathers user input to create a database entry logging a workout
def logworkout():
    print("\nNew Workout\nNote: throughout this page, you can enter \"exit\" to log out and exit the application without saving changes, or \"cancel\" to cancel adding this workout.")
    # takes an input of what the workout should be called, allowing for easier navigation through workout history
    name = input("What would you like this workout to be called? (i.e. \"Push Day\"):")
    # exit clause
    if name == "exit":
        print("Logged out.")
        exit()
    # cancel clause
    elif name == "cancel":
        print("Cancelled workout.")
        menu() # sends the user back to the menu if they cancel adding a workout, rather than logging them out of the whole application
    # infinite loop until correct input is given
    while True:
        # checks whether the user wants to log a duration for their workout
        durationq = input("Would you like to log a duration for this workout? (\"y\" or \"n\"):")
        # exit clause
        if durationq == "exit":
            print("Logged out.")
            exit()
        # cancel clause
        elif durationq == "cancel":
            print("Cancelled workout.")
            menu()
        elif durationq == "n":
            break
        elif durationq == "y":
            # infinite loop until correct input is given
            while True:
                # try-catch statement to ensure that an integer is inputted
                try:
                    duration = int(input("How many minutes did your workout take? (enter an integer):")) # currently unaccessed, when I finish this function I will have it save the details into a database, which will access duration
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            break
        # if the given input is invalid, loops again
        else:
            print("Invalid input. Please try again.")
    # infinite loop until valid input is given
    while True:
        action = input("Type \"+\" to add a new exercise or \"done\" to save the workout: ")
        # exit clause
        if action == "exit":
            print("Logged out.")
            exit()
        # cancel clause
        elif action == "cancel":
            print("Cancelled workout.")
            menu()
        # triggers function to save the workout when the user is done inputting information
        elif action == "done":
            print("Workout saved. (real function to be implemented later)")
            menu()
        # triggers function to add an exercise
        elif action == "+":
            print("Exercise added. (real function to be implemented later)")
            menu() # as there is no function to add exercises yet, the user is sent back to the menu for now to avoid errors
        # loops if invalid input is given
        else:
            print("Invalid input. Please try again.")
