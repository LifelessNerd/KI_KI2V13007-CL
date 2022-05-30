# import nltk.corpus
# from nltk.book import *
import re
from nltk.corpus import gutenberg

words = gutenberg.words("carroll-alice.txt")
words = [w.lower() for w in words if re.search(r'\w', w)]


woordenlijst = {}

for index, word in enumerate(words):
        if word.lower() == 'alice':
            nextword = words[index + 1]
            if nextword in woordenlijst.keys():
                woordenlijst[nextword] = woordenlijst[nextword] + 1
            else:
                woordenlijst[nextword] = 1

woordenlijst = dict(sorted(woordenlijst.items(), key=lambda item: item[1], reverse=True))



if __name__ == "__main__":
    for index, woord in enumerate(woordenlijst):
        if index < 5:
            print(woord, woordenlijst[woord])
