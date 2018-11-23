# Black Friday

total = 0.0
choice = 0

while choice != 5:
    valid = False
    while not valid:
        print("Here are the options: ")
        print("1 - Hard drive - £50.99")
        print("2 - Box of Maltesers - £2.99")
        print("3 - Book about something - £7.50")
        print("4 - Keyboard - £15")
        print("5 - Quit and show total")

        choice = input("What is your pick?")

        if choice.isnumeric():
            choice = int(choice)
            if choice >=1 and choice <=5:
                valid = True

    if choice == 1:
        print("You just bought a hard drive for £50.99")
        total += 50.99
    if choice == 2:
        print("You just bought a box of maltesers for £2.99")
        total += 2.99
    if choice == 3:
        print("You just bought a book about something for £7.50")
        total += 7.5
    if choice == 4:
        print("You just bought a keyboard for £15")
        total += 15.0
    if choice == 5:
        print("Your total is £" + str(total))
        total /= 2.0
        print("With a discount for Black Friday: £" + str(total))

