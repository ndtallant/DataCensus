library(readr)
library(dplyr)
library(ggplot2)

# Flat file downloaded from:
# http://apps.who.int/gho/data/view.main.REGION2480A?lang=en

data <- read_csv('obesity.csv')

by.region <- data %>%
  group_by(REGION, YEAR) %>%
  summarize(mean.Numeric = mean(Numeric)/100)

ggplot(by.region, aes(x = YEAR, y = mean.Numeric, color = REGION)) +
  geom_point() +
  geom_line() +
  ggtitle('Obesity Rates Over Time', subtitle = 'Grouped By Region') +
  ylab('Average Obesity Rate')