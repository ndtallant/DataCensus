---
title: Statistical Abstracts of the United States 
tag: Social Science
anchor: statistical_abstracts 
---

The Statistical Compendia program is comprised of the Statistical Abstract of the United States and its supplemental products—the State and Metropolitan Area Data Book and the County and City Data Book, however, the program was discontinued in October 1, 2011. 

https://www.census.gov/library/publications/time-series/statistical_abstracts.html

<button data-toggle="collapse" data-target="#stat_abs-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="stat_abs-python" class="collapse">
{% highlight python %}
import pandas as pd
# Download Variables of interest from data portal
# You can load the data file like any text file
df = pd.read_table('default.dat')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#stat_abs-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="stat_abs-r" class="collapse">
{% highlight r %}
# Download Variables of interest from data portal
# You can load the data file like any text file
df <- pd.read_table("default.dat")
{% endhighlight %}
</div>
