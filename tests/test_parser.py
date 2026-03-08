from  journal.logic.parsing.japanese_parser import JapaneseParser

parser = JapaneseParser()

text = "今日は仕事のあとで日本語を勉強しました。それからYouTubeで日本のニュースを見ました。"

print(parser.parse(text))