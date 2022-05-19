# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:16:12 2022

@author: lucmi
"""
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
    
    gram = model_path[-5]
    zinl = test_path[-2:]
    goed = 0
    
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



