import pandas as pd

def main():
	indiana_df = pd.read_csv('gsod.obs_indiana.csv')
	series = indiana_df[indiana_df['measure_id'] == 9].values
	print(series)
	series = [i for i in series if i[4] == 127.4]
	print(series)

main()
