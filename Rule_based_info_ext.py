from pickle import TRUE
import re
import string
import nltk
import spacy
import pandas as pd
import numpy as np
import math
from tqdm import tqdm
import mymodule

from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy
import matplotlib.pyplot as plt
#import ipython

#load spaCy model
nlp = spacy.load("en_core_web_sm")

# sample text for X such as Y
text = "GDP in developing countries such as Vietnam will continue growing at a high rate."
mymodule.tok_func(nlp, text)
pattern = [{'DEP':'amod', 'OP':"?"}, # adjectival modifier
           {'POS':'NOUN'},
           {'LOWER': 'such'},
           {'LOWER': 'as'},
           {'POS': 'PROPN'}]
sp = mymodule.pattern_rec(nlp, text, pattern)
print(sp)

#sample text for pattern X and/or Y
text1 = "Here is how you can keep your car and other vehicles clean."
mymodule.tok_func(nlp, text1)
pattern1 = [{'DEP':'amod', 'OP':"?"}, 
           {'POS':'NOUN'}, 
           {'LOWER': 'and', 'OP':"?"},
           #'OP':'?' means optional exp, i. e. 'and'/'or' may or may not be there.
           {'LOWER': 'or', 'OP':"?"}, 
           {'LOWER': 'other'}, 
           {'POS': 'NOUN'}] 

sp1 = mymodule.pattern_rec(nlp, text1, pattern1)
print(sp1)



