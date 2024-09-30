from collections import defaultdict
import re
from multiprocessing import Pool, cpu_count

# Map function: reads file and emits (word, 1) pairs
def map_function(file_path):
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\w+', line.lower())
            for word in words:
                results.append((word, 1))
    return results

# Parallel map function
def parallel_map(file_path):
    with Pool(cpu_count()) as pool:
        mapped_data = pool.map(map_function, [file_path])
    # Flatten the list of lists
    flattened_data = [item for sublist in mapped_data for item in sublist]
    return flattened_data

# Word count function: orchestrates the map phase and calculates total word count
def word_count(file_path):
    mapped_data = parallel_map(file_path)
    total_words = sum(count for word, count in mapped_data)
    return total_words

file_path = 'alice.txt'  # Path to your file
total_words = word_count(file_path)

# Print the total word count
print(f"Total number of words: {total_words}")