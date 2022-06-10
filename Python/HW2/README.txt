build_models.py: 

If you want to run this via the command line, the syntax is as follows: 
python build_models.py (feature (from features.py) you want to use) (the amount of sentences used from ned_train) (algoritm you want to use)
Keep in mind that the feature and algoritm can be both a string and not a string. For example: python build_models.py test_feature 1000 or python build_models.py "test_feature" 1000
The amount of sentences used is 1000 by default, you do not have to give this as a parameter in the command line.

The default algoritm parameter is NaiveBayes, when you change the algoritm, the name changes.
When using a different algoritm, you need to give a samplesize as well. For example: 
python build_models.py test_feature IIS is not possible. Instead, use: python build_models.py test_feature 1000 IIS

If you want to use the whole corpus of ned.train, give "whole" as amount of sentences used: 
python build_models.py test_feature whole (or "whole")
The filename is then: test_feature@whole@NaiveBayes
The builder pickles the data in a file called (feature used)@(sentences used)@(algoritm), keep this in mind when loading the file in evaluate_models.py

evaluate_models.py:

Syntax in the command line is as follows:
python evaluate_models.py (file you want to load)
For example: python evaluate_models.py test_feature@1000@NaiveBayes
The program prints the file, the feature used, the amount of sentences used and the algoritm used.
At the end the program evaluates the model using chunked sentences from ned.testa. It prints the results.
 