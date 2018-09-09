---
title:  US Births and General Fertility Rates (NCHS)
tag: Healthcare
---

The National Center for Healthcare Statistics provides this data as flatfiles and through a [well documented API](https://dev.socrata.com/foundry/data.cdc.gov/tndt-s2gv).
The [dataset](https://data.cdc.gov/NCHS/NCHS-Births-and-General-Fertility-Rates-United-Sta/e6fc-ccez) includes crude birth rates and general fertility rates in the United States since 1909. This particular dataset has 107 observations accounting for year, birth number, crude birth rate, and general fertility rate. 


<button data-toggle="collapse" data-target="#births-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="births-python" class="collapse">
{% highlight python %}
import pandas as pd

# See all observations in 1909.
df = pd.read_json('https://data.cdc.gov/resource/tndt-s2gv.json?year=1909')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#births-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="births-r" class="collapse">
{% highlight r %}
library(RSocrata)

# See all observations in 1909.
df <- read.socrata("https://data.cdc.gov/resource/tndt-s2gv.json?year=1909")
{% endhighlight %}
</div>
