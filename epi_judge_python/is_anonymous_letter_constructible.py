from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    hash_magazine = {}
    # counting occurence of each word in magazine 
    for char in magazine_text: 
        hash_magazine[char] = (hash_magazine[char] if char in hash_magazine else 0) + 1
    # removing occurence of each word in magazine from letter_text
    for char in letter_text:
        if char not in hash_magazine or hash_magazine[char]<1: return False
        else: hash_magazine[char] -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
