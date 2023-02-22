def print_upper_words(words):
    """Prints words in upper case letters

    -words: list of different words"""
    for word in words:
        print(word.upper())

# print_upper_words(['cat', 'dog','mouse','rat'])

def print_e_upper_words(words):
    """Prints words that start with "e" in upper case letters

    -words: list of different words"""
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

# print_e_upper_words(['cat', 'dog','mouse','rat', 'elephant','ego', 'EAt'])


def print_upper_words_with_letter(words, letters):
    """Prints words that start with "e" in upper case letters

    -words: list of different words"""
    for word in words:
        for letter in letters:
            if word[0] == letter or word[0] == letter.upper():
                print(word.upper())

print_upper_words_with_letter(['cat', 'dog','Mouse','rat', 'elephant','ego', 'EAt'], {'m', 'c'})
