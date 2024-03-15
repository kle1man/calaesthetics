# main.py: main application logic (mostly user inputs)

# import modules
import app.authentication
import app.exercises
import app.menu

# handles the user input associated with logging into the application
def login():
    print("\nInput your credentials to log in. (Alternately: \"create\" to create an account, \"delete\" to delete an account, or \"exit\" to exit the program).")
    # infinite loop until correct credentials are entered
    while True:
        # takes user input for their username
        username = input("Username (or \"create\"/\"delete\"): ")
        # exit clause
        if username == "exit":
            exit()
        # enters an if statement to gather information if the user chooses to create a new account
        elif username == "create":
            print("\nWelcome to the account creation portal, enter the credentials you would like to use.")
            # takes user input for their new credentials
            newusername = input("Username: ")
            newpassword = input("Password: ")
            # runs auxilliary function to create the account
            app.authentication.createaccount(newusername, newpassword)
            print("Successfully created a new account. You are now logged in.")
            # sends the user to the menu once they have succesfully created an account
            menu()
        # enters an if statement to gather information if the user chooses to delete an account
        elif username == "delete":
            # infinite loop until correct credentials are entered or "cancel" command is inputted
            while True:
                print("\nInput the credentials of the account you would like to delete, or \"cancel\" to cancel this action.")
                # gathers username or "cancel" input
                delusername = input("Username: ")
                # cancel clause
                if delusername == "cancel":
                    print("Cancelled deletion of account.")
                    # sends user back to login screen if they cancel
                    login()
                # gathers password or "cancel" input
                delpassword = input("Password: ")
                # cancel clause
                if delpassword == "cancel":
                        print("Cancelled deletion of account.")
                        # sends user back to login scren if they cancel
                        login()
                # checks that inputted credentials are valid
                if app.authentication.authenticate(delusername, delpassword):
                    # infinite loop until the user confirms whether they want to delete the account
                    while True:
                        confirmation = input("Are you sure you want to delete this account? (\"y\" or \"n\"): ")
                        # if yes...
                        if confirmation == "y":
                            # runs auxilliary function to delete the account
                            app.authentication.deleteaccount(delusername)
                            print("Account successfully deleted.")
                            # sends the user back to the login screen after deleting the account
                            login()
                        # if no...
                        elif confirmation == "n":
                            print("Account deletion cancelled.")
                            # sends the user back to the login screen since they cancelled
                            login()
                        # if input isn't one of the two answer choices, loops again
                        else:
                            print("Invalid input. Try again.")
                # if the credentials entered don't exist...
                else:
                    print("The credentials you entered don't correspond to an account in the system. Try again.")
        # takes user input for their password
        password = input("Password: ")
        # exit clause
        if password == "exit":
            exit()
        # runs inputted values through the authentication algorithm
        if app.authentication.authenticate(username, password):
            print("Login successful.")
            # proceeds to the navigation menu if authentication passes
            menu()
        # if authentication fails, loops again
        else:
            print("Login failed. Try again.")

# prints a menu of options for the user to navigate through the program; takes input for said navigation
def menu():
    print("\nActions Menu\n1: Log workout\n2: Workout history")
    # infinite loop until valid navigation option is entered
    while True:
        selection = input("Type the number correlated to the option you wish to select (or \"exit\" to log out and exit the application): ")
        # exit clause
        if selection == "exit":
            print("Logged out.")
            exit()
        elif selection.isdigit():
            # enters workout logging page
            if int(selection) == 1:
                logworkout()
            # enters workout history page
            elif int(selection) == 2:
                print("Workout history (to be implemented later)")
                menu() # temporary, just sends the user back to the menu if they try to access an unimplemented section
            # if the number inputted is out of range, loops again
            else:
                print("Invalid input. Try again.")
        # if the given input is invalid, loops again
        else:
            print("Invalid input. Try again.")

