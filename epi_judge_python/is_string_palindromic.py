from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # TODO - you fill in here.
    res = (s[i]==s[~i] for i in range(len(s)))
    return all(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
