---
title: Consumer Price Index (CPI) 
tag: Economic 
---
The Consumer Price Index (CPI) is a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services. Indexes are available for the U.S. and various geographic areas. Average price data for select utility, automotive fuel, and food items are also available. All [data](https://www.bls.gov/cpi/data.htm) is available in flat files and through the Bureau of Labor Statistics [API](https://www.bls.gov/developers/).

This large data set is segmented into four groups:
- All Urban Consumers (Current Series)
- Urban Wage Earners and Clerical Workers (Current Series)
- All Urban Consumers (Chained CPI)
- Average Price Data

<button data-toggle="collapse" data-target="#cpi_python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="cpi_python" class="collapse">
{% highlight python %}
import requests
import pandas as pd

# All items in U.S. city average, all urban consumers, seasonally adjusted
response = requests.get('https://api.bls.gov/publicAPI/v2/timeseries/data/CUSR0000SA0') 
data = response.json()
df = pd.DataFrame(data['Results']['series'][0]['data'])
df.value = df.value.astype('float')

# See the average price by year
print(df.groupby('year')['value'].mean())
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#cpi_r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="cpi_r" class="collapse">
{% highlight r %}
library(dplyr)
library(jsonlite)

# All items in U.S. city average, all urban consumers, seasonally adjusted
data <- fromJSON("https://api.bls.gov/publicAPI/v2/timeseries/data/CUSR0000SA0") 
df <- data[["Results"]][["series"]][["data"]][[1]]
df$value <- as.numeric(df$value)

# See the average price by year
df %>%
  group_by(year) %>%
  summarise(avg_rate = mean(value))
{% endhighlight %}
</div>
