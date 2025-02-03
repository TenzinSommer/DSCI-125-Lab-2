import pandas as pd

# make new float column called 'est_stop_distance', float with 2 decimal places
# convert and round speed and slope values with series functions
# make new str column called 'distance_compare' which shows if the 'stop_distance' is 
# shorter or longer than the 'est_stop_distance'

df = pd.read_csv('q3_answer.csv')

df['est_stop_distance'] = round((df['reaction_time'] * df['speed']) + df['speed'] ** 2 / (2 * 9.8 * (df['slope'] + df['road_type_coe']) * df['tire_type_coe']), 2)

distance_compare = []

for index, row in df.iterrows():
    if row['est_stop_distance'] == row['stop_distance']:
        distance_compare.append('equal')
    elif row['est_stop_distance'] > row['stop_distance']:
        distance_compare.append('shorter')
    else:
        distance_compare.append('longer')

df['distance_compare'] = distance_compare
print(df)

