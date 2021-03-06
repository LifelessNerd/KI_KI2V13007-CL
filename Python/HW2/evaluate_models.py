# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:16:02 2022

@author: lucmi
"""
import pickle
import re
from nltk.corpus import conll2002 as conll
import sys
def evaluatemodel(file):
    """
    This function takes a pickled file and loads it.
    Then it prints the filename, the feature used and the samplesize.
    At last it prints the evaluated values of the classifier using the evaluate() method

    Parameters
    ----------
    file : name of pickled file you want to load    
    Returns
    -------
    None.

    """
    title = re.split(r"@", file)
    if title[1] == "whole": #if samplesize = whole it used all the sentences in ned.train for training
        title[1] = len(conll.chunked_sents("ned.train"))
    pickledfile = pickle.load(open(file, "rb"))
    testsent = conll.chunked_sents("ned.testa")
    print(file)
    print("Model used feature:", title[0], "using the first", title[1], "sentences from ned.train with algoritm:", title[2])
    print(pickledfile.evaluate(testsent))


if __name__ == "__main__":
    """Evaluates arguments as files, except when its best.pickle, so it doesnt try and read it as a normal file name, 
    since normal files have @'s in them to split on. best.pickle doesnt, so we have a different system."""
    file = sys.argv[1]
    if file == "best.pickle":
        pickledfile = pickle.load(open(file, "rb"))
        testsent = conll.chunked_sents("ned.testa")
        print(pickledfile.evaluate(testsent))
    else:
        evaluatemodel(file)