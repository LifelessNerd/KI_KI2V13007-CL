# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:16:02 2022

@author: lucmi
"""
import pickle
import re
import nltk
from nltk.chunk.util import conlltags2tree, tree2conlltags
from nltk.corpus import conll2002 as conll
import features
from custom_chunker import ConsecutiveNPChunker
def evaluatemodel(file):
    title = re.split(r"@", file)
    if title[1] == "whole":
        title[1] = len(conll.chunked_sents("ned.train"))
    pickledfile = pickle.load(open(file, "rb"))
    testsent = conll.chunked_sents("ned.testa")
    print("Model used feature:", title[0], "using the first", title[1], "sentences from ned_train")
    print(pickledfile.evaluate(testsent))


if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    print(file)
    evaluatemodel(file)