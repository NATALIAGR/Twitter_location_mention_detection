#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
@author: Natalia Grion

"""


import re
# Use compiler to speed up
post_finder=re.compile(r'\b([gG][iI][rR]{0,}0[aA]{2})|((([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y]?[0-9][0-9]?)|(([a-pr-uwyzA-PR-UWYZ][0-9][a-hjkstuwA-HJKSTUW])|([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y][0-9][abehmnprv-yABEHMNPRV-Y]))) {0,}[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2})\b')


def find_postcode_mention(text):
    """Find postcodes mentions with regex    
    requirements: import re
    """
    match=post_finder.search(text)
    if match==None:
        data_=None
    else:
        data_= match.group(0)    

    return data_

    
def standarize_postcode(post):
    """Transform postcodes without space into standard format 
    (this is because geocoder does not recognize full lenght postcodes without space). 
    This is the most common typo, then users might put whitspaces randomly and that is 
    deleterious for the geocoder too. This is sth to consider for improvement"""
    if (post!=None):
        if len(post) >= 6 and " " not in post:
            i = -1
            while post[i] not in "0123456789":
                i -= 1
            post=(f"{post[:i]} {post[i:]}")
        else:
            post=post
    return post

