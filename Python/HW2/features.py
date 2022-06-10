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
    """"# This featureset uses the 6 perfect features plus the next word and its features.
		word, pos = the word itself and its pos tag
		capital: whether the first letter of the word is a capital (boolean)
		prevcapital: whether the first letter of the previous word is a capital (boolean)
		prevword: the previous word in the sentence
		prevpos: the pos of the previous word
		nextword: the next word
		nextpos: the pos of the next word
		nextcapital: whether the first letter of the next word is a capital (boolean)"""

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
    """"# This featureset uses a list of countries from https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv
		word, pos, capital, prevcapital, prevword, prevpos
		in_loc_file: if the word is in the countries file"""
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
    """# This featureset uses a list of names found at https://www.meertens.knaw.nl/nvb/topnamen/provincie/Utrecht/2014
		word, pos, capital, prevcapital, prevword, prevpos
		in_loc_file: if the word is in the names file"""
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
    """This is generally the best featureset, as given in the notebook as a striven for accuracy
		# Later featuresets are based on this one, with extra features
		word, pos, capital, prevcapital, prevword, prevpos"""
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
    """# Based on the features_best featureset, with a "BV" check implemented
		word, pos, capital, prevcapital, prevword, prevpos
		containsBV: if the next word is equal to "bv" or "b.v.", if so, this current word is probably a business (boolean)"""
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
    """# Uses the features_best set, plus all checklist variables
		# csv's used:
			world-cities.csv (https://github.com/datasets/world-cities/blob/master/data/world-cities.csv)
			countries.csv (see previous reference)
			names.csv (see previous reference)
		word, pos, capital, prevcapital, prevword, prevpos
		name: if the word is a name (boolean)
		city: if the word is a city (boolean)
		country: if the word is a country (boolean)"""
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
    """# Uses only list checks
		# csv's used:
			world-cities.csv (https://github.com/datasets/world-cities/blob/master/data/world-cities.csv)
			countries.csv (see previous reference)
			names.csv (see previous reference)
		name: if the word is a name (boolean)
		city: if the word is a city (boolean)
		country: if the word is a country (boolean)"""
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
    """# Uses all features from features_best, plus a capitals count
		word, pos, capital, prevcapital, prevword, prevpos
		capcount: a count of how many letters in the word are capitals (int)"""
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
