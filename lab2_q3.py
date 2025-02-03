import pandas as pd
import numpy as np

df = pd.read_csv("car_stopping_distance.csv")
df = df.dropna()

df["speed"] = df["speed"].apply(lambda x: round(float(x) * 0.277778, 2))
df["slope"] = df["slope"].apply(lambda x: round(np.tan(float(x)/180 * np.pi), 2))

tire_coe = pd.DataFrame({"tire_type": ["passenger", "performance"], "tire_type_coe": [1.0, 1.1]})
# tire_coe["tire_type"] = None
# tire_coe["tire_type_coe"] = None
# tire_coe.loc[0] = ["passenger", 1.0]
# tire_coe.loc[1] = ["performance", 1.1]

road_coe = pd.DataFrame({"road_type": ["summer", "dry", "wet"], "road_type_coe": [.9, .7, .4]})
# road_coe["road_type"] = None
# road_coe["road_type_coe"] = None
# road_coe.loc[0] = ["summer", .9]
# road_coe.loc[1] = ["dry", .7]
# road_coe.loc[2] = ["wet", .4]

df = df.merge(tire_coe, on=["tire_type"]).merge(road_coe, on=["road_type"])

print(df)

df.to_csv(path_or_buf="./q3_answer.csv", index= False)