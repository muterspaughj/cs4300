# Create a function that counts the words in a text file
def count_words(filename):

    # Open the file in read mode
    with open(filename, "r") as file:

        # Read all of the text from the file
        text = file.read()

    # Split the text into individual words
    words = text.split()

    # Return the number of words
    return len(words)


# Count the words in task6_read_me.txt
word_count = count_words("task6_read_me.txt")

# Print the total number of words
print(word_count)