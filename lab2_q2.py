import pandas as pd

# get rid of rows with any missing values
# check each block of rows 10 rows long to find highest speed, largest stopping distance, number of 'dry' conditions
# save those values to 3 columns
# put them in one row in new csv file

# read csv and turn into dataframe
df = pd.read_csv("car_stopping_distance.csv")

# removes any row containing an empty space in any column
df = df.dropna()

# makes a new DF that holds the relevant values
newDF = pd.DataFrame({'max_stop_distance': [], 'max_speed': [], 'dry_count': []})

# checks every 10 rows and adds results to new DF 
for beg in range(0, len(df), 10):
    tempDF = df.iloc[beg:beg + 10][['stop_distance', 'speed', 'road_type']]
    
    dryCounter = 0
    for condition in tempDF['road_type']:
        if condition == 'dry':
            dryCounter += 1

    newDF.loc[len(newDF)] = [tempDF['stop_distance'].max(), tempDF['speed'].max(), dryCounter]

# typecasts newDF to correct results
newDF = newDF.astype({'max_stop_distance': float, 'max_speed': float, 'dry_count': int})
print(newDF)

# writes newDF to csv file
newDF.to_csv(path_or_buf = "./q2_answer.csv", index = False)