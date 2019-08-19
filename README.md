# Twitter_incident-mention-detection
"""

Author= Natalia Grion

Date= March 2019

"""


DATA:
'---.csv'
 These are the main modules I created to develop an early warning system pipeline based on social media channels from the company interested.
 These modules were created analyzing historical twitter data.  
a) Clean twitters to prepare the text for location information detection.
  To extract location information in 3 different ways:
b) Find 'street' (lane, avenue) mentions using regex
c) Find post code mentions using the regex for UK postcode format. This module has an extra function to standirize postcodes: by correcting 'missing space' typo. 
d) Apply neural network package spaCy. https://spacy.io/usage/spacy-101
d)It geocodes locations found and concatenates long-lat for each source into the dataframe. 


         Modules created: 

        a) clean_tweet.py
        b) find_street_mention.py
        c) find_postcode_mention.py
        d) find_ner_mention.py
        e) geocode_tweet_location.py
