import pandas as pd

def read_data(filename):
	df = pd.read_csv(filename, usecols=[0,2,3,4,5])
	return df

def read_indiana(filename, indiana_stations):
	df = pd.read_csv(filename, skiprows=(lambda x:x not in indiana_stations))

df_stn = read_data('gsod.stn.csv')
print('read stations')
indiana_stations = df_stn[df_stn['state'] == 'IN']['station_id'].values
indiana_stations = [i for i in indiana_stations if i != '999999'] 

#df_obs = read_indiana('gsod.obs.csv', indiana_stations)
obs = open('gsod.obs.csv','r')
neq = open('gsod.obs_indiana.csv','w+')
obs.readline()
print(indiana_stations)
for line in obs:
	#print(line)
	if line[0:line.index(',')] in indiana_stations:
		print('read indiana',line)
		neq.write(line)
print('closing')
obs.close()
neq.close()
#print('read data',obslines)
#indiana_weather = df_obs[df_obs['station_id'] in indiana_stations]

#print(indiana_weather)
