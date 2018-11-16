# This is an example of a menu interface in Python.
# This version includes an input validation for integers.
# This code is Typesafe, i.e. it handles exceptions when the
# wrong type is encountered.

# Variable: choice, integer
choice = 0
# Flag: input is valid, boolean, default value is False
input_valid = False

# We are sure to enter the loop because we explicitly
# set up the flag as False on line 9
while not input_valid:
    # Print the menu
    print("Welcome to the jungle")
    print("1 - Coffee ping")
    print("2 - Tea traceroute")
    print("3 - Beer netstat")
    
    try:
        # Read the input and convert to an integer
        choice = int(input("Please enter your choice: "))
        # Set up the flag if the choice is in the boundaries
        if choice >=1 and choice <=3:
            # By setting the flag to True we stop the loop
            input_valid = True
        else:
            print("Invalid choice, enter something between 1 and 3")
    except:
        ValueError
        print("Please ensure you enter a number.")


# Code branching the different menu actions
if choice == 1:
    print("Coffee")
elif choice == 2:
    print("Tea")
elif choice == 3:
    print("Beer")
else:   # Default for a non-recongnised value
    print("You did not enter a valid choice")

