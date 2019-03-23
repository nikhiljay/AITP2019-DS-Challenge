import geopandas as gpd

map_df = gpd.read_file('tl_2013_18_cousub.shp')
print(map_df.head())
