---
title: Statistical Abstracts of the United States 
tag: Social Science
anchor: statistical_abstracts 
---
The *Statistical Abstract of the United States*, published from 1878 to 2012, is the authoritative and comprehensive summary of statistics on the social, political, and economic organization of the United States. It is designed to serve as a convenient volume for statistical reference, and as a guide to other statistical publications and sources both in print and on the Web. These sources of data include the U.S. Census Bureau, Bureau of Labor Statistics, Bureau of Economic Analysis, and many other Federal agencies and private organizations.

The documentation is segmented by year, and then separated into parts. For example, the documentation for 1994 can be found [here](https://www.census.gov/library/publications/1994/compendia/statab/114ed.html).

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
