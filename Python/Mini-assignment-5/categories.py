import sys
from collections import Counter
from nltk import word_tokenize, pos_tag
import nltk
from nltk.corpus import brown
nltk.download('universal_tagset')

if __name__ == "__main__":
    # Gets all inputs from command line arguments
    argslist = sys.argv[1:]
    for i in range(len(argslist)):
        argslist[i] = argslist[i].lower()

    # Counter logic
    tuplelist = []
    tupledict = {}
    brown_words = brown.tagged_words(tagset="universal")
    for word_tuple in brown_words:
        tuplelist = tupledict.keys()
        if word_tuple not in tuplelist:
            tupledict[word_tuple] = 0
        else:
            tupledict[word_tuple] += 1

    # Checking if argument is in dictionary, gets its amounts and prints
    for argument in argslist:
        for word_tag_tuple in tuplelist:
            if argument == word_tag_tuple[0]:
                print(word_tag_tuple[0], word_tag_tuple[1], end=" ")
                print(tupledict[(word_tag_tuple[0],word_tag_tuple[1])],  end=" ")
        print(" ")

# Output syntax isn't quite right, I have made this too hard for myself. Counter would work better and easier (I hope)
# My numbers are slightly off, and even when using Counter I believe this was the case. Did I miss something?
