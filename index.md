---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

## Global Health Observatory data repository
The Global Health Observatory data repository is the World Health Organization's gateway to health-related statistics for its 194 Member States. It provides access to over 1000 indicators on priority health topics including mortality and burden of diseases, the Millennium Development Goals (child nutrition, child health, maternal and reproductive health, immunization, HIV/AIDS, tuberculosis, malaria, neglected diseases, water and sanitation), non communicable diseases and risk factors, epidemic-prone diseases, health systems, environmental health, violence and injuries, equity among others.

Many of these datasets represent the best estimates of WHO using methodologies for specific indicators that aim for comparability across countries and time. Please check the Indicator and Measurement Registry for indicator specific information. Additional metadata and definitions can be found [here](http://apps.who.int/gho/data/node.metadata). The World Health Organization also provides [examples of API usage](http://apps.who.int/gho/data/node.resources.examples?lang=en)

### Example in Python
{% highlight python %}
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
{% endhighlight %}

### Example in R
{% highlight r %}
library(readr)
library(dplyr)
library(ggplot2)

# Flat file downloaded from:
# http://apps.who.int/gho/data/view.main.REGION2480A?lang=en

data <- read_csv('obesity.csv')

by.region <- data %>%
  group_by(REGION, YEAR) %>%
  summarize(mean.Numeric = mean(Numeric)/100)

ggplot(by.region, aes(x = YEAR, y = mean.Numeric, color = REGION)) +
  geom_point() +
  geom_line() +
  ggtitle('Obesity Rates Over Time', subtitle = 'Grouped By Region') +
ylab('Average Obesity Rate')
{% endhighlight %}

<br>
<br>
<br>

## FBI Crime Data API

The FBI Crime Data API is a read-only web service that returns JSON or CSV data. It is broadly organized around the FBI’s Uniform Crime Reporting systems data, and requires a [data.gov API network](https://api.data.gov/docs) key. Agencies submit data using one of two reporting formats -- the Summary Reporting System (SRS), or the National Incident Based Reporting System (NIBRS). 

The FBI also provides [full documentation](https://crime-data-explorer.fr.cloud.gov/api) and [source code](https://github.com/fbi-cde).

### Example in Python
{% highlight python %}
import requests
api_key = your_key_here 
base = 'https://api.usa.gov/crime/fbi/sapi/'
offenses = ['burglary', 'homicide', 'rape']

ori = 'api/agencies?api_key='
crime = 'api/summarized/agencies/{}/{}?api_key='

def get_data(query):
    '''Returns a dictionary of data from an API request.'''<br>
    response = requests.get(base + query + api_key)
    return response.json()

def get_county_agencies(data, state, county):
    '''<br>
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

### Example in R
{% highlight r %}
print("R Code!")
{% endhighlight %}
<br>
<br>
<br>

## American Time Use Survey

Researchers can produce their own time-use estimates using the ATUS microdata files. The ATUS data files include information for over 190,000 respondents total from 2003 to 2017. Because of the size of these data files, it is easiest to work with them using statistical software such as Stata, SAS, or SPSS.

The survey is sponsored by the Bureau of Labor Statistics and is conducted by the U.S. Census Bureau.

The major purpose of ATUS is to develop nationally representative estimates of how people spend their time. The survey also provides information on the amount of time people spend in many other activities, such as religious activities, socializing, exercising, and relaxing. Demographic information such as sex, race, age, educational attainment, etc. is also available for each respondent. Can we estimate the value of unpaid work?

[Microdata](https://www.bls.gov/tus/data.htm) 
 | [User Guide](https://www.bls.gov/tus/atususersguide.pdf)
