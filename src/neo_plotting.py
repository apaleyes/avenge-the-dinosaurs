import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('neo_api_data.csv')

print(df[df["is_potentially_hazardous_asteroid"] == True].shape)
print(df[df["is_potentially_hazardous_asteroid"] == False].shape)

fig, ax = plt.subplots()

df[df["is_potentially_hazardous_asteroid"] == True].plot(kind='scatter', x='epoch_osculation', y='ascending_node_longitude', marker='o', color='blue', ax=ax)
df[df["is_potentially_hazardous_asteroid"] == False].plot(kind='scatter', x='epoch_osculation', y='ascending_node_longitude', marker='x', color='red', ax=ax)

plt.show()
