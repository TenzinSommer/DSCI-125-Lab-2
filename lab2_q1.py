import pandas as pd

df = pd.read_csv("car_stopping_distance.csv")
df = df.dropna()
df = df.iloc[0:10]

out = pd.DataFrame(columns=["result", "value"])
out.loc[0] = ["min_reaction_time", df["reaction_time"].min()]
out.loc[1] = ["max_reaction_time", df["reaction_time"].max()]
out.loc[2] = ["min_speed", df["speed"].min()]
out.loc[3] = ["max_speed", df["speed"].max()]
out.loc[4] = ["avg_stop_distance", df["stop_distance"].mean()]

out.to_csv(path_or_buf="./q1_answer.csv", index= False)