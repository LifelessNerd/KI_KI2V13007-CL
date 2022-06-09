import pandas as pd


def test_features(sentence, i, history):
    """Chunker features designed to test the Chunker class for correctness 
        - the POS tag of the word
        - the entire history of IOB tags so far
            formatted as a tuple because it needs to be hashable
    """
    word, pos = sentence[i]
    return {
        "pos": pos,
        "whole history": tuple(history)
    }


def features_luka(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]

    capital, prevcapital = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,

        "whole history": tuple(history)
    }


def features_luka_locfile(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]

    data = pd.read_csv("world-cities.csv")
    df = pd.DataFrame(data, columns=['name'])
    df = df.values.tolist()

    in_loc_file = False
    capital, prevcapital = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True
    if word in df:
        in_loc_file = True

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,

        "whole history": tuple(history)
    }

# data = pd.read_csv("world-cities.csv")
# df = pd.DataFrame(data, columns=['name'])
# df = df.values.tolist()
# if "Pretor" in df:
#     print("shite")

