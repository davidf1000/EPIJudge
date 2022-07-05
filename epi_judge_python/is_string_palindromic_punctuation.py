from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    i,j = 0,len(s)-1
    while i<j:
        # left : abisin jika ada non alpha
        while i<j and not s[i].isalnum():
            i+=1
        # right : abisin jika ada non alpha
        while i<j and not s[j].isalnum():
            j-=1
        # check kanan kiri sama
        if s[i].lower() != s[j].lower():
            return False 
        # geser left kekanan, geser right kekiri
        i+=1
        j-=1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
