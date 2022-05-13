import fnmatch
from pip._internal.cli.spinners import open_spinner
import langdetect as ld
import os


def make_profiles(location, n, limit):

    #evt default: datafiles/datafiles/training/

    os.chdir(location)
    print(os.getcwd())
    for file in os.listdir():
        os.chdir(location)
        print(os.getcwd())

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

        # BRON: https://www.geeksforgeeks.org/create-a-directory-in-python/#mkdir
        os.chdir('../')
        os.chdir('../')
        os.chdir('../') # bagger
        current = os.getcwd()
        directory = "models"
        # Dit moet beter kunnen, pech gehad! file shit in Python is echt het KUTSTE wat ik ooit heb gedaan
        path = os.path.join(current, directory)
        try:
            os.mkdir(path)
        except OSError as error:
            print("Directory already exists. Continuing...")


        os.chdir("/models/")
        ld.write_ngrams(table, naam + "-profile")
            
    
if __name__ == "__main__":
    # Alle dingen die moeten gebeuren als de file niet geimporteerd wordt maar gerunt
    # Is handig voor testing maar in het eindproduct bestaat deze file veelal uit declaraties en functies en geen statements

    location = "datafiles/datafiles/training/"
    make_profiles(location, 2, 200)
