import random

def load_words(filepath):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    level1 = []
    level2 = []
    level3 = []

    # Read the words from the file
    with open(filepath) as file:
        content = file.read()
        content = content.lower()
        words = content.split()

    # Populate lists based on word lengths
    for word in words:
        word_length = len(word)
        if word_length <= 4:
            level1.append(word)
        elif 4 < word_length <= 6:
            level2.append(word)
        else:
            level3.append(word)
    return level1,level2,level3



def get_word(words_list):
    """
    Returns a random word from the word list
    """
    # Returns a random number from the list
    return random.choice(words_list)
