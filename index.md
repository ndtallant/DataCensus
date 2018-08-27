---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

## Nationwide Readmissions Database (NRD)
The Nationwide Readmissions Database is designed to support various types of analyses of national readmission rates. The NRD includes discharges for patients with and without repeat hospital visits in a year and those who have died in the hospital. The criteria to determine the relationship between hospital admissions is left to the analyst using the NRD. 
This database was compiled by the Agency for Healthcare Research and Quality (AHRQ), who provides a [Data Dictionary](https://www.hcup-us.ahrq.gov/db/nation/nrd/nrddde.jsp) and [Full Documentation](https://www.hcup-us.ahrq.gov/db/nation/nrd/nrddbdocumentation.jsp).

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

## National Longitudinal Surveys (NLS)
Information on the labor market activities and other significant life events of several groups of men and women at multiple points in time. For more than 4 decades, NLS data have served as an important tool for economists, sociologists, and other researchers.The NLS program includes the following cohorts :

- [NLS Youth 1997 (NLSY97)](https://www.nlsinfo.org/content/cohorts/nlsy97): Respondents were ages 12-17 when first interviewed in 1997. 
- [NLS Youth 1979 (NLSY79)](https://www.nlsinfo.org/content/cohorts/nlsy79): Respondents were ages 14-22 when first interviewed in 1979. 
- [NLSY79 Children and Young Adults](https://www.nlsinfo.org/content/cohorts/nlsy79-children): Assessments of biological children of women in the NLSY79, starting in 1986.
- [NLS Young and Mature Women (NLSW)](https://www.nlsinfo.org/content/cohorts/mature-and-young-women): Young women born in the years 1943-53 and mature women born in the years 1922-37. 
- [NLS Young and Older Men (NLSM)](https://www.nlsinfo.org/content/cohorts/older-and-young-men): Young men born in the years 1941-52 and older men born in the years 1906-21. 

The download functionality for these data sets provides access to files for SPSS, SAS, Stata, R, or simply a csv. A tagset, codebook, description file, and log file are also included with a download.

The R, SAS, and SPSS files contain code needed to load the data set, as well as short explanations for missing values and level names.

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

## USDA National Agricultural Statistics Service API

This API provides access to data from the Census of Agriculture as well as national, state, and county level surveys. Data is queried through requesting commodities encapsulated in the sectors of Crops, Animals & Products, Economics, Demographics, and Environmental. The commodity statistics are aggregated for standard census geographies, agricultural statistics districts, and watershed boundaries over annual, seasonal, monthly, weekly, and daily time periods. For example, requesting published statistics for corn in Virginia for years greater than or equal to 2010 would be:

`http://quickstats.nass.usda.gov/api/api_GET/?key=apikey&commodity_desc=CORN&year__GE=2010&state_alpha=VA` 

Full Documentation, a Data Dictionary, and API Registration can be found [here](https://quickstats.nass.usda.gov/api).

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

## Integrated Public Use Microdata Series

IPUMS is not a collection of compiled statistics; it is composed of microdata. Each record is a person, with all characteristics numerically coded. In most samples persons are organized into households, making it possible to study the characteristics of people in the context of their families or other co-residents. Because the data are individuals and not tables, researchers must use a statistical package to analyze the millions of records in the database. A data extraction system enables users to select only the samples and variables they require. Data is received in a gzip file.
Data that is used for publicatoin must be cited. The IPUMS download portal yields a data file as well as command files for SAS, SPSS, Stata, and R. Researchers using R are recommended to use the `Ipumsr` package.

**Helpful Links:**
- [Downloading data](https://usa.ipums.org/usa/resources/instruct.pdf)
- [Data sample](https://usa.ipums.org/usa/data_example.html)
- [FAQ](https://usa.ipums.org/usa-action/faq)
- [Must Create an account](https://uma.pop.umn.edu/usa/user/new?return_url=https%3A%2F%2Fusa.ipums.org%2Fusa-action%2Fextract_requests%2Fdownload)

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>



## Food Environment Atlas (USDA)

The current version of the Food Environment Atlas has over 275 variables, including new indicators on access and proximity to a grocery store for sub populations; an indicator on the SNAP Combined Application Project for recipients of Supplemental Security Income (at the State level); and indicators on farmers' markets that report accepting credit cards or report selling baked and prepared food products. All of the data included in the Atlas are aggregated into an Excel spreadsheet for easy download. These data are from a variety of sources and cover varying years and geographic levels. The documentation for each version of the data provides complete information on definitions and data sources, and can be found [here](https://www.ers.usda.gov/webdocs/DataFiles/80526/archived_documentation_August2015.pdf?v=0)

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>


## Feed Grains: Yearbook Tables (USDA)

This data product provided by the USDA contains statistics on four main feed grains - corn, grain sorghum, barley, and oats - as well as foreign coarse grains such as rye, millet, hay, and related items. This includes data published in the monthly Feed Outlook and previously annual Feed Yearbook. Data are monthly, quarterly, and/or annual depending upon the data series.

Latest data may be preliminary or projected. Missing values indicate unreported values, discontinued series, or not yet released data. It is available in a bulk download from [here]( https://www.ers.usda.gov/data-products/feed-grains-database/feed-grains-yearbook-tables.aspx).

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

## Energy Information Administration API

The U.S. Energy Information Administration has its data free and open through an API, bulk file download, Excel / Google Sheets add-ons, and pluggable online widgets. EIA's API contains the datasets centered around hourly electricity operations, state energy systems, petroleum products, crude imports, natural gas, coal, international energy, and short-term and annual energy outlook. While the API is offered as a free public service, registration is required. The EIA also provides: 
- [API Terms of Service Agreement](https://www.eia.gov/opendata/register.cfm#terms_of_service)
- [Copyrights and Reuse](https://www.eia.gov/about/copyrights_reuse.cfm)
- [Full Documentation](https://www.eia.gov/opendata/commands.php)

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

## College ScoreCard API

This API makes all data available from the Department of Education’s College Scorecard, as well as supporting data on student completion, debt and repayment, earnings, and more. The files include data from 1996 through 2016 for all undergraduate degree-granting institutions of higher education. Data includes institution level characteristic such as average cost of attendance and retention rates for first-time students, as well as student characteristics such as student body by ethnicity and age. 
The full documentation and data dictionary can be found at [here](https://collegescorecard.ed.gov/data/documentation/).

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

## City of Boston
Analyze Boston is the City of Boston's open data hub to find facts, figures, and maps related to our lives within the city. We are working to make this the default technology platform to support the publication of the City's public information, 
in the form of [data](https://data.boston.gov/pages/glossary), and to make this information easy to find, access, and use by a broad audience. This platform is managed by the [Citywide Analytics Team](https://www.boston.gov/departments/analytics-team). 

Each dataset from Analyze Boston typically has metadata and relevant information. For example, [this dataset from ParkBoston](https://data.boston.gov/dataset/park-boston-monthly-transactions-by-zone-2015).

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>


## Bureau of Labor Statistics'  API

The BLS Public Data API gives the public access to economic data from all BLS programs, such as the Consumer Price Index. The API is currently available in two versions, the most recent requiring registration and allows users to access more data more frequently. Both versions return data from published historical time series data in json or xlsx format.
The data sources available to this API are extensive - covering employment, inflation, spending, pay and more. Knowledge of data series’ codes and formats is necessary for successful use of the API, and ID formats can be found [here](https://www.bls.gov/help/hlpforma.htm). Additionally, the full documentation can be found [here](https://www.bls.gov/developers/home.htm)

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}
<br>
<br>
<br>

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

## TSA API
The MyTSA Web Service API supports several features, some of which include: Security Checkpoint Wait Times, TSA Pre-Check locations, and Sunrise/Sunset times for all locations. 
Data can be queried by state and/or airport. The TSA provides XML files of data in addition to the API with [documentation](https://www.dhs.gov/mytsa-api-documentation).

### Example in Python
{% highlight python %}
print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
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
