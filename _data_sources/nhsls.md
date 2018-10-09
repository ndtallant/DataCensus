---
title: National Health and Social Life Survey, 1992 
tag: Social Science
anchor: NHSLS 
---

The purpose of this study was to collect extensive information on the sexual experiences and other social, demographic, attitudinal, and health-related characteristics of adults in the United States. The survey collected information on sexual practices with spouses/cohabitants and other sexual partners and collected background information about the partners. Major areas of investigation include sexual experiences such as number of sexual partners in given time periods, frequency of particular practices, and timing of various sexual events. The data cover childhood and adolescence, as well as adulthood. Other topics in the survey relate to sexual victimization, marriage and cohabitation, and fertility. Respondents were also queried about their physical health, including history of sexually transmitted diseases. Respondents' attitudes toward premarital sex, the appeal of particular practices such as oral sex, and levels of satisfaction with particular sexual relationships were also studied. Demographic items include race, education, political and religious affiliation, income, and occupation.

The codebook can be found [here](https://www.icpsr.umich.edu/icpsrweb/HMCA/studies/6647/datadocumentation#).

<button data-toggle="collapse" data-target="#nhsls-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="nhsls-python" class="collapse">
{% highlight python %}
import pandas as pd
# Download Variables of interest from data portal
# You can load the data file like any text file
df = pd.read_table('default.dat')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#nhsls-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="nhsls-r" class="collapse">
{% highlight r %}
# Download Variables of interest from data portal
# You can load the data file like any text file
df <- pd.read_table("default.dat")
{% endhighlight %}
</div>
