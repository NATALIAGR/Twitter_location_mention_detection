#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
@author: Natalia Grion

"""
get_ipython().system('pip install emoji')
import emoji
import re

# clean twitters
def clean_standard(text):
        """ it goes through standard cleaning: commas in numbers, replace & per "and", DM per "message", 
        substract RT, and remove https 
        requirements: import re
        """
        # remove commas in numbers (else vectorizer will split on them)
        text = re.sub(r',([0-9])', '\\1', text)
        # sort out HMTL formatting of &
        text = re.sub(r'&', 'and', text)
          # remove @name 
        text = re.sub(r'(?:\@|https?\://)\S+', '', text)
        # remove hashtags
        text= re.sub(r'#','', text)
            # replace DM and RT
        text= re.sub(r' DM ',' message ', text)
        text= re.sub(r' RT ','', text)
        # strip urls
        return re.sub(r'http[s]{0,1}://[^\s]*', '', text)
    
    
def clean_emoji(text):
        """ clean text from emoji's 
        requirement: install emoji and import emoji """
        allchars = text#[str for str in text.decode('utf-8')]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)]) #.decode('utf-8')
        return text



def clean_web_links(text):
        """Remove mention to pics or webpages attached by the user. 
        Mentions to pics come in the form of: pic.twitter.com/t9R15yUTHD
         and mentiones to webpages (this comes from YW): ow.ly ...
         requirement: import re"""
        # remove @name 
        text= re.sub(r'pic.twitter.com\S+', '', text)
        return re.sub(r'ow.ly\S+', '', text)

