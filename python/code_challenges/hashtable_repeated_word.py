from data_structures.hashtable import Hashtable
import string

def first_repeated_word(s):
    """Finds the first word to occur more than once in a string,
    considering punctuation as part of the word.

    Parameters:
        `s` (`str`): The input string.

    Returns:
        `str`: The first word to be repeated or None if there are no repetitions.
    """
    word_seen = set()  # A set to keep track of words that have been seen
    # Split the string into words by whitespace
    words = s.split()

    for word in words:
        # Strip punctuation from the start and end of the word
        clean_word = word.strip(string.punctuation).lower()
        if clean_word in word_seen:
            return clean_word
        word_seen.add(clean_word)
