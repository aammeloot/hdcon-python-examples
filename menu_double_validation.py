# This is an example of a menu interface in Python.
# This version includes an input validation for integers.
# It also checks that a numeric value has been input before proceeding.

choice = 0 # Menu choice, integer
valid = False # Boolean type, indicates if input is valid or not

# Validate the input
while not valid:
    # First display the menu
    print("Would you like: 1 - Juice 2 - Wine 3 - Whisky")
    choice = input("What is your drink of choice?")
    # Now input is a string, let's check it contains numbers
    if choice.isnumeric():
        # If it contains numbers then convert to an integer
        choice = int(choice)
        # Now check it's in the 1 - 3 boundaries
        if choice >= 1 and choice <=3:
            # Change the flag so the loop doesn't repeat itself
            valid = True
        else:
            print("Number not between 1 and 3")
    else:
        print("Not a number, buddy.")

if choice == 1:
    print("Juice")
elif choice == 2:
    print("Wine")
elif choice == 3:
    print("Whisky")
