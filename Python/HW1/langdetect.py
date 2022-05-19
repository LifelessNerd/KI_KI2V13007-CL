import re


def prepare(string):
    """
    Function that removes any weird characters. Output to be used by a number of functions.
    The n-grams should be clean and not have any weird characters.

    :param string: Input string to be prepared
    :return: a prepared string to be used elsewhere for n-gram extraction
    """
    gesplit = re.split(r'[!|?|"|,|.|(|)|<|>]', string)
    newline = " ".join(gesplit)
    newline1 = newline.split()
    return newline1


def ngrams(seq, n=3):
    """
    Function that creates a list of all ngrams for a certain sequence of words/ a string
    Outputs a list of ngrams, without spaces or any weird characters due to the prepare function

    :param seq: Sequence to be converted into n-grams
    :param n: Of how many characters the ngrams should consist
    :return: a list of all ngrams of the input sequence.
    """
    ngrams_list = []
    i = 0
    while i <= len(seq) - n:
        ngram = ""
        ngram = seq[i: i + n]
        ngrams_list.append(ngram)
        i += 1
    return ngrams_list


def ngram_table(text, n=3, limit=0):
    """
    Uses text, lenght of n-gram and a limit to create a ngram-dictionary that consists of the n-gram itself as a key,
    and the frequency as value. The dictionary is sorted on this value, and cut of based on the input of limit.

    :param text: Text to be converted into an ngram-table
    :param n: Of how many characters the ngrams should consist
    :param limit: How many ngrams should be output in the list (sorted by frequency)
    :return: A dictionary with a limited length, ordered by frequency that is contained in the value
    """
    word_list = prepare(text)
    ngram_dict = {}
    limited_ordered_dict = {}

    for index, item in enumerate(word_list):
        tokenized_word = "<" + item + ">"
        word_list[index] = tokenized_word
        # Logic om van woord naar ngram te gaan (hopelijk zonder een nieuwe for-loop)
        ngram_list = ngrams(word_list[index], n)

        for index_2, ngram in enumerate(ngram_list):
            # Ngram in dict zetten of frequentie aanpassen als duplicate
            if ngram in ngram_dict:
                # duplicate: +1 bij freq
                ngram_dict[ngram] += 1
            else:
                ngram_dict[ngram] = 1

            index_2 += 1
        index += 1

    # Dict orderen
    ordered_dict = dict(sorted(ngram_dict.items(), key=lambda x: x[1], reverse=True))
    # Combi van 2 bronnen:
    # BRON: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    # BRON: https://careerkarma.com/blog/python-sort-a-dictionary-by-value/

    for index, item in enumerate(ordered_dict):
        # Als de limit 0 is gewoon de hele lijst returnen
        if limit == 0:
            return ordered_dict

        elif index < limit:
            # de KV-pairs die onder limit liggen in nieuwe lijst kopieren
            key = item
            limited_ordered_dict[key] = ordered_dict[key]

        index += 1

    return limited_ordered_dict


def write_ngrams(table, filename):
    """
    Function that opens a file and writes an n-gram-table

    :param table: The ngram table that can be created by the ngram_table function
    :param filename: The file to which the ngram-table should be written
    :return: None
    """
    with open(filename, 'w', encoding='utf8') as f:
        for key, value in table.items():
            string = '%s:%s\n' % (key, value)
            f.write(string)  # bron: https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/
    f.close()


def read_ngrams(filename):
    """
    Reads ngrams out of the filename and puts them into a dictionary (n-gram-table)

    :param filename: The filename of the file to be read and analyzed and put into an n-gram table
    :return: N-gram table based on text in that file
    """
    dicto = dict()
    with open(filename, "r", encoding='utf8') as f:
        string = f.read()
    f.close()

    nstring = string.split("\n")
    del nstring[-1]  # laatse zin is een lege string als het gesplit wordt
    for element in nstring:
        splitter = element.split(":")
        dicto[splitter[0]] = int(splitter[-1])

    return dicto


def cosine_similarity(known, unknown):
    """
    Calculates the similarity score for 2 ngram-tables.

    :param known: Ngram-table out of training set
    :param unknown: Ngram-table you want the similarity score for
    :return: Similarity score (higher = better)
    """
    dot_product = 0
    for x in known:  # calculates dot product
        if x in unknown:
            dot_product += known[x] * unknown[x]

    magnitude_known = calculate_magnitude(known)
    magnitude_unknown = calculate_magnitude(unknown)

    return dot_product / (magnitude_known * magnitude_unknown)  # calculates entire cosine similarity and returns result


def calculate_magnitude(dictionary):
    """
    Calculates magnitude of dictionary, to be used in cosine_similarity

    :param dictionary: Input n-gram dictionary
    :return: Magnitude of n-gram dictionary
    """
    from math import sqrt
    magnitude = 0
    for x in dictionary:
        magnitude += dictionary[x] ** 2
    return sqrt(magnitude)