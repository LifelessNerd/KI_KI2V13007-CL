import fnmatch

from pip._internal.cli.spinners import open_spinner

import langdetect as ld
import os
def make_profiles(datafiles, n, limit):

    if __name__ == "__main__":
        # Alle dingen die moeten gebeuren als de file niet geimporteerd wordt maar gerunt
        os.chdir("datafiles/datafiles/training/")
        for file in os.listdir():
            
            if "UTF8" in file:
                with open(file, encoding="utf8") as f:
                    naam = os.path.basename(f.name)
                    string = f.read()
                    #print(naam)
            else:
                with open(file) as f:
                    naam = os.path.basename(f.name)
                    string = f.read()
                    #print(naam)
    
            table = ld.ngram_table(string, n, limit)
            print(table)
        
            #ergens hier dus een path /models<n><limit> om het bestand uit ngram_write naartoe te doen
            print(ld.write_ngrams(table, naam))
            
    
    
    else:
        pass
        # CODE

make_profiles("ikd", 2, 200)
