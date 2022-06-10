import nltk
import pandas
nltk.download('conll2002') # Better safe than sorry
from nltk.chunk.util import conlltags2tree, tree2conlltags
from nltk.corpus import conll2002 as conll
from copy import copy
from abc import ABC
from nltk.corpus import conll2002 as conll
import nltk
from nltk.chunk.util import conlltags2tree, tree2conlltags
# If numpy is absent, the nltk fails with a very confusing error.
# We avoid problems by checking directly
try:
    import numpy
except ImportError:
    print("You need to download and install numpy!!!")




# for debugging, use a tiny corpus
tiny_sample = 10
training = conll.chunked_sents("ned.train")[:tiny_sample] # SHORT DATASET: FOR DEMO/DEBUGGING ONLY!
# training = conll.chunked_sents("ned.train")
testing = conll.chunked_sents("ned.testa")


def reformat_corpus_for_tagger(train_sents):
    """
    Given a corpus in nltk.Tree format, returns the corpus as a list of lists of tuples,
    where each tuple ((word, POS), IOB) includes the word, its POS tag, and the IOB tag to be predicted.
    @param train_sents nltk.Tree list
    """
    return [[((word, pos), iob) for (word, pos, iob) in tree2conlltags(sent)] for sent in train_sents]





def create_training_data(feature_map, train_sents):
    """
    Creates training data from the corpus of train_sents and the feature_map
    :param feature_map: function that maps (untagged sentence, word index,
     history) to a dict of features (from features.py)
    :param train_sents: training sentences as lists of nltk.Tree objects
    :return: list of (dict, IOB tag) pairs
    """
    # TODO reformat sentences to ((word, pos_tag), iob_tag) pairs

    # TODO turn the sentences into appropriate training data by finding their features
    # TODO reformat sentences to ((word, pos_tag), iob_tag) pairs
    _train_set = []
    reformated = reformat_corpus_for_tagger(train_sents)
    # print(reformated)

    # TODO turn the sentences into appropriate training data by finding their features
    # store them in self._train_set
    for sent in reformated:
        sentlist = []
        sent = copy(sent)
        sent2 = [(word, tag) for ((word, tag), ios) in sent]

        for i in range(len(sent)):
            _train_set.append(tuple([feature_map(sent2, i, sentlist), sent[i][1]]))

            sentlist.append(sent[i][1])

    return _train_set



"""Checks if Numpy is present, if not raises an error."""
# If numpy is absent, nltk fails with a very confusing error.
# We avoid problems by checking directly
try:
    import numpy
except ImportError:
    print("You need to download and install numpy!!!")
    raise


training = conll.chunked_sents("ned.train")#[:100]

