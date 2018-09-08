---
title: Energy Information Administration API
tag: Energy
---

The U.S. Energy Information Administration has its data free and open through an API, bulk file download, Excel / Google Sheets add-ons, and pluggable online widgets. EIA's API contains the datasets centered around hourly electricity operations, state energy systems, petroleum products, crude imports, natural gas, coal, international energy, and short-term and annual energy outlook. While the API is offered as a free public service, registration is required. The EIA also provides: 
- [API Terms of Service Agreement](https://www.eia.gov/opendata/register.cfm#terms_of_service)
- [Copyrights and Reuse](https://www.eia.gov/about/copyrights_reuse.cfm)
- [Full Documentation](https://www.eia.gov/opendata/commands.php)

### Example in Python
{% highlight python %}
import requests
import pandas

# See MMBtu by year for the plant in Tracy, Nevada.
url = ('http://api.eia.gov/series/?api_key=YOUR_API_KEY&'
       'series_id=ELEC.PLANT.CONS_EG_BTU.2336-ALL-ALL.A')
response = requests.get(url)
info = response.json()

df = pd.DataFrame(info['series'][0]['data'], columns=['Year', 'MMBtu'])

{% endhighlight %}

### Example in R
{% highlight r %}
library(httr)
library(purrr)
# See MMBtu by year for the plant in Tracy, Nevada.
url <- paste("http://api.eia.gov/series/?api_key="
            , "YOUR_API_KEY&"
            , "series_id=ELEC.PLANT.CONS_EG_BTU.2336-ALL-ALL.A"
            , sep = "")

response <- GET(url)
data <- content(response, "parsed")[["series"]][[1]][["data"]]
years <- unlist((transpose(data)[[1]]))
MMBtu <- unlist((transpose(data)[[2]]))
df <- data.frame(years, MMBtu)
{% endhighlight %}
