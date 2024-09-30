def map_function(text):
    """Map function that processes the text and returns a list of words."""
    # Split the text into words and return the list
    return text.split()

def reduce_function(word_list):
    """Reduce function that counts the total number of words."""
    # Count the total number of words in the list
    return len(word_list)

def read_file(file_path):
    """Read the entire content of the file."""
    with open(file_path, 'r') as file:
        return file.read()

def word_count(file_path):
    """Main function to perform word count using a MapReduce approach."""
    # Step 1: Read the entire file content
    text = read_file(file_path)

    # Step 2: Map phase
    words = map_function(text)

    # Step 3: Reduce phase
    total_count = reduce_function(words)

    return total_count

if __name__ == "__main__":
    file_path = 'alice.txt'  # Path to your file
    total_words = word_count(file_path)

    # Print the total word count
    print(f"Total number of words: {total_words}")
