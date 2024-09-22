__author__ = "Jeremy Nelson"

import datetime
import hashlib
import json
import os
import pathlib
import random

from dataclasses import dataclass, field
from typing import Union

from js import console, navigator
from pyscript import document

YIN, YANG = 2,3

PATTERNS = dict()

HEXAGRAM_PATH = pathlib.Path("./intro-pre-conference/iching.json")

with HEXAGRAM_PATH.open() as fo:
    PATTERNS = json.load(fo)

@dataclass
class Trigram:
    """Creates a Trigram made up of three lines"""
    lines: list = field(default_factory=list)

    def generate(self):
        if len(self.lines) > 0:
            return
        for line in range(0,3):
            line_total = 0
            for value in range(0,3):
                line_total += random.randint(YIN, YANG)
            self.lines.append(line_total)

@dataclass
class Hexagram:
    lines: list = field(default_factory=list)
    name: Union[str, None] = None
    above_trigram: Union[Trigram, None] = None
    below_trigram: Union[Trigram, None] = None
    pattern: str = str()
    transformed_hexagram = None
    
    def _generate_transformed_hexagram(self):
        """Checks and generates transformed hexagram if any lines are 6 or 9"""
        if self.lines.count(6) > 0 or self.lines.count(9) > 0:
            self.transformed_hexagram = Hexagram(
                above_trigram = Trigram(lines=[self._normalize(x) for x in self.above_trigram.lines]),
                below_trigram = Trigram(lines=[self._normalize(x) for x in self.below_trigram.lines])
            )
            self.transformed_hexagram._save()

    def _normalize(self, value):
        match value:
            case 6:
                output = 7
            case 9:
                output = 8
            case _:
                output = value
        return output

      
    def _save(self):
        self.pattern = ""
        for i in self.lines:
            if i%2:
                self.pattern += "0"
                continue
            self.pattern += "1"
 

    def generate(self):
        if len(self.lines) < 1:
            self.above_trigram = Trigram()
            self.below_trigram = Trigram()
            self.above_trigram.generate()
            self.below_trigram.generate()
            self.lines = self.below_trigram.lines + self.above_trigram.lines
        self._generate_transformed_hexagram()
        self._save()
     

@dataclass
class Oracle:
    question: str
    hexagram: Hexagram = field(default_factory=Hexagram)
    consulted_on: datetime.datetime = datetime.datetime.now(datetime.UTC)

def tell_fortune(event):
    question = document.querySelector("#question")
    fortune_elem = document.querySelector("#fortune")
    fortune_elem.classList.remove("invisible")
    hexagram_char = document.querySelector("#hexagram-character")
    hexagram_name = document.querySelector("#hexagram-name")
    small_question = document.querySelector("#question-repeat")
    oracle = Oracle(question=question.value)
    oracle.hexagram.generate()
    fortune = PATTERNS[oracle.hexagram.pattern]
    hexagram_char.innerHTML = fortune["character"]
    hexagram_name.innerHTML = fortune["name"]
    small_question.innerHTML = oracle.question

def copy_fortune(event):
    hexagram_char = document.querySelector("#hexagram-character")
    hexagram_name = document.querySelector("#hexagram-name")
    small_question = document.querySelector("#question-repeat")
    copied_text = f"{small_question.textContent} - the Iching {hexagram_char.textContent} {hexagram_name.textContent}"
    navigator.clipboard.writeText(copied_text)
 
