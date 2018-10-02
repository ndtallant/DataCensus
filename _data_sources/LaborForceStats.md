---
title: Labor Force Statistics (CPS) 
tag: Economic 
parent: CPS
---

This data set comes from the Current Population Survey (CPS), a monthly survey of households conducted by the Bureau of Census for the Bureau of Labor Statistics. This large dataset has data for the years 1995-1999, as well as 2002-2017. All data is available in HTML, PDF, and XLSX flat formats, as well as through the Bureau of Labor Statistics [API](https://www.bls.gov/developers/home.htm).

The 57 data tables are grouped together in the following catagories: 
- <a href="https://www.bls.gov/cps/tables.htm#empstat">Employment status</a>
- <a href="https://www.bls.gov/cps/tables.htm#charemp">Characteristics of the employed</a>
- <a href="https://www.bls.gov/cps/tables.htm#charunem">Characteristics of the unemployed</a>
- <a href="https://www.bls.gov/cps/tables.htm#pnilf">Persons not in the labor force</a>
- <a href="https://www.bls.gov/cps/tables.htm#multjob">Multiple jobholders</a>
- <a href="https://www.bls.gov/cps/tables.htm#weekearn">Weekly earnings</a>
- <a href="https://www.bls.gov/cps/tables.htm#union">Union affiliation</a>
- <a href="https://www.bls.gov/cps/tables.htm#minimum">Minimum wage workers</a>
- <a href="https://www.bls.gov/cps/tables.htm#absences">Absences from work</a>
- <a href="https://www.bls.gov/cps/tables.htm#vets">Veteran status</a>
- <a href="https://www.bls.gov/cps/tables.htm#certs_licenses">Certification and licensing status</a>
 
A full list of tables and variables for the Current Population Survey can be found [here](https://www.bls.gov/cps/tables.htm).

<button data-toggle="collapse" data-target="#lfs_python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="lfs_python" class="collapse">
{% highlight python %}
import requests
import pandas as pd

# Seasonally Adjusted Unemployment Rate 
response = requests.get('https://api.bls.gov/publicAPI/v2/timeseries/data/LNS14000000') 
data = response.json()
df = pd.DataFrame(data['Results']['series'][0]['data'])
df.value = df.value.astype('float')

# See the average rate by year
print(df.groupby('year')['value'].mean())
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#lfs_r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="lfs_r" class="collapse">
{% highlight r %}
library(dplyr)
library(jsonlite)

# Seasonally Adjusted Unemployment Rate 
data <- fromJSON("https://api.bls.gov/publicAPI/v2/timeseries/data/LNS14000000") 
df <- data[["Results"]][["series"]][["data"]][[1]]
df$value <- as.numeric(df$value)

# See the average rate by year
df %>%
  group_by(year) %>%
  summarise(avg_rate = mean(value))
{% endhighlight %}
</div>
