from random import randint
"""Word Finder: finds random words from a dictionary."""
word_dictionary = open("words.txt", "r")

class WordFinder:
    """Program to find random words from a dictionary"""
    def __init__(self, source):
        """reads the source, makes a list out of the source and reports the word length """
        self.dict_file = list(source)
        print(f"{len(self.dict_file)} words read")

    def random(self):
        """returns a random word from the dictionary"""
        return self.dict_file[randint(0, len(self.dict_file))]

wf = WordFinder(word_dictionary)
print(wf.random())



#=========================================================================================================================================================================================
#
"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder_2:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder_2("own_words")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

wf2 = WordFinder_2("words.txt")
print(wf2.random())

wf3 = WordFinder_2("/usr/share/dict/words")
print(wf3.random())
