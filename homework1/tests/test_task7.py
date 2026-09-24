# Import runpy to run the script
import runpy


# Run task7.py and store its contents
task7 = runpy.run_path("src/task7.py")

# Store the calculate_average function
calculate_average = task7["calculate_average"]


# Test the average using integers
def test_integer_average():

    # Verify that the correct average is calculated
    assert calculate_average([10, 20, 30, 40, 50]) == 30


# Test the average using floats
def test_float_average():

    # Verify that the function works with floating-point numbers
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5


# Test the average with negative numbers
def test_negative_average():

    # Verify that the function works with negative numbers
    assert calculate_average([-10, 0, 10]) == 0