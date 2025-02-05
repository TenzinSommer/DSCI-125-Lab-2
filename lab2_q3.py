import pandas as pd
import numpy as np

df = pd.read_csv("car_stopping_distance.csv")
df = df.dropna()

df["speed"] = df["speed"].apply(lambda x: round(float(x) * 0.277778, 2))
df["slope"] = df["slope"].apply(lambda x: round(np.tan(float(x)/180 * np.pi), 2))

tire_coe = pd.DataFrame({"tire_type": ["summer", "passenger", "performance"], "tire_type_coe": [.9, 1.0, 1.1]})
road_coe = pd.DataFrame({"road_type": ["dry", "wet"], "road_type_coe": [.7, .4]})

df = df.merge(road_coe, on=["road_type"], how="left")
df = df.merge(tire_coe, on=["tire_type"], how="left")


df.to_csv(path_or_buf="./q3_answer.csv", index= False)