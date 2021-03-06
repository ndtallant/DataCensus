---
title: TSA API
tag: Security
---

The MyTSA Web Service API supports several features, some of which include: Security Checkpoint Wait Times, TSA Pre-Check locations, and Sunrise/Sunset times for all locations.
Data can be queried by state and/or airport. The TSA provides XML files of data in addition to the API with [documentation](https://www.dhs.gov/mytsa-api-documentation).
<button data-toggle="collapse" data-target="#tsa-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="tsa-python" class="collapse">
{% highlight python %}
import requests
# Returns JSON file of today’s sunset time for DCA airport
response = requests.get('http://apps.tsa.dhs.gov/MyTSAWebService/GetEventInfo.ashx?eventtype=sunset&airportcode=DCA&output=json')
data = response.json()
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#tsa-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="tsa-r" class="collapse">
{% highlight r %}
library(jsonlite)
# Returns JSON file of today’s sunset time for DCA airport
data <- fromJSON('http://apps.tsa.dhs.gov/MyTSAWebService/GetEventInfo.ashx?eventtype=sunset&airportcode=DCA&output=json')
{% endhighlight %}
</div>
