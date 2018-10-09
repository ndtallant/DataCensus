---
title: Small Business Administration Survey (1992) 
tag: Economic 
anchor: small_business_administration_survey 
---

The Small Business Administration Survey records general charactersitics of small businesses in the United States, such as the number of employees, industry, number of locations, paid wages, etc. It also considers the demographic information of owners, such as marital status and ethnicity. The data provided below is for the year of 1992. 

[Survey 1 Download](https://harris.uchicago.edu/files/sbaraw-s1.dta)
| [Documentation](https://harris.uchicago.edu/files/sba-i-questionnaire.pdf)

[Survey 2 Download](https://harris.uchicago.edu/files/sbaraw-s2.dta)
| [Documentation](https://harris.uchicago.edu/files/sba-2-employer_survey.pdf)


<button data-toggle="collapse" data-target="#sba-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="sba-python" class="collapse">
{% highlight python %}
import pandas as pd
df = pd.read_table('sbaraw-s1.dta')
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#sba-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="sba-r" class="collapse">
{% highlight r %}
df <- pd.read_table("sbaraw-s1.dta")
{% endhighlight %}
</div>
