#Yoda Simulator

import os

# Clear the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Now, to clear the screen:
cls()

while True:

    # Prompt user input
    original_string = input("Enter your sentence: ")

    # Original string
    #original_string = "This is an example sentence"

    # Split the string into words
    words_list = original_string.split()

    # Calculate the last index (X)
    X = len(words_list) - 1

    # Reorder the words dynamically
    reordered_list = words_list[2:X+1] + words_list[:2]

    # Join the reordered words back into a string
    reordered_string = ' '.join(reordered_list)

    print("Master Yoda Says:", reordered_string)

    input('Press any Key to Continue... ')

    cls()

