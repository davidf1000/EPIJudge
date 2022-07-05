from typing import List

from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    # count word freq
    # count size of word (assume it all same)
    # create a function that return true if combination of words in s 
    if not words or not s:
        return []
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word,0) +1
    word_size = len(words[0])
    def is_composed(idx: int)->bool:
        # create hashmap to count occurence, loop, check if occurence of words > word_freq
        word_occurence = {}
        for i in range(idx,idx + word_size*len(words),word_size):
            word = s[i:i+word_size]
            if word not in word_freq:
                return False
            word_occurence[word] = word_occurence.get(word,0) + 1
            if word_occurence[word] > word_freq[word]:
                return False
        return True
    return [i for i in range(len(s)-word_size*len(words)+1) if is_composed(i)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
