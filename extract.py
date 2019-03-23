import pandas as pd

def read_data(filename):
	df = pd.read_csv(filename, nrows=1E6, usecols=[0,2,3,4,5])
	return df

df = read_data('gsod.obs.csv')
for index, row in df.iterrows():
	if row['']
print(df)
