import requests
import numpy as np
import pandas as pd

base = ('http://apps.who.int/gho/athena/data/GHO/{}'
        '.json?profile=simple&filter=COUNTRY:*')

ad_restrictions = 'SA_0000001515'

def get_data(code):
    response = requests.get(base.format(code))
    data = get_data_helper(response.json())
    return pd.DataFrame(data)

def get_data_helper(who_dictionary):
    '''Pads the dictionary so entries are same length'''
    rv = [] 
    fact_table = who_dictionary['fact']
    for observation in fact_table:
        new_row = observation['dim']
        new_row['VALUE'] = observation['Value']
        rv.append(new_row)
    return rv

def clean_who_data(df):
    df['ad_type'] = df.ADVERTISINGTYPE.apply(lambda s: 
                                     s.replace(' Ads', ''))
    df.drop(['GHO', 'PUBLISHSTATE'
           , 'ADVERTISINGTYPE'], axis=1, inplace=True)
    df.replace('', np.NaN, inplace=True)

if __name__ == "__main__":
    df = get_data(ad_restrictions)
    clean_who_data(df)
    print('Preview:') 
    print(df.head())
    df.to_csv('WHO_ad_data.csv', index=False)
