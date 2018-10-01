---
title:  US Leading Causes of Death (NCHS)
tag: Healthcare Policy
---
This [dataset](https://data.cdc.gov/NCHS/NCHS-Leading-Causes-of-Death-United-States/bi63-dtpu) presents the age-adjusted death rates for the 10 leading causes of death in the United States beginning in 1999. This particular dataset has 10,296 observations describing the year, state, cause of death, number of deaths, and age adjusted death rate. Documentation on the latest version of this dataset provides complete information on variables, data sources, dataset identifier, definitions, and classifications can be found at the API docs [here](https://dev.socrata.com/foundry/data.cdc.gov/u4d7-xz8k)

<button data-toggle="collapse" data-target="#LeadingCausesOfDeath-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="LeadingCausesOfDeath-python" class="collapse">
{% highlight python %}
import pandas as pd
# All records for the state of Alabama
df = read_json('https://data.cdc.gov/resource/u4d7-xz8k.json?state=Alabama')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#LeadingCausesOfDeath-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="LeadingCausesOfDeath-r" class="collapse">
{% highlight r %}
library(RSocrata)
# All records for the state of Alabama
df <- read.socrata("https://data.cdc.gov/resource/u4d7-xz8k.json?state=Alabama")
{% endhighlight %}
</div>
