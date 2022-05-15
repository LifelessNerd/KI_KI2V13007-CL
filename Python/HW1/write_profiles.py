
import langdetect as ld
import os


def make_profiles(location, n, limit):
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
        # Hij overwrite wel gwn alle profiles steeds, dus als we dat niet willen moeten we daar iets aan doen
        ld.write_ngrams(table, naam + "-profile")
        print("Profile voor", f.name, "gemaakt!")
        os.chdir('../')
        os.chdir(location)
        # Dit kan beter, pech gehad! file shit in Python is echt het KUTSTE wat ik ooit heb gedaan


if __name__ == "__main__":
    # Alle dingen die moeten gebeuren als de file niet geimporteerd wordt maar gerunt
    # Is handig voor testing maar in het eindproduct bestaat deze file veelal uit declaraties en functies en geen statements

    location = "datafiles/datafiles/training/"
    make_profiles(location, 2, 200)
