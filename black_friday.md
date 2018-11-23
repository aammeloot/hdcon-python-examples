# Black Friday

## Instructions
You sell 4 products of your choice with a different price each.
Offer 5 choices in the menu: choices 1 – 4 are to buy the products
Choice 5 is to quit and display the total price and a discount of 50%.
Menu must repeat itself until 5 is selected and input needs to be validated.

## Pseudo code

* Global variable: total, float, set to 0
* Global variable: choice, integer, initialise to 0
* Loop While choice is different from 5
    * Variable valid, Boolean, initialised to false
    * Loop While not valid
        * Show menu options with prices and option 5 to quit
        * Input choice
        * If choice is a numeric value then
            * Convert choice to integer
            * If choice is between 1 and 5 then
                * Set valid to true
            * End if
        * End if
    * End loop
    * If choice is equal to 1
        * Print “You chose product 1”
        * Add price 1 to total
    * Else if choice is equal to 2
        * Print “You chose product 2”
        * Add price 2 to total
    * Else if choice is equal to 3
        * Print “You chose product 3”
        * Add price 3 to total
    * Else if choice is equal to 4
        * Print “You chose product 4”
        * Add price 4 to total
    * Else if choice is equal to 5
        * Print “Your total is:”
        * Print total
        * Print “but it’s black Friday”
        * Remove 50% from total
        * Print total
    * End if
* End loop
