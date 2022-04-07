#!/usr/bin/env python3
# alice.py
# analyze Alice in Wonderland text
# from Matthes Crash Course 2e

FILENAME= 'alice.txt'

try:
    with open(FILENAME, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {FILENAME} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {FILENAME} has about {num_words} words.")
