---
title: Global Health Observatory Data Repository
tag: health
---
The Global Health Observatory data repository is the World Health Organization's gateway to health-related statistics for its 194 Member States. It provides access to over 1000 indicators on priority health topics including mortality and burden of diseases, the Millennium Development Goals (child nutrition, child health, maternal and reproductive health, immunization, HIV/AIDS, tuberculosis, malaria, neglected diseases, water and sanitation), non communicable diseases and risk factors, epidemic-prone diseases, health systems, environmental health, violence and injuries, equity among others.

Many of these datasets represent the best estimates of WHO using methodologies for specific indicators that aim for comparability across countries and time. Please check the Indicator and Measurement Registry for indicator specific information. Additional metadata and definitions can be found [here](http://apps.who.int/gho/data/node.metadata). The World Health Organization also provides [examples of API usage](http://apps.who.int/gho/data/node.resources.examples?lang=en).

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
