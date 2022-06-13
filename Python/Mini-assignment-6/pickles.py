import type_counter as tc
import pickle
import sys
import nltk.corpus


def make_and_pickle(corpus, path, tagset=None):
    tagtype = tc.TagTypes(corpus, tagset)
    file = open(path, 'wb')
    pickle.dump(tagtype, file)
    file.close()


def unpickle(path):
    file = open(path, 'rb')
    tagtype = pickle.load(file)
    file.close()
    return tagtype


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 3:
        function = sys.argv[1]
        path = sys.argv[2]
        if function == "--pickle":
            make_and_pickle(nltk.corpus.conll2000, path, tagset="universal")
        elif function == "--unpickle":
            print(unpickle(path))
        else:
            print("Argument '", function, "' was not recognised, nothing happened.")

    else:
        print("You specified the wrong amount of parameters, nothing happened. 2 arguments should be given: function "
              "and path.")
