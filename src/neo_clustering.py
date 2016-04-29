import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

df = pd.read_csv('neo_api_data.csv')

df['average_diameter'] = (df['estimated_diameter_min'] + df['estimated_diameter_max'])/2.0
columns = [
    # "absolute_magnitude_h",
    "average_diameter",
    # "minimum_orbit_intersection",
    "jupiter_tisserand_invariant",
    "epoch_osculation",
    "eccentricity",
    "semi_major_axis",
    "inclination",
    "ascending_node_longitude",
    "orbital_period",
    "perihelion_distance",
    "perihelion_argument",
    "aphelion_distance",
    "perihelion_time",
    "mean_anomaly",
    "mean_motion"
]

data_df = df[columns]
labels = df["is_potentially_hazardous_asteroid"]

data = pd.DataFrame(scale(data_df))

# PCA
pca_data = PCA(n_components=2).fit_transform(data)
result_df = pd.DataFrame(pca_data)
result_df[2] = data[14]
result_df["pha"] = df["is_potentially_hazardous_asteroid"]

# KMeans
clusterator = KMeans(init='k-means++', n_clusters=3, n_init=10)
clusterator.fit(data)
clusters = clusterator.predict(data)
result_df["cluster"] = clusters

# Color code by cluster, marker code by PHA flag
categories = np.unique(result_df["cluster"])
colors = np.linspace(0, 1, len(categories))
colordict = dict(zip(categories, colors))  
result_df["color"] = result_df["cluster"].apply(lambda x: colordict[x])

fig, ax = plt.subplots()
xv = 0
yv = 2
for c in colors:
    pha_df = result_df[(result_df["pha"] == True) & (result_df["color"] == c)]
    if not pha_df.empty:
        ax.scatter(pha_df[xv], pha_df[yv], marker='s', s=200, c=cm.hot(c))
        # uncomment to get the label for the PHA asteroid
        # for i, row in pha_df.iterrows():
        #     ax.annotate(df['neo_reference_id'][i], xy=row[[xv, yv]], textcoords='data')
        # pha_df.plot(kind='scatter', x=xv, y=yv, marker='x', markersize=20, color=cm.hot(c), ax=ax)

    non_pha_df = result_df[(result_df["pha"] == False) & (result_df["color"] == c)]
    if not non_pha_df.empty:
        ax.scatter(non_pha_df[xv], non_pha_df[yv], marker='o', c=cm.hot(c))
        # non_pha_df.plot(kind='scatter', x=xv, y=yv, marker='o', color=cm.hot(c), ax=ax)


# 2D
# fig, ax = plt.subplots()
# result_df[(result_df["pha"] == True)].plot(kind='scatter', x=1, y=2, marker='x', color='r', ax=ax)
# result_df[(result_df["pha"] == False)].plot(kind='scatter', x=1, y=2, marker='o', color='b', ax=ax)


# 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# pha_df = result_df[(result_df["pha"] == True)]
# non_pha_df = result_df[(result_df["pha"] == False)]
# ax.scatter(pha_df[0], pha_df[1], pha_df[2], marker='x', c='r')
# ax.scatter(non_pha_df[0], non_pha_df[1], non_pha_df[2], marker='o', c='b')

plt.show()