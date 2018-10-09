---
title: General Social Survey (GSS)
tag: Social Science
anchor: general_social_survey
---

http://gss.norc.org/About-The-GSS

<button data-toggle="collapse" data-target="#gss-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="gss-python" class="collapse">
{% highlight python %}
import pandas as pd
# Download Variables of interest from data portal
# You can load the data file like any text file
df = pd.read_table('default.dat')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#gsss-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="gss-r" class="collapse">
{% highlight r %}
# Download Variables of interest from data portal
# You can load the data file like any text file
df <- pd.read_table("default.dat")
{% endhighlight %}
</div>
