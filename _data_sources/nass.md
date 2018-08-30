---
title: USDA National Agricultural Statistics Service API
tag: agriculture
---

This API provides access to data from the Census of Agriculture as well as national, state, and county level surveys. Data is queried through requesting commodities encapsulated in the sectors of Crops, Animals & Products, Economics, Demographics, and Environmental. The commodity statistics are aggregated for standard census geographies, agricultural statistics districts, and watershed boundaries over annual, seasonal, monthly, weekly, and daily time periods. For example, requesting published statistics for corn in Virginia for years greater than or equal to 2010 would be:

`http://quickstats.nass.usda.gov/api/api_GET/?key=apikey&commodity_desc=CORN&year__GE=2010&state_alpha=VA` 

Full Documentation, a Data Dictionary, and API Registration can be found [here](https://quickstats.nass.usda.gov/api).

### Example in Python
{% highlight python %}
import requests
import numpy as np
import pandas as pd

url = 'http://quickstats.nass.usda.gov/api/api_GET/?key=apikey&\
       commodity_desc=CORN&year__GE=2010&state_alpha=VA'

print("Hello, World")
{% endhighlight %}

### Example in R
{% highlight r %}
print("Hello, World")
{% endhighlight %}