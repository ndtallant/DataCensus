---
title: National Study of Private Ownership of Firearms in the United States, 1994 
tag: Crime 
anchor: NSPOF 
---
This data collection consists of a survey of private ownership of firearms by adults in the United States. Respondents who both did and did not own firearms were included. The variables cover topics such as the number and type of guns owned privately, methods of, and reasons for, firearms acquisition, the storage and carrying of guns, the defensive use of firearms against criminal attackers, and reasons for and against firearm ownership. Basic demographic variables include sex, age, education, and employment. 

The full codebook can be viewed [here](https://www.icpsr.umich.edu/icpsrweb/NACJD/studies/6955/datadocumentation#).

The public-use data files in this collection are available for access by the general public. Access does not require affiliation with an ICPSR member institution. However, an ICPSR login is still required to download the data itself.

<button data-toggle="collapse" data-target="#nspof-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="nspof-python" class="collapse">
{% highlight python %}
import pandas as pd
# Download Variables of interest from data portal
# You can load the data file like any text file
df = pd.read_table('default.dat')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#nspof-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="nspof-r" class="collapse">
{% highlight r %}
# Download Variables of interest from data portal
# You can load the data file like any text file
df <- pd.read_table("default.dat")
{% endhighlight %}
</div>
