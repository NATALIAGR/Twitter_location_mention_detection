#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
@author: Natalia Grion

"""
import re
import nltk
from nltk import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')



# Regex street loop
street_compiler= re.compile(r'\w+\s([Rr](oa)?d|[Ss]tr(eet)?|[Aa]v(enue)?|[Ll](a)?n(e)?)')
def find_street_mention(text):
    """ find matches through regex, then with nltk discards matches in which there is no NOUN found before word 'street'
        this is to avoid matches of the kind 'the road
        requirements: import nltk
                      from nltk import word_tokenize
                      nltk.download('averaged_perceptron_tagger')
                      nltk.download('vader_lexicon')
    """
    match = street_compiler.search(text)
# Discard matches in which there is no NOUN found before word 'street' this is to avoid matches of the kind 'the road
    if match==None:
        data_=None
    else:
        item= match.group(0)
        tokenized = nltk.word_tokenize(item)
        tagged = nltk.pos_tag(tokenized)
        if (tagged[0][1].startswith('DT') | tagged[0][1].startswith('VB') | tagged[0][1].startswith('IN')
            | tagged[0][1].startswith('CC') | tagged[0][1].startswith('PRP$')):
            data_=None
        else: 
            data_= match.group(0)

    return data_

