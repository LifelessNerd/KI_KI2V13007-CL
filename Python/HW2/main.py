import nltk
from nltk.chunk.util import conlltags2tree, tree2conlltags

# If numpy is absent, the nltk fails with a very confusing error.
# We avoid problems by checking directly
try:

    import numpy
except ImportError:
    print("You need to download and install numpy!!!")
    raise
