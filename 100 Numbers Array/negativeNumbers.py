# Problem:

    # Write an algorithm and draw a flowchart that will input 100 numbers
    # and will find the number of positive numbers.

# Note:

    # Normally our curriculum includes only C programming language but since we
    # haven't made it to the arrays in C yet, I wrote this algorithm in Python
    # programming language

# To generate random numbers with an interval

import numpy as np

# First, create a function

def function():

    # To generate 100 random numbers (both positive and negative included)

    array = (list(np.random.randint(-100,100,100)))

    # Array to swap the negative numbers from first array

    swapArray = []

    # To control the loop and to check the each member of the main array

    iCounter = 0

    # To count how many negative numbers found

    iNegativeCounter = 0

    # To check every integer

    while iCounter != 100:

        # If the current number is negative

        if array[iCounter] < 0:

            # Current status

            print("Negative")

            # To update the negative number index

            iNegativeCounter = iNegativeCounter + 1

            # Append the current number to the swap array

            swapArray.append(array[iCounter])

            # Increase the counter to check next members

            iCounter = iCounter + 1

        # Else the current numbers is positive

        else:

            # Current status

            print("Positive")

            # Increase the counter to check next members

            iCounter = iCounter + 1

    # Exhibit the original list

    print(array)

    # Exhibit the swap list

    print(swapArray)

    # Exhibit how many negative numbers found

    print(iNegativeCounter)

function()