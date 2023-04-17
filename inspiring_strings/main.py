def longest_word(string_of_words):
    return [s for s in string_of_words.split() if len(s) == len(max(string_of_words.split(), key=len))][-1]
