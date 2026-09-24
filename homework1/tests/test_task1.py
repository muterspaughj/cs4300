# Import runpy to run the task1.py script
import runpy


# Test that task1.py prints "Hello, World!"
def test_hello_world(capsys):

    # Run the task1.py script
    runpy.run_path("src/task1.py")

    # Capture everything printed to standard output
    captured = capsys.readouterr()

    # Verify that the output is exactly "Hello, World!" followed by a newline
    assert captured.out == "Hello, World!\n"