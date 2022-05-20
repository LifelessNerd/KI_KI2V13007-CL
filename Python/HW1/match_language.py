import langdetect as ld
import os
import re


class LangMatcher:
    """
    The LangMatcher class fixes all things regarding which models folder to use, scoring and recognising languages
    using other functions from other modules
    """

    def __init__(self, profilepath):
        """
        When creating a LangMatcher, a file path needs to be specified to look up the models.
        Creates a dictionary whose keys are language names, and each value is itself a dictionary whose
        keys are ngrams and whose values are frequencies, stored under lang_dict

        :param profilepath: The path to a directory with the saved ngram profiles
        """
        self.lang_dict = {}
        self.profilepath = profilepath
        os.chdir(profilepath)
        for file in os.listdir():  # Loop through all files in provided dir
            temp_key_list = file.split("-")
            temp_key = temp_key_list[0]
            # print(temp_key)
            temp_value = ld.read_ngrams(file)
            self.lang_dict[temp_key] = temp_value

    def score(self, text, k_best=1):
        """
        This function uses other functions from langdetect to assign a score to every language based on the similarity
        of its n-gram tables, and ranks them.

        :param text: Text to be recognised and scored
        :param k_best: Amount of languages to be output
        :return: A list of k_best languages, ranked on score
        """
        self.gramlijst = []
        gramlijstwinnaars = []

        nlimit = os.path.split(self.profilepath)[1]
        n = nlimit.split("-")[0]
        limit = nlimit.split("-")[-1]

        ngrams = ld.ngram_table(text, int(n), int(limit)) # ngrams = ld.ngram_table(text, int(n), int(limit)) werkt niet
        for alledingen in self.lang_dict:
            self.gramlijst.append([ld.cosine_similarity(self.lang_dict[alledingen], ngrams), alledingen])

        self.gramlijst.sort(reverse=True)
        for i in range(k_best):
            gramlijstwinnaars.append(self.gramlijst[i][1])

        return gramlijstwinnaars

    def recognize(self, filename, encoding='utf-8'):
        """
        Function for lazy people: It opens the specified file & calls score on its contents

        :param filename: Filename of the text file that needs to be opened/scored
        """
        with open(filename, encoding = encoding) as file:
            string = file.read()
            return self.score(string, 1)


if __name__ == "__main__":
    import sys
    
    
    ln, textfile = sys.argv[1], sys.argv[2]
   
    ln2 = LangMatcher(ln)
    
    os.chdir("../")
    os.chdir("../")
    
    os.chdir("./datafiles")
    print(textfile, ln2.recognize(textfile), ln2.gramlijst[0][0])
    # Zie whatsapp wat hier nog moet

