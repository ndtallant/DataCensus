---
title: Feed Grains' Yearbook Tables (USDA)
tag: Agriculture
---
This data product provided by the USDA contains statistics on four main feed grains - corn, grain sorghum, barley, and oats - as well as foreign coarse grains such as rye, millet, hay, and related items. This includes data published in the monthly Feed Outlook and previously annual Feed Yearbook. Data are monthly, quarterly, and/or annual depending upon the data series.

Latest data may be preliminary or projected. Missing values indicate unreported values, discontinued series, or not yet released data. It is available in a bulk download from [here](https://www.ers.usda.gov/data-products/feed-grains-database/feed-grains-yearbook-tables.aspx).

<button data-toggle="collapse" data-target="#feed-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="feed-python" class="collapse">
{% highlight python %}
import pandas as pd

df = pd.read_excel('Feed Grains Yearbook Tables-Recent.xls'
    , sheet_name='FGYearbookTable01'
    , skiprows=[0, 1, 38, 39, 40, 41]
    , names=['commodity', 'year', 'planted', 'harvested', 'production', 'yield', 'price', 'loan_rate']
    , header=None)
df.dropna(how='all', inplace=True)
df.commodity.fillna(method='ffill', inplace=True)
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#feed-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="feed-r" class="collapse">
{% highlight r %}

{% endhighlight %}
</div>
