# This is an example of a menu interface in Python.
# This version includes an input validation for integers.
# This code is unsafe, i.e. if there is a text input
# it is likely to crash.

# Variable: choice, integer
choice = 0

def display_menu():
    # Print the menu
    print("Welcome to the jungle")
    print("1 - Coffee ping")
    print("2 - Tea traceroute")
    print("3 - Beer netstat")

display_menu()
choice = int(input("Please enter your choice: "))
# Conditional loop acting as value guard
while choice < 1 or choice > 3:
    print("Invalid choice, enter something between 1 and 3")
    display_menu()
    choice = int(input("Please enter your choice: "))

# Code branching the different menu actions
if choice == 1:
    print("Coffee")
elif choice == 2:
    print("Tea")
elif choice == 3:
    print("Beer")
else:   # Default for a non-recongnised value
    print("You did not enter a valid choice")

