import re


def prepare(string):
    gesplit = re.split(r'[!|?|"|,|.|(|)|<|>]', string)
    newline = " ".join(gesplit)
    newline1 = newline.split()
    return newline1


def ngrams(seq, n=3):
    ngrams_list = []
    i = 0
    while i <= len(seq) - n:
        ngram = ""
        ngram = seq[i: i + n]
        ngrams_list.append(ngram)
        i += 1
    return ngrams_list


def ngram_table(text, n=3, limit=0):
    word_list = prepare(text)
    # output: ['Lorum', 'ipsum', 'dolor', 'sit', 'amet']
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

    allowed = True
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

def cosine_similarity(known, unknown):
    dot_product = 0
    for x in known: #calculates dot product
        if x in unknown:
            dot_product += known[x]*unknown[x]
    
    magnitude_known = calculate_magnitude(known)
    magnitude_unknown = calculate_magnitude(unknown)
    
    return dot_product / (magnitude_known * magnitude_unknown) #calculates entire cosine similarity and returns result

def calculate_magnitude(dictionary): #calculates magnitude of dictionary
    from math import sqrt
    magnitude = 0
    for x in dictionary:
        magnitude += dictionary[x]**2
    return sqrt(magnitude)


print(ngram_table("hiep, hiep, hoera!", 3, 0))

