from journal.config import VOCAB_FILE
import json

class VocabRepository:
    def read(self):
        if not VOCAB_FILE.exists():
            return {"vocab": []}
        
        with open(VOCAB_FILE, "r+", encoding="utf-8") as file:
            return json.load(file)
    
    def add(self, word):
        VOCAB_FILE.parent.mkdir(parents=True, exist_ok=True)

        file_data = {"vocab": []}
        
        if VOCAB_FILE.exists():
            with open(VOCAB_FILE, "r", encoding="utf-8") as file:
                try:
                    loaded_data = json.load(file)

                    if isinstance(loaded_data, dict):
                        file_data = loaded_data
                except json.JSONDecodeError:
                    pass
            
        if word not in file_data["vocab"]:
            file_data["vocab"].append(word)

            with open(VOCAB_FILE, "w", encoding="utf-8") as file:
                json.dump(file_data, file, indent=4, ensure_ascii=False)        
