# Import runpy so we can run task2.py and access its variables
import runpy


# Run task2.py and store its variables in a dictionary
variables = runpy.run_path("src/task2.py")


# Test that age is an integer
def test_integer():

    # Verify that age has the integer data type
    assert isinstance(variables["age"], int)


# Test that height is a float
def test_float():

    # Verify that height has the float data type
    assert isinstance(variables["height"], float)


# Test that name is a string
def test_string():

    # Verify that name has the string data type
    assert isinstance(variables["name"], str)


# Test that is_student is a boolean
def test_boolean():

    # Verify that is_student has the boolean data type
    assert isinstance(variables["is_student"], bool)