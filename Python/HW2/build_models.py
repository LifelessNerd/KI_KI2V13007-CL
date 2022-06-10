# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:56:36 2022

@author: lucmi
"""
import pickle
import nltk
from nltk.chunk.util import conlltags2tree, tree2conlltags
from nltk.corpus import conll2002 as conll
import features
from custom_chunker import ConsecutiveNPChunker
import importlib
import sys
def modelbuilder(feature, samplesize = 1000, algoritm="NaiveBayes"):
    """
    This function takes a feature and samplesize from the commandline and trains a model using that feature and samplesize.
    It then pickles the classifier in a file called: (feature used)@(samplesize)
    
    Parameters
    ----------
    feature : feature you want to use
        
    samplesize : TYPE, string
        Amount of sentences of ned_train used to train algoritm. The default is 1000.


    """
  
    if samplesize == "whole": #if samplesize is "whole" use the whole dataset of ned.train
        trainer = conll.chunked_sents("ned.train")
    else:
        try:
            if int(samplesize) > len(conll.chunked_sents("ned.train")): #if samplesize is larger than the amound of sentences in ned.train
                raise ValueError
        except ValueError:
            print("not a valid samplesize")
            
        trainer = conll.chunked_sents("ned.train")[:int(samplesize)]
        
    try:
        chosen_feature = getattr(features, feature) #if feature does not exist (or is spelled wrongly)
    except:
        print("not a valid feature")
    
    recognizer = ConsecutiveNPChunker(chosen_feature, trainer, algoritm)
    title = feature + "@" + str(samplesize) + "@" + algoritm
    file = open(title, 'wb')
    pickle.dump(recognizer, file)
    file.close()
    print("file pickled succesfully under name:", title)
    
if __name__ == "__main__":
    """Builds models based on the feature set that is given in the argument"""

    feature = sys.argv[1]
    if len(sys.argv) == 3: # only if given two parameters in commandline (index 0 = build_models.py)
        sample = sys.argv[2]    
        modelbuilder(feature, sample)
    elif len(sys.argv) > 3: # for optional algoritm parameter
        sample = sys.argv[2] 
        algo = sys.argv[3]
        modelbuilder(feature, sample, algo)
    else:
        modelbuilder(feature)