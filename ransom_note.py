from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    for char in ransom_count:
        if ransom_count[char] > magazine_count.get(char, 0):
            return False
    return True
