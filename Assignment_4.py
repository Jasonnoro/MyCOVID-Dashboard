import pandas as pd

#Load CSV with pandas; parse dates; show head(), info()
df=pd.read_csv("COVID_Country_Sample.csv",parse_dates=['date'])

print(df.head())
df.info()

#Handle missing values (e.g., fillna or drop) and mild outliers (justify method)
df['new_vaccinations']=df['new_vaccinations'].fillna(0)

'''
-> Justification: Chose to fill the 'new_vaccinations' with the default value 0, since missing 
entries likely indicate no vaccination records for this date. 
-> Sensible to fill the value rather than dropping as it avoids removing rows and preserves the dataset.
-> However, this data may introduce bias, if missing records do not truly represent 0 vaccinations. 
-> The data solely focuses on COVID cases and vaccinations received so far.
'''
df.to_csv("cleaned_covid_data.csv", index=False)

#Create monthly aggregates if needed and compute rolling means
df['month'] = df['date'].dt.to_period('M')
monthly = df.groupby('month')['new_vaccinations'].sum()

df = df.sort_values(['country', 'date'])

df['rolling_avg'] = df.groupby('country')['new_vaccinations'] \
                     .transform(lambda x: x.rolling(window=7).mean())



