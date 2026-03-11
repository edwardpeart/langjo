from config import VOCAB_FILE
import json

class VocabRepository:
    def read(self):
        with open(VOCAB_FILE, "r+", encoding="utf-8") as file:
            return json.load(file)
    
    def add(self, word):
        with open(VOCAB_FILE, "r+", encoding="utf-8") as file:
            file_data = json.load(file)
            if word not in file_data["vocab"]:
                file_data["vocab"].append(word)
                
            file.seek(0)
            json.dump(file_data, file, indent=4, ensure_ascii=False)
            file.truncate()

        
