'''
This is program is create to translate the words .
Program contains the tabluate function to improve the visibility fro the user and give attarct output . 
For translating the words we import googletrans in-built function . 
'''

import os
from tabluate import tabulate           #First need to install library
from googletrans import Translator

class simple_translator(object):
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.translator = Translator()
    def translation(self):
        translation = self.translator.translate(self.word, dest = self.language)
        data = [["Orignal Sentence:", "Translated Sentence:"],
                [self.word, str(translation.text)]]
        return tabulate(data, headers = "firstrow", tablefmt = "fancy_grid")
    def __str__(self):
        return self.translation()

if __name__ == '__main__':
    sentence = input("Enter string to translate >>")
    os.system("cls")
    print(simple_translator(sentence,"en"))