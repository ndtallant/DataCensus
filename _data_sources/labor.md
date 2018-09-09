---
title: Bureau of Labor Statistics'  API
tag: Economic
---
The BLS Public Data API gives the public access to economic data from all BLS programs, such as the Consumer Price Index. The API is currently available in two versions, the most recent requiring registration and allows users to access more data more frequently. Both versions return data from published historical time series data in json or xlsx format.
The data sources available to this API are extensive - covering employment, inflation, spending, pay and more. Knowledge of data series’ codes and formats is necessary for successful use of the API, and ID formats can be found [here](https://www.bls.gov/help/hlpforma.htm). Additionally, the full documentation can be found [here](https://www.bls.gov/developers/home.htm)

<button data-toggle="collapse" data-target="#labor-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="labor-python" class="collapse">
{% highlight python %}
import pandas as pd
print("Hello, World")
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#labor-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="labor-r" class="collapse">
{% highlight r %}
print("Hello, World")
{% endhighlight %}
</div>
