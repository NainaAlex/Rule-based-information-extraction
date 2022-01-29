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

# sample text 
text = "We eat vegetables at home, like spinach, potatoes etc." 
text1 = "GDP in developing countries such as Vietnam will continue growing at a high rate."

# create a spaCy object 
document = nlp(text)
document1 = nlp(text1)

mymodule.tok_func(document)
mymodule.tok_func(document1)

pattern1 = [{'POS':'NOUN'},
            {'LOWER': 'such'},
            {'LOWER': 'as'},
            {'POS': 'PROPN'}]

pattern2 = [[{'POS':'VERB'},
            {'POS':'NOUN'}],

            [{'POS':'ADP'},
            {'POS':'NOUN'},
            {'DEP':'punct'},
            {'POS':'NOUN'}]]

pattern3 = [{'POS':'ADP'},
            {'POS':'NOUN'},
            {'DEP':'punct'},
            {'POS':'NOUN'}]

# Matcher class object 
matcher = Matcher(nlp.vocab)
matcher.add("matching_1", pattern2)

matches = matcher(document)
print(len(matches))

for i in range(len(matches)):
    span = document[matches[i][1]:matches[i][-1]]
    print(span.text)

span = document[matches[0][1]:matches[0][-1]]
span1 = document[matches[len(matches)-1][1]:matches[len(matches)-1][-1]]

print(span.text + ' ' + span1.text)

#displacy.render(document, style='dep', jupyter=True)
#mymodule.vis_dependency_parsing(text)


