---
title: USDA National Agricultural Statistics Service API
tag: Agriculture
---

This API provides access to data from the Census of Agriculture as well as national, state, and county level surveys. Data is queried through requesting commodities encapsulated in the sectors of Crops, Animals & Products, Economics, Demographics, and Environmental. The commodity statistics are aggregated for standard census geographies, agricultural statistics districts, and watershed boundaries over annual, seasonal, monthly, weekly, and daily time periods. 

Full Documentation, a Data Dictionary, and API Registration can be found [here](https://quickstats.nass.usda.gov/api).
<button data-toggle="collapse" data-target="#nass-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="nass-python" class="collapse">
{% highlight python %}
import requests
import pandas as pd

key = 'your_api_key'

# Observations for corn in Virginia in 2010
url = 'http://quickstats.nass.usda.gov/api/api_GET/?key={}&\
       commodity_desc=CORN&year__GE=2010&state_alpha=VA'

response = requests.get(url.format(key))
data = response.json()
df = pd.DataFrame(data['data'])
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#nass-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="nass-r" class="collapse">
{% highlight r %}
library(jsonlite)

key <- "your_api_key"

# Observations for corn in Virginia in 2010
url <- paste("http://quickstats.nass.usda.gov/api/api_GET/?key="
           , key
           , "&commodity_desc=CORN&year__GE=2010&state_alpha=VA"
           , sep = "")

data <- fromJSON(url)
df <- data.frame(data)
{% endhighlight %}
</div>
