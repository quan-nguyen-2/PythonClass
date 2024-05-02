"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, file_path):
        self.words = self.read_words(file_path)
        print(f"{len(self.words)} words read")

    def read_words(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def read_words(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]
...
