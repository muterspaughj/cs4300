# Import the numpy package
import numpy as np


# Create a function that calculates the average of a list of numbers
def calculate_average(numbers):

    # Use numpy to calculate and return the average
    return np.mean(numbers)


# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the average
average = calculate_average(numbers)

# Print the average
print(average)