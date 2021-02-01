# Importing the library we need
from deep_translator import GoogleTranslator

# Opening the text file that contains the kanji we want to translate in read-only mode
with open("words.txt", "r", encoding="utf8") as f:
    for word in f:
        try:
            # For this specific case we only want the first character
            token = word[:1] if len(word) != 1 else word
            # We translate token plus an empty space because the translator needs at least two letters
            print(token, " --> " , GoogleTranslator(source='auto', target='en').translate(token + " "))
        except Exception as e:
            print(e)