---
title: American Time Use Survey
tag: Economic
---

Researchers can produce their own time-use estimates using the ATUS microdata files. The ATUS data files include information for over 190,000 respondents total from 2003 to 2017. Because of the size of these data files, it is easiest to work with them using statistical software such as Stata, SAS, or SPSS.

The survey is sponsored by the Bureau of Labor Statistics and is conducted by the U.S. Census Bureau.

The major purpose of ATUS is to develop nationally representative estimates of how people spend their time. The survey also provides information on the amount of time people spend in many other activities, such as religious activities, socializing, exercising, and relaxing. Demographic information such as sex, race, age, educational attainment, etc. is also available for each respondent.

[Microdata](https://www.bls.gov/tus/data.htm) 
 | [Data Dictionary](https://www.bls.gov/tus/atuscpscodebk17.pdf) 
 | [User Guide](https://www.bls.gov/tus/atususersguide.pdf)

### Example in Python
{% highlight python %}
import pandas as pd

mapping = {1: 'New England'
         , 2: 'Middle Atlantic'
         , 3: 'East North Central'
         , 4: 'West North Central'
         , 5: 'South Atlantic'
         , 6: 'East South Central'
         , 7: 'West South Central'
         , 8: 'Mountain'
         , 9: 'Pacific'}

df = pd.read_table('atuscps_2017.dat', delimiter=',')
df['division'] = df['GEDIV'].map(mapping)

# See number of housing units by geographic division.
print(pd.crosstab(df.division, df.HEHOUSUT))
{% endhighlight %}

### Example in R
{% highlight r %}
df <- read.csv("atuscps_2017.dat")
df$GEDIV <- factor(df$GEDIV)
levels(df$GEDIV) <- c("New England"
                     ,  "Middle Atlantic"
                     ,  "East North Central"
                     ,  "West North Central"
                     ,  "South Atlantic"
                     ,  "East South Central"
                     ,  "West South Central"
                     ,  "Mountain"
                     ,  "Pacific")

# See number of housing units by geographic division.
table(df$GEDIV, df$HEHOUSUT)
{% endhighlight %}

