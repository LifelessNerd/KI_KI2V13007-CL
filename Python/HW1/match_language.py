import langdetect as ld
import os
class LangMatcher:
    
    def __init__ (self, profilepath):
        """:param profilepath: The path to a directory with the saved ngram profiles
        Creates a dictionary whose keys are language names, and each value is itself a dictionary whose
        keys are ngrams and whose values are frequencies, stored under lang_dict"""
        self.lang_dict = {}
        os.chdir(profilepath)
        for file in os.listdir():  # Loop through all files in provided dir
            temp_key_list = file.split("-")
            temp_key = temp_key_list[0]
            #print(temp_key)
            temp_value = ld.read_ngrams(file)
            self.lang_dict[temp_key] = temp_value
        
        
    def score(self, text, k_best = 1):
        
        gramlijst = []
        gramlijstwinnaars = []
        
        bigram = ld.ngram_table(text, 2, 200)
        trigram = ld.ngram_table(text, 3, 200)
        for alledingen in self.lang_dict:
            gramlijst.append([ld.cosine_similarity(self.lang_dict[alledingen], bigram), alledingen]) 
        for alledingen in self.lang_dict:
            gramlijst.append([ld.cosine_similarity(self.lang_dict[alledingen], trigram), alledingen])
        gramlijst.sort(reverse = True)
        for i in range(k_best):
            gramlijstwinnaars.append(gramlijst[i][1])
        
        return gramlijstwinnaars

    def recognize(self, filename, encoding='utf8'):
        with open(filename, "r" ,encoding = 'utf8') as file:
            string = file.read()
            
            return self.score(string, 1)