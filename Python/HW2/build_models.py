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


def modelbuilder(feature, samplesize=1000):
    import importlib

    if samplesize == "whole":
        trainer = conll.chunked_sents("ned.train")
    else:
        try:
            if int(samplesize) > len(conll.chunked_sents("ned.train")):
                raise ValueError
        except ValueError:
            print("not a valid samplesize")

        trainer = conll.chunked_sents("ned.train")[:int(samplesize)]

    try:
        chosen_feature = getattr(features, feature)
    except:
        print("not a valid feature")

    recognizer = ConsecutiveNPChunker(chosen_feature, trainer)
    title = feature + "@" + str(samplesize)
    file = open(title, 'wb')
    pickle.dump(recognizer, file)
    file.close()


if __name__ == "__main__":
    import sys

    feature = sys.argv[1]
    if len(sys.argv) > 2:
        # print("yeah")
        sample = sys.argv[2]

        modelbuilder(feature, sample)
    else:
        modelbuilder(feature)
