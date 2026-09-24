# Import runpy so we can run task3.py and access its contents
import runpy


# Run task3.py and store its contents
task3 = runpy.run_path("src/task3.py")


# Test the positive number condition
def test_positive():

    # Verify that a positive number returns positive
    assert task3["check_number"](10) == "positive"


# Test the negative number condition
def test_negative():

    # Verify that a negative number returns negative
    assert task3["check_number"](-10) == "negative"


# Test the zero condition
def test_zero():

    # Verify that zero returns zero
    assert task3["check_number"](0) == "zero"


# Test the first 10 prime numbers
def test_prime_numbers():

    # Verify that the correct first 10 prime numbers were found
    assert task3["prime_numbers"] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# Test the sum from 1 to 100
def test_total():

    # Verify that the sum from 1 to 100 is 5050
    assert task3["total"] == 5050