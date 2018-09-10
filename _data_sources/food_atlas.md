---
title: Food Environment Atlas (USDA)
tag: Nutrition
---
The current version of the Food Environment Atlas has over 275 variables, including new indicators on access and proximity to a grocery store for sub populations; an indicator on the SNAP Combined Application Project for recipients of Supplemental Security Income (at the State level); and indicators on farmers' markets that report accepting credit cards or report selling baked and prepared food products. 
All of the data included in the Atlas are aggregated into an Excel spreadsheet for [easy download](https://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads/). 
These data are from a variety of sources and cover varying years and geographic levels. The [documentation](https://www.ers.usda.gov/webdocs/DataFiles/80526/archived_documentation_August2015.pdf?v=0) for each version of the data provides complete information on definitions and data sources.

<button data-toggle="collapse" data-target="#food-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="food-python" class="collapse">
{% highlight python %}
import pandas as pd

# After downloading the excel file.
df = pd.read_excel('August2015.xls', sheet_name='PRICES_TAXES')

# See the 10 counties with the highest soda price.
df.sort_values('SODA_PRICE10'
         , ascending=False).head(10)[['State', 'County', 'SODA_PRICE10']]
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#food-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="food-r" class="collapse">
{% highlight r %}
library(xlsx)

# After downloading the excel file.
df <- read.xlsx("August2015.xls", sheetName = "PRICES_TAXES")

# See the 10 counties with the highest soda price.
head(df[order(df$SODA_PRICE10, decreasing = TRUE)
  , c("State", "County", "SODA_PRICE10")], 10)
{% endhighlight %}
</div>
