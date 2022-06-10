import pandas as pd

data = pd.read_csv("countries.csv")
df = pd.DataFrame(data, columns=['name'])
df = df.values.tolist()

namesdata = pd.read_csv("names.csv")
names = pd.DataFrame(namesdata, columns=['name'])
names = names.values.tolist()

locdata = pd.read_csv("world-cities.csv")
locations = pd.DataFrame(namesdata, columns=['name'])
locations = locations.values.tolist()


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


def features_prevnext(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]
    try:
        nextword, nextpos = sentence[i + 1]
    except:
        nextword, nextpos = sentence[i]

    capital = False
    prevcapital = False
    nextcapital = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True
    if nextword[0].isupper():
        nextcapital = True

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,
        "nextword": nextword,
        "nextpos": nextpos,
        "nextcapital": nextcapital,

        "whole history": tuple(history)
    }


def features_luka_countries(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]

    in_loc_file = False
    capital = False
    prevcapital = False
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
        "in_loc_file": in_loc_file,

        "whole history": tuple(history)
    }


def features_luka_names(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]

    in_loc_file = False
    capital = False
    prevcapital = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True
    if word in names:
        in_loc_file = True

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,
        "in_loc_file": in_loc_file,

        "whole history": tuple(history)
    }


def features_best(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]

    capital = False
    prevcapital = False
    nextcapital = False
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


def features_best_BV(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]
    try:
        nextword, nextpos = sentence[i + 1]
    except:
        nextword, nextpos = sentence[i]

    capital = False
    prevcapital = False
    nextcapital = False
    containsBV = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True
    if "bv" in nextword.lower() or "b.v." in nextword.lower():
        containsBV = True

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,
        "containsBV": containsBV,

        "whole history": tuple(history)
    }


def features_luka_whole_bimbam(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]

    name = False
    city = False
    country = False
    # floraluxtest = False

    capital = False
    prevcapital = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True
    if word in names:
        name = True
    if word in df:
        country = True
    if word in locations:
        city = True
    # if word == "Floralux":
    #     floraluxtest = True
    #     print("very wow very wow")

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,
        "name": name,
        "city": city,
        "country": country,
        # "floraluxtest": floraluxtest,

        "whole history": tuple(history)
    }


def features_luka_lists(sentence, i, history):
    word, pos = sentence[i]

    name = False
    city = False
    country = False
    # floraluxtest = False

    if word in names:
        name = True
    if word in df:
        country = True
    if word in locations:
        city = True
    # if word == "Floralux":
    #     floraluxtest = True
    #     print("very wow very wow")

    return {
        "name": name,
        "city": city,
        "country": country,
        # "floraluxtest": floraluxtest,

        "whole history": tuple(history)
    }


def features_best_capcount(sentence, i, history):
    word, pos = sentence[i]
    prevword, prevpos = sentence[i - 1]
    capcount = 0

    capital = False
    prevcapital = False
    nextcapital = False
    if word[0].isupper():
        capital = True
    if prevword[0].isupper():
        prevcapital = True
    index = 0
    for char in word:
        if char.isupper():
            capcount += 1

    return {
        "word": word,
        "pos": pos,
        "capital": capital,
        "prevcapital": prevcapital,
        "prevword": prevword,
        "prevpos": prevpos,
        "capcount": capcount,

        "whole history": tuple(history)
    }
