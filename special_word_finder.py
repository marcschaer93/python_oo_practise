"""WordFinder_2 Class Extension"""
from wordfinder import WordFinder_2

class SpecialWordFinder(WordFinder_2):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("own_words.txt")
    3 words read

    >>> swf.random() in ["banana", "apple", "blueberry"]
    True

    >>> swf.random() in ["banana", "apple", "blueberry"]
    True

    >>> swf.random() in ["banana", "apple", "blueberry"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
