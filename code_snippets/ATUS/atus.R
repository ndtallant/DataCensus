library(tidyverse)

data <- read.csv('atuscps_2017.dat')
data$PEIO1ICD <- as.character(data$PEIO1ICD)
by_region <- data %>%
  group_by(GEDIV, PEIO1ICD) %>%
  summarize(industry.count = count(PEIO1ICD)) 

