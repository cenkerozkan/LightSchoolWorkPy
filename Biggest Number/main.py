# Problem:

    # Write an algorithm and draw a flowchart to input N and N numbers. Suppose that the
    # numbers are in the range -5000 <= x <= 5000. This algorithm/flowchart should find and
    # output the largest of N numbers.

# To generate random variables in an interval

import numpy as np

# Function declaration

def function():

    # Numbers

    array = (list(np.random.randint(-5000, 5000, 10000)))

    # Symbolic maximum value

    iMax = array[0]

    # For while loop

    iCounter = 1

    # To check the members

    while iCounter != len(array):

        # If the current numbers is bigger than the symbolic one

        if array[iCounter] > iMax:

            # Setting the new symbolic value

            iMax = array[iCounter]

            # For next member

            iCounter = iCounter + 1

        # If the current number is not bigger than the symbolic one

        else:

            # For next member

            iCounter = iCounter + 1

    # For you to check if you don't trust the algorithm

    print(array)

    # Output

    print(iMax)

function()