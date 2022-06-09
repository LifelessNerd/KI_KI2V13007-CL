build_models.py: 

If you want to run this via the command line, the syntax is as follows: 
python build_models.py (feature (from features.py) you want to use) (the amount of sentences used from ned_train)
Keep in mind that the feature can be both a string and not a string. For example: python build_models.py test_feature 1000 or python build_models.py "test_feature" 1000
The amount of sentences used is 1000 by default, you do not have to give this as a parameter in the command line.
If you want to use the whole corpus of ned_train, give "whole" as amount of sentences used: 
python build_models.py test_feature whole (or "whole")
The filename is then: test_feature@whole
The builder pickles the data in a file called (feature used)@(sentences used), keep this in mind when loading the file in evaluate_models.py

evaluate_models.py:

Syntax in the command line is as follows:
python evaluate_models.py (file you want to load)
This time you do want to use a string. For example: python evaluate_models.py "test_feature@1000"
The program prints the file, the feature used, the amount of sentences used.
At the end the program evaluates the model using chunked sentences from ned_traina. It prints the results.
 