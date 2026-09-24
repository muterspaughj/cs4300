# Import runpy so we can run task5.py and access its contents
import runpy


# Run task5.py and store its contents
task5 = runpy.run_path("src/task5.py")


# Test that the books list contains four books
def test_books_list():

    # Verify that there are four books in the list
    assert len(task5["books"]) == 4


# Test the first three books
def test_first_three_books():

    # Verify that list slicing returns the correct first three books
    assert task5["first_three_books"] == [
        ["The Lord of the Rings", "J.R.R. Tolkien"],
        ["The Hobbit", "J.R.R. Tolkien"],
        ["Harry Potter", "J.K. Rowling"]
    ]


# Test that the student database is a dictionary
def test_student_dictionary():

    # Verify that students is a dictionary
    assert isinstance(task5["students"], dict)


# Test a student ID
def test_student_id():

    # Verify that Jack has the correct student ID
    assert task5["students"]["Jack"] == 1001