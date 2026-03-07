from .parsing.japanese_parser import JapaneseParser
from ..repository.vocab_repository import VocabRepository

class VocabLogic:
    def __init__(self):
        self.parser = JapaneseParser()
        self.repo = VocabRepository()
    
    def add_from_text(self, text: str):
        words = self.parser.parse(text)

        for word in words:
            self.repo.add(word)

    def count_words(self):
        data = self.repo.read()
        return len(data["vocab"])
        



