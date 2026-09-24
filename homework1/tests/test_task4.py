# Import runpy to run the script
import runpy

# Import pytest so we can test exceptions
import pytest


# Run task4.py and store its contents
task4 = runpy.run_path("src/task4.py")

# Store the calculate_discount function
calculate_discount = task4["calculate_discount"]


# Test using integers
def test_integer_discount():

    # Verify the correct price using integer values
    assert calculate_discount(100, 20) == 80


# Test using a float price
def test_float_price():

    # Verify the correct price using a float
    assert calculate_discount(50.0, 10) == 45.0


# Test using a float discount
def test_float_discount():

    # Verify the correct price using a float discount
    assert calculate_discount(100, 12.5) == 87.5


# Test an invalid data type
def test_invalid_type():

    # Verify that a string price raises a TypeError
    with pytest.raises(TypeError):
        calculate_discount("100", 20)


# Test a negative price
def test_negative_price():

    # Verify that a negative price raises a ValueError
    with pytest.raises(ValueError):
        calculate_discount(-100, 20)


# Test an invalid discount
def test_invalid_discount():

    # Verify that a discount greater than 100 raises a ValueError
    with pytest.raises(ValueError):
        calculate_discount(100, 110)