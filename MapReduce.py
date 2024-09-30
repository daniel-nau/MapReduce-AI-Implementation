import re
from multiprocessing import Pool, cpu_count

# Map function: reads a chunk of text and emits (word, 1) pairs
def map_function(chunk):
    results = []
    # Find all words in the chunk, convert to lowercase
    words = re.findall(r'\w+', chunk.lower())
    # Emit (word, 1) pairs for each word
    for word in words:
        results.append((word, 1))
    return results

# Function to split the file into chunks
def split_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Parallel map function: uses multiprocessing to parallelize the map phase
def parallel_map(file_path):
    # Split the file into chunks
    chunks = list(split_file(file_path))
    # Create a pool of worker processes
    with Pool(cpu_count()) as pool:
        # Map the map_function to each chunk using the pool
        mapped_data = pool.map(map_function, chunks)
    # Flatten the list of lists into a single list of (word, 1) pairs
    flattened_data = [item for sublist in mapped_data for item in sublist]
    return flattened_data

# Word count function: orchestrates the map phase and calculates total word count
def word_count(file_path):
    # Perform the parallel map phase
    mapped_data = parallel_map(file_path)
    # Calculate the total number of words by summing the counts
    total_words = sum(count for word, count in mapped_data)
    return total_words

file_path = 'alice.txt'  # Path to your file
total_words = word_count(file_path)

# Print the total word count
print(f"Total number of words: {total_words}")