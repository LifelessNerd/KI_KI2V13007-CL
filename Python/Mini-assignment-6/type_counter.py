from collections import defaultdict, Counter


class TagTypes:
    """
    Given an NLTK tagged corpus, and optionally a tagset such as "universal"
     for Brown, stores a dict of tags and the words with those tags.

    Attributes:
        pos_dict: a dict from str (pos tags) to sets of strings (words)
        counts: a counter for the pos tags
    """

    def __init__(self, corpus, tagset=None):
        """
        Given an nltk tagged corpus, builds a dict of pos tags and set of words
        with those tags, storing it as pos_dict.
        If a tagset is given, uses it as the optional `tagset` parameter for
        the corpus's method tagged_words.

        :param corpus: nltk tagged corpus such as nltk.corpus.brown
        :param tagset: str: Optional. The name of the tagset; if None,
         the default is used.
        """
        if tagset is not None:
            tagged_words = corpus.tagged_words(tagset=tagset)
        else:
            tagged_words = corpus.tagged_words()

        # we use a set because we want types, not tokens (no duplicates!)
        self.pos_dict = defaultdict(set)
        for word, tag in tagged_words:
            word = word.lower()
            self.pos_dict[tag].add(word)  # case insensitive

        # store the counts too
        self.counts = Counter(dict([(k, len(self.pos_dict[k]))
                                    for k in self.pos_dict]))

    def __repr__(self):
        """
        catgories and their raw frequencies in alphabetical order
        :return string representation of the object
        """
        return "\n".join([f"{tag} {self.counts[tag]} types"
                          for tag in sorted(self.counts)])

    def __eq__(self, other):
        """
        equality for two TagTypes object because pickle doesn't think
         the round trip should work
        :param other: TagTypes
        :return: bool
        """
        return self.pos_dict == other.pos_dict and self.counts == other.counts

    def examples(self, tag, n=1):
        """
        Return a list of n words with the given tag.
        :param tag: str
        :param n: int, default 1
        :return string list
        """
        return list(self.pos_dict[tag])[:n]
