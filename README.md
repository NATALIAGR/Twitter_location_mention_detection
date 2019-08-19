# Introduction

These are the main modules I created as part of a project I developed: an early warning system pipeline based on social media channels. I used historical data (csv format) but functions can be inserted into an online twitter stream pipeline.
Hope you find it useful. 


# Data:
'---.csv'
 
# Modules created: 

a) clean_tweet.py
b) find_street_mention.py
c) find_postcode_mention.py
d) find_ner_mention.py
e) geocode_tweet_location.py
 
a) Clean twitters to prepare the text for location information detection.

Extract location information (from tweets) in 3 different ways:

b) Find 'street' (lane, avenue) mentions using regex.
c) Find post code mentions using the regex for UK postcode format. This module has an extra function to standirize postcodes: by correcting 'missing space' typo. 
d) Apply neural network package spaCy. https://spacy.io/usage/spacy-101

d)It geocodes locations found and concatenates long-lat for each source into the dataframe. 

