#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install geopy')
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
from tqdm import tqdm
import time
import pandas as pd


# view_box referes to the area of competence of Yorkshire Waters (+ what falls into the square). It was created manually using 
# https://boundingbox.klokantech.com/: -2.4602,53.1375,0.1985,54.6077
# view_box has the form: [Point(22, 180), Point(-22, -180)]

geolocator = Nominatim(format_string=None, view_box=[(54.6077,0.1985),(53.1375,-2.4602)], bounded=True, 
                        country_bias='gb-eng', 
                        domain='nominatim.openstreetmap.org', scheme=None, 
                        user_agent='my-application')

def geocode_tweetsYW_area(x):
    """ Apply Geopy. Import Nominatim and set the params for it. Use a time to sleep of 
        2 secs in the loop to avoid limit of 1query/sec
        Input: x: list of column data of addresses to be geolocated.
               for example:x= df['Street Found'].tolist()
       requirements:
                    !pip install geopy
                    from geopy.geocoders import Nominatim
                    from geopy.extra.rate_limiter import RateLimiter
                    from geopy.exc import GeocoderTimedOut
                    from tqdm import tqdm
                    import time
    """
    #x= df['Street Found'].tolist()
    geocoded=[]
    for item in range(len(x)):
        d={}
        if pd.isna(x[item]):
            d['Address']= None
            d['Lat']=None
            d['Lon']=None
        else:
            a=geolocator.geocode(x[item], exactly_one=True,timeout=60,language='en')
            try:
                d['Address']=a.address
            except:
                pass
            try:
                d['Lat']=a.latitude
            except:
                pass
            try:
                d['Lon']=a.longitude
            except:
                pass
            time.sleep(2)
        geocoded.append(d)
    #Convert the geocoded list into a dataframe
    df_geocoded=pd.DataFrame(geocoded)  
    return df_geocoded

