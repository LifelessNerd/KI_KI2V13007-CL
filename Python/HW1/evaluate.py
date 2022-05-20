import os
import match_language as ml

langdict = dict()
langdict["da"] = "Danish"
langdict["de"] = "German"
langdict["el"] = "Greek"
langdict["en"] = "English"
langdict["es"] = "Spanish"
langdict["fi"] = "Finnish"
langdict["fr"] = "French"
langdict["it"] = "Italian"
langdict["nl"] = "Dutch"
langdict["pt"] = "Portuguese"
langdict["sv"] = "Swedish"



def eval(model_path, test_path):
    """
    This function takes a certain ngram collection compares it to every file in a europarl collection with the
    recognize function. For every comparison, it prints the filename, the predicted language from recognize and the
    language from the text of the file. If the predicted language is not the same as the actual language it adds
    ERROR to the message. At the end this function prints the type of ngram, the amount of words in the text from the
    testdata files, the amount of correctly predicted languages and the amount of incorrectly predicted languages.

    :param model_path: path to location where ngram dictionaries are stored (./models/2-200 or ./models/3-200)
    :param test_path: path to location where testdata is stored (path to europarl-10/30/90)
    """

    gram = model_path[-5]
    zinl = test_path[-2:]
    goed = 0 #counts the number of correct predictions
    
    gramstr = ""
    if gram == "2":
        gramstr = "Bigram"
    else:
        gramstr = "Trigram"
    
    ln = ml.LangMatcher(model_path)
    os.chdir("../")
    os.chdir("../")
    os.chdir(test_path)
    
    
    for file in os.listdir():
        echtetaal = langdict[file[-2:]]
       
        x = ln.recognize(file)
        if x[0] != echtetaal:
          
            print(file, x[0], "ERROR", echtetaal)
        else:
            print(file, x[0])
            goed += 1
        
    print(gramstr, "models for " + zinl + "-word sentences:", goed, "correct,", len(os.listdir()) - goed, "incorrect")

if __name__ == "__main__":
    eval("./models/2-200", "./datafiles/datafiles/test/europarl-10")
    for n in range(4):
        os.chdir("../")
    eval("./models/2-200", "./datafiles/datafiles/test/europarl-30")
    for n in range(4):
        os.chdir("../")
    eval("./models/2-200", "./datafiles/datafiles/test/europarl-90")
    for n in range(4):
        os.chdir("../")
    eval("./models/3-200", "./datafiles/datafiles/test/europarl-10")
    for n in range(4):
        os.chdir("../")
    eval("./models/3-200", "./datafiles/datafiles/test/europarl-30")
    for n in range(4):
        os.chdir("../")
    eval("./models/3-200", "./datafiles/datafiles/test/europarl-90")



