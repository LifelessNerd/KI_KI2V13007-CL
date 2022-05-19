
import langdetect as ld
import os


def make_profiles(location, n, limit):
    """
    This function gets all training language files out of the location directory, opens them, creates n-gram-tables out
    of each of them, and puts those in language-specific files. They are put in a models folder based on the lenght
    of the n-grams (n), this folder is created if it did not exist already. Any profiles that are already present get
    overwritten.
    :param location:
    :param n:
    :param limit:
    :return:
    """
    # evt default: datafiles/datafiles/training/

    os.chdir(location)
    for file in os.listdir():

        if "UTF8" in file:
            with open(file, encoding="utf8") as f:
                naam = os.path.basename(f.name)
                string = f.read()

        else:
            with open(file) as f:
                naam = os.path.basename(f.name)
                string = f.read()

        table = ld.ngram_table(string, n, limit)

        os.chdir('../')
        os.chdir('../')
        os.chdir('../')
        path = os.path.join(os.getcwd(), "models")
        try:
            os.mkdir(path)
            print("Models folder bestond nog niet, gemaakt in", os.getcwd())
        except OSError as error:
            pass
        os.chdir("models/")
        path = os.path.join(os.getcwd(), str(n) + "-" + str(limit))
        try:
            os.mkdir(path)
            print("Models folder bestond nog niet, gemaakt in", os.getcwd())
        except OSError as error:
            pass
        os.chdir(str(n) + "-" + str(limit))
        # Hij overwrite wel gwn alle profiles steeds, dus als we dat niet willen moeten we daar iets aan doen
        ld.write_ngrams(table, naam + "-profile")
        print("Profile voor", f.name, "gemaakt!")
        os.chdir('../')
        os.chdir('../')
        os.chdir(location)
        # Dit kan beter, pech gehad! file shit in Python is echt het KUTSTE wat ik ooit heb gedaan
    print("Models stored in: " + path)


if __name__ == "__main__":
    # Alle dingen die moeten gebeuren als de file niet geimporteerd wordt maar gerunt
    # Is handig voor testing maar in het eindproduct bestaat deze file veelal uit declaraties en functies en geen statements

    make_profiles("datafiles/datafiles/training", 3, 200)
    make_profiles("datafiles/datafiles/training", 2, 200)
