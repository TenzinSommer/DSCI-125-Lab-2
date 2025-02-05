import pandas as pd

# make new float column called 'est_stop_distance', float with 2 decimal places
# convert and round max_speed and slope values with series functions
# make new str column called 'distance_compare' which shows if the 'max_stop_distance' is 
# shorter or longer than the 'est_stop_distance'

df = pd.read_csv('q3_answer.csv')

df['est_stop_distance'] = round((df['reaction_time'] * df['speed']) + df['speed'] ** 2 / (2 * 9.8 * (df['slope'] + df['road_type_coe']) * df['tire_type_coe']), 2)

# distance_compare = []

# for index, row in df.iterrows():
#     if row['est_stop_distance'] == row['max_stop_distance']:
#         distance_compare.append('equal')
#     elif row['est_stop_distance'] > row['max_stop_distance']:
#         distance_compare.append('shorter')
#     else:
#         distance_compare.append('longer')

# df['distance_compare'] = distance_compare
def compare(est, actual):
	if est == actual: return 'equal'
	if est > actual: return 'shorter'
	return 'longer'

df["distance_compare"] = (df[["est_stop_distance", "stop_distance"]].apply(lambda x: compare(x["est_stop_distance"], x["stop_distance"]), axis=1))

# corr = pd.read_csv('q4_answer.csv')

# print(df == corr)

df.to_csv(path_or_buf="./q4_answer.csv", index= False)
