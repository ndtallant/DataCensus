'''
Code Snippet to work with the FBI Crime API

Nick Tallant, July 2018
'''
import requests
from dotenv import get_key, find_dotenv 

api_key = get_key(find_dotenv(),'FBI_KEY')
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
    data = get_data(crime.format(ori, offense))
    return data['results']