# gathers user input to create a database entry logging a workout
def logworkout():
    print("\nNew Workout\nNote: throughout this page, you can enter \"exit\" to log out and exit the application without saving changes, or \"cancel\" to cancel adding this workout.")
    # takes an input of what the workout should be called, allowing for easier navigation through workout history
    name = input("What would you like this workout to be called? (i.e. \"Push Day\"): ")
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
        durationq = input("Would you like to log a duration for this workout? (\"y\" or \"n\"): ")
        # exit clause
        if durationq == "exit":
            print("Logged out.")
            exit()
        # cancel clause
        elif durationq == "cancel":
            print("Cancelled workout.")
            menu()
        elif durationq == "n":
            duration = ""
            break
        elif durationq == "y":
            # infinite loop until correct input is given
            while True:
                # try-catch statement to ensure that an integer is inputted
                try:
                    duration = int(input("How many minutes did your workout take? (enter an integer): ")) # currently unaccessed, when I finish this function I will have it save the details into a database, which will access duration
                    break
                except ValueError:
                    print("Invalid input. Try again.")
            break
        # if the given input is invalid, loops again
        else:
            print("Invalid input. Try again.")
    # creates file for the workout data to be put into
    filepath = app.exercises.createworkoutfile(name, duration)
    # infinite loop until valid input is given
    while True:
        action = input("\nType \"+\" to add a new exercise or \"done\" to save the workout: ")
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
            print("Workout saved.")
            menu()
        # triggers function to add an exercise
        elif action == "+":
            # pulls the list of exercise names for use in the selection menu
            exercises = app.menu.readdata("exercisedb.txt")
            # triggers the selection menu to open and binds the selection to a variable
            selection = app.menu.navigatemenu(exercises, "Exercise Menu")
            # initializes data string to be written into the file after gathering user input
            data = f"{selection}:"
            print(f"\nExercise: {selection}")
            # infinite loop until correct input is given 
            while True:
                # try-catch statement to ensure an integer is inputted
                try:
                    sets = int(input("Number of sets: "))
                    break
                except ValueError:
                    print("Invalid input. enter a Number.")
            # iterates through the number of sets the user completed to gather information on the reps, weight, and rpe
            for i in range (1, sets + 1):
                print(f"\nSet {i}/{sets}")
                # infinite loop until correct input is given
                while True:
                    # try-catch statement to ensure an integer is inputted
                    try:
                        # sets the number of reps the user inputted to a variable
                        reps = int(input("Number of reps: "))
                        break
                    except ValueError:
                        print("Invalid input. Enter a number.")
                # infinite loop until correct input is given
                while True:
                    # try-catch statement to ensure a float is inputted
                    try:
                        # sets the weight the user inputted to a variable
                        weight = float(input("Weight (x2 if it's per arm): ")) # float variable type used in case the user did a decimal weight
                        break
                    except ValueError:
                        print("Invalid input. Enter a number.")
                # infinite loop until correct input is given
                while True:
                    # try-catch statement to ensure an integer is inputted
                    try:
                        # sets the rpe the user inputted to a variable
                        rpe = int(input("RPE (1 being warmup, 10 being failure): "))
                        # ensures the inputted rpe is within range
                        if 1 <= rpe <= 10:
                            # breaks out of the while loop once all the information is properly collected
                            break
                        else:
                            print("Invalid input. Enter a number between 1 and 10.")
                    except ValueError:
                        print("Invalid input. Enter a number.")
                # appends the collected data to the variable to be written in a file later
                if i != sets:
                    data += f"{reps},{weight},{rpe};"
                # if it's the last bit of data, appends without a semi-colon at the end to not confuse the splitting algorithm later
                else:
                    data += f"{reps},{weight},{rpe}"
            # writes the collected data into the workout file
            app.exercises.writeworkoutdata(filepath, data)
        # loops if invalid input is given
        else:
            print("Invalid input. Try again.")
