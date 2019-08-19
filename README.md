# Twitter_incident-mention-detection
"""

Author= Natalia Grion

Date= March 2019

"""


DATA:
'---.csv'
 These are the main functions I created to develop an early warning system pipeline based on social media channels from the company interested.
 These functions were created analyzing historical twitter data.  

SCRIPTS content:

1) Twiter_incident_locationExtraction
a)This module loads twitter data (csv format) to extract location information in 3 different ways. 
b)It geocodes locations found and concatenates long-lat for each source into the dataframe. 
c)Saves the final dataframe for later usage
d)Computes the level of ocnfidence for each location geocoded according to the consistency of the data.


         Modules created and imported in this script: 

        clean_tweet.py
        find_street_mention.py
        find_postcode_mention.py
        find_ner_mention.py
        geocode_tweet_location.py
        label_tweets_confidence level.py


2) Plot_Coordinates_withLabelling. It loads the final dtaaframe with all location and geocded information
and plot it into a map of the area with the colors related to the level of confidence



