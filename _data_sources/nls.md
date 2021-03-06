---
title: National Longitudinal Surveys (NLS)
tag: Social Science
anchor: national_longitudinal_surveys
---
Information on the labor market activities and other significant life events of several groups of men and women at multiple points in time. For more than 4 decades, NLS data have served as an important tool for economists, sociologists, and other researchers.The NLS program includes the following cohorts :

- [NLS Youth 1997 (NLSY97)](https://www.nlsinfo.org/content/cohorts/nlsy97): Respondents were ages 12-17 when first interviewed in 1997. 
- [NLS Youth 1979 (NLSY79)](https://www.nlsinfo.org/content/cohorts/nlsy79): Respondents were ages 14-22 when first interviewed in 1979. 
- [NLSY79 Children and Young Adults](https://www.nlsinfo.org/content/cohorts/nlsy79-children): Assessments of biological children of women in the NLSY79, starting in 1986.
- [NLS Young and Mature Women (NLSW)](https://www.nlsinfo.org/content/cohorts/mature-and-young-women): Young women born in the years 1943-53 and mature women born in the years 1922-37. 
- [NLS Young and Older Men (NLSM)](https://www.nlsinfo.org/content/cohorts/older-and-young-men): Young men born in the years 1941-52 and older men born in the years 1906-21. 

The download functionality for these data sets provides access to files for SPSS, SAS, Stata, R, or simply a csv. A tagset, codebook, description file, and log file are also included with a download.

The R, SAS, and SPSS files contain code needed to load the data set, as well as short explanations for missing values and level names.
<button data-toggle="collapse" data-target="#nls-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="nls-python" class="collapse">
{% highlight python %}
import pandas as pd
# Download Variables of interest from data portal
# You can load the data file like any text file
df = pd.read_table('default.dat')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#nls-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="nls-r" class="collapse">
{% highlight r %}
# Download Variables of interest from data portal
# You can load the data file like any text file
df <- pd.read_table("default.dat")
{% endhighlight %}
</div>
