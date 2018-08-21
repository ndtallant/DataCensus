import pandas as pd

df = pd.read_csv('atuscps_2017.dat')
by_state = df.GESTFIPS.value_counts(normalize=True).sort_index()

print('Share of observations by state (FIPS)')
print(by_state)
