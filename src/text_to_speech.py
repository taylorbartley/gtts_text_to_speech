#!/usr/bin/env python3
"""Docstring"""

import os

from gtts import gTTS


def main():
    """Start"""
    with open("input/test.txt", "r") as file_handle:
        file_out = "output/output.mp3"
        my_text = file_handle.read().replace("\n", " ")

        lang = "la"

        speech = gTTS(text=my_text, lang=lang, slow=False)

        speech.save(file_out)

    os.system("start output.mp3")


if __name__ == "__main__":
    main()
