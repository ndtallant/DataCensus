---
title:  US Injury Mortality (NCHS)
tag: Healthcare Policy
---
This [dataset](https://data.cdc.gov/NCHS/NCHS-Injury-Mortality-United-States/nt65-c7a7) describes injury mortality in the United States beginning in 1999. Two concepts are included in the circumstances of an injury death: intent of injury and mechanism of injury. This particular dataset has 17 variables/columns and 98,280 rows. Using filters and SoQL queries, researcher can search for records, limit results, and adjust the way the data is output

All of the data are aggregated into a CSV or CSV for Excel spreadsheet for easy download. 

Documentation on the latest version of this dataset provides complete information on variables, data sources, dataset identifier, definitions, and classifications can be found at the API docs [here](https://dev.socrata.com/foundry/data.cdc.gov/6j4j-ispt)

<button data-toggle="collapse" data-target="#InjuryMortality-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="InjuryMortality-python" class="collapse">
{% highlight python %}
import pandas as pd

# Get all injury mechanisms for mortality in the United States 
df = pd.read_json("https://data.cdc.gov/resource/6j4j-ispt.json")
{% endhighlight %}
</div>


<button data-toggle="collapse" data-target="#InjuryMortality-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="InjuryMortality-r" class="collapse">
{% highlight r %}
library(RSocrata)


# Get all injury mechanisms for mortality in the United States 
df <- read.socrata("https://data.cdc.gov/resource/6j4j-ispt.json")
{% endhighlight %}
</div>
