
from googletrans import Translator

def translate(text):
    translator = Translator()
    result = translator.translate(text, dest="es")  # Translate to Spanish
    return result.text
                             