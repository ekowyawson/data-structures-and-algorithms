from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    """
    Perform a LEFT JOIN operation between two hashmaps.

    Args:
    - synonyms (dict): A dictionary with word strings as keys and their synonyms as values.
    - antonyms (dict): A dictionary with word strings as keys and their antonyms as values.

    Returns:
    - list: A list of lists, where each sublist contains a key from the synonyms dictionary,
            its corresponding value, and the value from the antonyms dictionary if it exists,
            otherwise "NONE".
    """
    # Initialize an empty list to store the result
    result = []
    for key in synonyms:
        antonym = antonyms.get(key, "NONE")
        result.append([key, synonyms[key], antonym])
    return result
