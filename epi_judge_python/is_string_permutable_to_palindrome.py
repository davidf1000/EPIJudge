from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # use hashmap, loop for every char add to hashmap with counter
    # can form palindrome if and only if every value is even except for 0 or 1 odd 
    hashmap = {}
    for c in s:
        hashmap[c] = (hashmap[c] if c in hashmap else 0) + 1
    count_odd = len([x for x in hashmap.values() if x%2!=0])
    return count_odd<=1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
