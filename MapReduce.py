from collections import defaultdict
import re

def map_function(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\w+', line.lower())
            for word in words:
                yield (word, 1)

def shuffle_and_sort(mapped_data):
    shuffled_data = defaultdict(list)
    for key, value in mapped_data:
        shuffled_data[key].append(value)
    return shuffled_data

def reduce_function(shuffled_data):
    reduced_data = {}
    for key, values in shuffled_data.items():
        reduced_data[key] = sum(values)
    return reduced_data

def word_count(file_path):
    mapped_data = map_function(file_path)
    shuffled_data = shuffle_and_sort(mapped_data)
    reduced_data = reduce_function(shuffled_data)
    return reduced_data

file_path = 'alice.txt'  # Path to your file
word_counts = word_count(file_path)

# Calculate the total number of words
total_words = sum(word_counts.values())

# Print the total word count
print(f"Total number of words: {total_words}")