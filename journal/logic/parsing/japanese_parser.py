import re
from sudachipy import dictionary, tokenizer

class JapaneseParser:
    def __init__(self):
        self.tokenizer_obj = dictionary.Dictionary().create()
        self.mode = tokenizer.Tokenizer.SplitMode.C

        self.latin_pattern = re.compile(r"[A-Za-z]")

    def parse(self, text: str):
        tokens = self.tokenizer_obj.tokenize(text, self.mode)

        vocab_objs = [{
            "dict_form": token.dictionary_form(),
            "reading": token.reading_form()
        }]

        for token in tokens:
            if token.part_of_speech()[0] in ("名詞", "動詞", "形容詞"):
                if not self.latin_pattern.search(token.dictionary_form()):
                    vocab_objs.append({
                        "dict_form": token.dictionary_form(),
                        "reading": token.reading_form()
                    })

        return list(set(vocab_objs))

