---
title:  Drug Poisoning Mortality (NCHS)
tag: Healthcare
---

The National Center of Health Statistics publishes this data at the [county](https://data.cdc.gov/NCHS/NCHS-Drug-Poisoning-Mortality-by-County-United-Sta/pbkm-d27e) and [state](https://data.cdc.gov/NCHS/NCHS-Drug-Poisoning-Mortality-by-State-United-Stat/jx6g-fdh6) level as flat files and through an API. 
Each dataset describes drug poisoning deaths by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning from 1999 to 2015.
The county level dataset has 8 variables/columns and 53,387 rows, which are described in the [API Documentation](https://dev.socrata.com/foundry/data.cdc.gov/tenp-43rk). The state level dataset also has full [documentation](https://dev.socrata.com/foundry/data.cdc.gov/fqf8-qnrv) of its 18 variables/columns and 2,703 rows. 

<button data-toggle="collapse" data-target="#drug-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="drug-python" class="collapse">
{% highlight python %}
import pandas as pd

# Get all mortality levels for the state of Texas.
df = pd.read_json("https://data.cdc.gov/resource/tenp-43rk.json?st=TX")
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#drug-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="drug-r" class="collapse">
{% highlight r%}
library(RSocrata)

# Get all mortality levels for the state of Texas.
df <- read.socrata("https://data.cdc.gov/resource/tenp-43rk.json?st=TX")
{% endhighlight %}
</div>

