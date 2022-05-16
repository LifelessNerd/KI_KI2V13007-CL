import langdetect as ld
import os


class LangMatcher:

    def __init__(self, path):
        """:param path: The path to a directory with the saved ngram profiles"""
        lang_dict = {}
        os.chdir(path)
        for file in os.listdir():  # Loop through all files in provided dir
            temp_key_list = file.split("-")
            temp_key = temp_key_list[0]
            print(temp_key)
            temp_value = ld.read_ngrams(file)
            #lang_dict.update({temp_key: temp_value})

        print(lang_dict)

    def score(self, text, k_best=1):
        pass


lang_matcher = LangMatcher("models/2-200")
