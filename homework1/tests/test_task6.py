# Import runpy to run the script
import runpy


# Run task6.py and store its contents
task6 = runpy.run_path("src/task6.py")


# Test the word count of task6_read_me.txt
def test_word_count():

    # Count the words in the text file
    result = task6["count_words"]("task6_read_me.txt")

    # Verify that the correct number of words was counted
    assert result == task6["word_count"]