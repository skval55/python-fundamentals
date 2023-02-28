"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """a class that reads the word files and has functionality
    to return a random work
    
    >>> word = WordFinder("test2.txt")
    3 words read

    >>> word.random_word() in ['cat', 'dog','mouse']
    True

    >>> word.random_word() in ['cat', 'dog','mouse']
    True

    >>> word.random_word() in ['cat', 'dog','mouse']
    True
    """
    def __init__(self, file):
        """reads the file and prints number of words"""
        file = open(file)
        self.words = self.make_list(file)
        print(f'{len(self.words)} words read')

    def make_list(self, file):
        """ makes a list of the words in the file"""
        return [w.strip() for w in file]

     

    def random_word(self):
        """ returns a random word from the list of words"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """a class that will make parse a file and give only words that arent commented out back

    >>> spw = SpecialWordFinder("test.txt")
    3 words read

    >>> spw.words == ['cat', 'dog', 'rat']
    True

    """      
    def make_list(self, file):
        """Parse file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in file if w.strip() and not w.startswith("#")]