"""Docstring"""

from gtts import gTTS
import os

with open("test.txt", "r") as fh:
    my_text = fh.read().replace("\n", " ")

    lang = "la"

    speech = gTTS(text=my_text, lang=lang, slow=False)

    speech.save("output.mp3")

os.system("start output.mp3")
