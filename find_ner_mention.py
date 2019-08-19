#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
@author: Natalia Grion

"""



get_ipython().system('pip install spacy ')
get_ipython().system('python -m spacy download en_core_web_lg')
import spacy 
from spacy import displacy
from collections import Counter
# For this phase use the large model
import en_core_web_lg
nlp=  spacy.load('en_core_web_lg')



def extract_entities_spacy(text):
    """
    run Spacy (it has a new functionality to remove whitespaces from tagging as entities). 
    The loop put together the interested tags in a single sting, 
    and add Nan value when no tag is found
    Picks up tags as FAC, ORG, GPE, LOC, see Spacy documentation.
    requirements: 
                    !pip install spacy 
                    !python -m spacy download en_core_web_lg
                    import spacy 
                     from spacy import displacy
                    from collections import Counter
                    # For this phase use the large model
                    import en_core_web_lg
                    nlp=  spacy.load('en_core_web_lg')
    """

    doc = nlp(text)
    ents = [(e.text) for e in doc.ents if e.label_ in ('FAC','ORG','GPE','LOC')]
   # print(ents)
    if not ents:
        entities= None
    else:                                  
        entities= ' '.join(ents)
    return entities

