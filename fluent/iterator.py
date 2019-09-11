from typing import *
from collections import abc
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    text: str

    def __init__(self, text: str):
        self.text = text

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


s = Sentence('"The time has come," the Walrus said,')
for word in s:
    print(word)
