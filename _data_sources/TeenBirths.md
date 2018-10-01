---
title:  US and State Trends on Teen Births (NCHS)
tag: Healthcare Policy
---
This [dataset](https://data.cdc.gov/NCHS/NCHS-U-S-and-State-Trends-on-Teen-Births/y268-sna3) assembles all final birth data for females aged 15–19, 15–17, and 18–19 for the United States and each of the 50 states. This particular dataset notes the year, state, age of mother, and relevant birthrates for 4,212 observations. 

Documentation on the latest version of this dataset provides complete information on variables, data sources, dataset identifier, definitions, and classifications can be found at the API docs [here](https://dev.socrata.com/foundry/data.cdc.gov/sgfp-ytm5)

<button data-toggle="collapse" data-target="#TeenBirths-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="TeenBirths-python" class="collapse">
{% highlight python %}
import pandas as pd
# Observations where the state teen birth rate is 37.5 %
df = pd.read_json('https://data.cdc.gov/resource/sgfp-ytm5.json?$where=state_rate=37.5')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#TeenBirths-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="TeenBirths-r" class="collapse">
{% highlight r %}
library(RSocrata)
df <- read.socrata('https://data.cdc.gov/resource/sgfp-ytm5.json?$where=state_rate=37.5')
{% endhighlight %}
</div>
