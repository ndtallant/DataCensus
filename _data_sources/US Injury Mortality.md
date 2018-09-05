---
title:  US Injury Mortality (NCHS)
tag: Healthcare Policy
---
This [dataset](https://data.cdc.gov/NCHS/NCHS-Injury-Mortality-United-States/nt65-c7a7) describes injury mortality in the United States beginning in 1999. Two concepts are included in the circumstances of an injury death: intent of injury and mechanism of injury. This particular dataset has 17 variables/columns and 98,280 rows. Each column is represented by a single field in its SODA API. Using filters and SoQL queries, researcher can search for records, limit results, and adjust the way the data is output

All of the data are aggregated into a CSV or CSV for Excel spreadsheet for easy download. Additional formats for download also include RDF, RSS, TSV for Excel, and XML.

Documentation on the latest version of this dataset provides complete information on variables, data sources, dataset identifier, definitions, and classifications can be found at the API docs [here](https://dev.socrata.com/foundry/data.cdc.gov/6j4j-ispt)

All communication with the API is done through HTTPS, and errors are communicated through HTTP response codes. Available response types include JSON, XML, and CSV, which are selectable by the "extension" (.json, etc.) on the API endpoint or through content-negotiation with HTTP Accepts headers.
