---
title:  US Death Rates and Life Expectancy at Birth (NCHS)
tag: Healthcare
---
This [dataset](https://data.cdc.gov/NCHS/NCHS-Death-rates-and-life-expectancy-at-birth/w9j2-ggv5) of U.S. mortality trends since 1900 highlights the differences in age-adjusted death rates and life expectancy at birth by race and sex. This particular dataset has 1,044 observations accounting for year, age, race, sex, average life expectancy in years, and mortality. 

The National Center for Healthcare Statistics provides this data as flatfiles and through a [well documented API](https://dev.socrata.com/foundry/data.cdc.gov/bgqx-uh4z).

<button data-toggle="collapse" data-target="#death_python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="death_python" class="collapse">
{% highlight python %}
import pandas as pd

df = pd.read_json('https://data.cdc.gov/resource/bgqx-uh4z.json')

# See Average Life Expectancy for All Races and Genders by Year
df[(df.race == 'All Races') & (df.sex == 'Both Sexes')][['average_life_expectancy', 'year']]
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#death_r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="death_r" class="collapse">
{% highlight r %}
library(RSocrata)

df <- read.socrata("https://data.cdc.gov/resource/bgqx-uh4z.json")

# See Average Life Expectancy for All Races and Genders by Year
df[df$race == "All Races" & df$sex == "Both Sexes", c("average_life_expectancy", "year")]
{% endhighlight %}
</div>
