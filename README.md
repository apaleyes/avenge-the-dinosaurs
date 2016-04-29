# General Info

NASA defines a set of so-called Near Earth Objects (NEO), which is a set of all known comets and asteroids considered to be near Earth at some point of their orbits. More info here: http://neo.jpl.nasa.gov/neo/

From that set NASA also recognizes a subset of dangerous objects, so called Potentially Hazardous Asteroids, which consists of all NEA whose Minimum Orbit Intersection Distance (MOID) with the Earth is 0.05 AU or less and whose absolute magnitude (H) is 22.0 or brighter. More info: http://neo.jpl.nasa.gov/neo/groups.html

# Project Idea

Astronomical data heavily depends on observations, and thus may have some part of error in it. Although we do not have any reason to believe that there are ay significant errors in any data that NASA currently has about any NEA or PHA, we wanted to see if machine learning could be utilized to identify asteroids that need to be studied closely in order to classify them as PHA or not PHA.

Thus there are two questions we asked during the hackathon:

1. Among all objects classified as PHA, are there any objects that might actually be safe, but due to some data error are marked as PHA?

2. Among all objects classified as NEO but not PHA, are there any potentially dangerous objects?

# Data sources

Primary source of data for us was NASA API: https://api.nasa.gov/api.html#NeoWS

We were also heavily using JPL web site to better understand asteroid characterists: http://neo.jpl.nasa.gov

# Approach

Our approach was to apply clustering algorithms to the data we have and see if any PHA objects fall into NEO cluster or the other way around. In details, here is what we did:

1. Download the data from NASA API

2. Preprocess and clean it from what we were not going to use. We focused on the following data for each asteroid: Orbital Elements (13 values describing the orbit), Absolute Magnitude, Average Estimated Diameter

3. Reduce the dimentions of the data. After a lot of trial and error we decided to:

    3.1. Run PCA to arrive at just 2 parameters for each object

    3.2. Add each of the original parameters one by one at a time, and see what results this gives

4. Clusterize data with K-Means algorithm. After some experiments we decided to go with 3 clusters

5. Plot and visually analyze the results.

What we were looking for on the final images is an objectsof one type and one clusted clearly surrounded by objects of another type and cluster. In this, we defined two types: "PHA" (bg squares on resulting images) or "non-PHA NEO" (small circles). We also defined three clusters, which are generic clusters output by K-Means, and are color coded on the images.

# Tools

The list of tools we used, in no particular order:

1. Python 2.7

2. Scikit-learn

3. Pandas

4. Matplotlib

# Results achived during hackathon

We managed to find one object which appears to be an outlier. This object is recognized as PHA, however our analysis displayed it as a potentially safe. That suggests that this object might have been misclassified, and perhaps additional observations should be done to see if it is really belongs to PHA.

Object reference: http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3024715

# Further development (post-hackathon)

There is plenty of room to improve current results:

1. We have no any proof of correctness of our approach, so the it can very well be that this way of researching the subject does not have any sciencific meaning.

2. If this approach has a valid potential, every aspect of the project can be improved, by using better clustering algorithm, filtering out unnecessary orbital data, improving the way to reduce dimencionality.
