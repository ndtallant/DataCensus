---
title: FBI Crime Data API
tag: Crime
---
The FBI Crime Data API is a read-only web service that returns JSON or CSV data. It is broadly organized around the FBI’s Uniform Crime Reporting systems data, and requires a [data.gov API network](https://api.data.gov/docs) key. Agencies submit data using one of two reporting formats -- the Summary Reporting System (SRS), or the National Incident Based Reporting System (NIBRS). 

The FBI also provides [full documentation](https://crime-data-explorer.fr.cloud.gov/api) and [source code](https://github.com/fbi-cde).

<button data-toggle="collapse" data-target="#fbi_python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="fbi_python" class="collapse">
{% highlight python %}
import requests
import pandas as pd
base = 'https://api.usa.gov/crime/fbi/sapi/'
query = 'api/summarized/agencies/WY0200100/homicide?api_key='
key = 'your_api_key' 

# Homicides Recorded by Jackson Police Department
response = requests.get(base + query + key)
data = response.json()
df = pd.DataFrame(data['results'])
{% endhighlight %} 
</div>

<button data-toggle="collapse" data-target="#fbi_r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="fbi_r" class="collapse">
  
{% highlight R %}
library(jsonlite)
url <- paste("https://api.usa.gov/crime/fbi/sapi/"
            , "api/summarized/agencies/WY0200100/homicide?api_key="
            , "your_api_key" 
            , sep = "")

data <- fromJSON(url)
df <- data[["results"]]
{% endhighlight %}
</div> 
