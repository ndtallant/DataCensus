---
title: Labor Productivity and Costs (BLS) 
tag: Economic 
parent: BLS
---

Labor productivity is a measure of economic performance that compares the amount of goods and services produced (output) with the number of hours worked to produce those goods and services. The BLS also publishes measures of [multifactor productivity](https://www.bls.gov/mfp/). 

The [data](https://www.bls.gov/lpc/data.htm) is organized into two separate databases - Major Sector Productivity and Costs and Industry Productivity. Both databases are available as flat files and through the Bureau of Labor Statistics [API](https://www.bls.gov/developers/).

<button data-toggle="collapse" data-target="#lpc_python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="lpc_python" class="collapse">
{% highlight python %}
import requests
import pandas as pd

# Office of Productivity And Technology and Percent/Rate/Ratio and Productivity : Nonfarm Business
response = requests.get('https://api.bls.gov/publicAPI/v2/timeseries/data/PRS85006092') 
data = response.json()
df = pd.DataFrame(data['Results']['series'][0]['data'])
df.value = df.value.astype('float')

# See the rate change by quarter 
print(df.sort_values(['year', 'period'])[['year', 'period', 'value']])
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#lpc_r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="lpc_r" class="collapse">
{% highlight r %}
library(dplyr)
library(jsonlite)

# Office of Productivity And Technology and Percent/Rate/Ratio and Productivity : Nonfarm Business
data <- fromJSON("https://api.bls.gov/publicAPI/v2/timeseries/data/PRS85006092") 
df <- data[["Results"]][["series"]][["data"]][[1]]
df$value <- as.numeric(df$value)

# See the rate change by quarter 
print(df[order(df$year, df$period), c("year", "period", "value")])
{% endhighlight %}
</div>
