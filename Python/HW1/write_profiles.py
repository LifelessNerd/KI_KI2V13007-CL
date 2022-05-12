import fnmatch

from pip._internal.cli.spinners import open_spinner

import langdetect as ld
import os

if __name__ == "__main__":
    # Alle dingen die moeten gebeuren als de file niet geimporteerd wordt maar gerunt
    os.chdir("datafiles/datafiles/training/")
    for file in os.listdir():
        print(file)
        if "UTF8" in file:
            with open(file, encoding="utf8") as f:
                print(f.read())
        else:
            with open(file) as f:
                print(f.read())




else:
    pass
    # CODE

