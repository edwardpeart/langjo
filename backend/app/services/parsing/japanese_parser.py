import re

from sudachipy import dictionary, tokenizer


class JapaneseParser:
    def __init__(self):
        self.tokenizer_obj = dictionary.Dictionary().create()
        self.mode = tokenizer.Tokenizer.SplitMode.C
        self.latin_pattern = re.compile(r"[A-Za-z]")

    def parse(self, text: str):
        tokens = self.tokenizer_obj.tokenize(text, self.mode)
        vocab_objs = []

        for token in tokens:
            if token.part_of_speech()[0] in ("名詞", "動詞", "形容詞"):
                dict_form = token.dictionary_form()
                if not self.latin_pattern.search(dict_form):
                    vocab_objs.append({
                        "dict_form": dict_form,
                        "reading": token.reading_form(),
                    })

        unique_words = []
        seen = set()
        for item in vocab_objs:
            key = (item["dict_form"], item["reading"])
            if key not in seen:
                seen.add(key)
                unique_words.append(item)

        return unique_words

