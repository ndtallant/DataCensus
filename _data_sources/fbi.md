---
title: FBI Crime Data API
tag: Crime
---
The FBI Crime Data API is a read-only web service that returns JSON or CSV data. It is broadly organized around the FBI’s Uniform Crime Reporting systems data, and requires a [data.gov API network](https://api.data.gov/docs) key. Agencies submit data using one of two reporting formats -- the Summary Reporting System (SRS), or the National Incident Based Reporting System (NIBRS). 

The FBI also provides [full documentation](https://crime-data-explorer.fr.cloud.gov/api) and [source code](https://github.com/fbi-cde).
{% highlight python %}
import requests
api_key = your_key_here 
base = 'https://api.usa.gov/crime/fbi/sapi/'
offenses = ['burglary', 'homicide', 'rape']

ori = 'api/agencies?api_key='
crime = 'api/summarized/agencies/{}/{}?api_key='

def get_data(query):
    '''Returns a dictionary of data from an API request.'''
    response = requests.get(base + query + api_key)
    return response.json()

def get_county_agencies(data, state, county):
    '''
    Given a state and county, reutrns a list of
    dictionaries - keys being Originating Agency Identifiers
    (ORI) - for any county level agencies.
    '''
    ori_list = [] 
    for agency in data[state]:
        try:
            if data[state][agency]['county_name'] == county:
            ori_list.append(data[state][agency])
        except:
            continue
    return ori_list

data = get_data(ori_query, api_key)
wood_county_agencies = get_county_agencies(data, 'TX', 'WOOD')

def get_agency_crimes(ori, offense):
    data = get_data(crime.format(ori, offense))<br>
    return data['results']
{% endhighlight %} 
  
{% highlight R %}
print("R Code!")
{% endhighlight %} 
