---
title: College ScoreCard API
tag: Education
---
This API makes all data available from the Department of Education’s College Scorecard, as well as supporting data on student completion, debt and repayment, earnings, and more. The files include data from 1996 through 2016 for all undergraduate degree-granting institutions of higher education. Data includes institution level characteristic such as average cost of attendance and retention rates for first-time students, as well as student characteristics such as student body by ethnicity and age. 
The full documentation and data dictionary can be found at [here](https://collegescorecard.ed.gov/data/documentation/).

<button data-toggle="collapse" data-target="#college-python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="college-python" class="collapse">

{% highlight python %}
import requests

key = 'YOUR API KEY HERE'
base = ('https://api.data.gov/ed/collegescorecard/v1/'
        'schools?school.name=chicago&api_key=')

response = requests.get(base + key)
data = response.json()['results']

# See all schools in Chicago
for observation in data:
    print(observation['school']['name'])
{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#college-r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="college-r" class="collapse">

{% highlight r %}
library(httr)

key <- "YOUR API KEY HERE"
base <- paste("https://api.data.gov/ed/collegescorecard/v1/"
              , "schools?school.name=chicago&api_key="
              , sep = "")
response <- GET(paste(base, key, sep = ""))
data <- content(response, "parsed")[["results"]]

# See all schools in Chicago
for (observation in data) {
  print(observation[["school"]][["name"]])
}
{% endhighlight %}
</div>
