---
title:  City of Boston
tag: Municipal Government
---
Analyze Boston is the City of Boston's open data hub to find facts, figures, and maps related to our lives within the city. We are working to make this the default technology platform to support the publication of the City's public information, 
in the form of [data](https://data.boston.gov/pages/glossary), and to make this information easy to find, access, and use by a broad audience. This platform is managed by the [Citywide Analytics Team](https://www.boston.gov/departments/analytics-team). 

Each dataset from Analyze Boston typically has metadata and relevant information. For example, [this dataset from ParkBoston](https://data.boston.gov/dataset/park-boston-monthly-transactions-by-zone-2015).

<button data-toggle="collapse" data-target="#boston_python" type="button" class="btn btn-secondary btn-lg btn-block">Example in Python</button>
<div id="boston_python" class="collapse">
{% highlight python %}
import pandas as pd
df = pd.read_csv('park-boston-monthly-transactions-by-zone-2015.csv')

# Remove trailing whitespace in column names.
df.columns = [c.strip() for c in df.columns]

# See the 20 most used parking zones in January.
print(df.sort_values('January', ascending=False)['Zone Name'].head(20))

{% endhighlight %}
</div>

<button data-toggle="collapse" data-target="#boston_r" type="button" class="btn btn-secondary btn-lg btn-block">Example in R</button>
<div id="boston_r" class="collapse">
{% highlight r %}
df <- read.csv("park-boston-monthly-transactions-by-zone-2015.csv")

# See the 20 most used parking zones in January.
head(df$Zone.Name[order(df$January), decreasing = TRUE], 20)
{% endhighlight %}
</div>
