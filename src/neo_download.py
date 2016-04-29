# Downloads data about all Near Earth Objects and stores into the csv file
# Relevant data: Name, ID, is it PHA, absolute magnitude, estimated diameter (min and max in m), orbital data

import csv
import json
import urllib2


api_key = "DEMO_KEY"

api_url_format = "https://api.nasa.gov/neo/rest/v1/neo/browse?page={page_number}&size=20&api_key={api_key}"

def load_page_data(page_number):
    page_url = api_url_format.format(page_number=page_number, api_key=api_key)

    raw_data = urllib2.urlopen(page_url).read()
    json_data = json.loads(raw_data)

    neo_list = json_data["near_earth_objects"]
    data_list = []

    for neo in neo_list:
        data = [
            neo["name"],
            neo["neo_reference_id"],
            neo["is_potentially_hazardous_asteroid"],
            neo["absolute_magnitude_h"],
            neo["estimated_diameter"]["meters"]["estimated_diameter_min"],
            neo["estimated_diameter"]["meters"]["estimated_diameter_max"],
            neo["orbital_data"]["orbit_id"],
            neo["orbital_data"]["minimum_orbit_intersection"],
            neo["orbital_data"]["jupiter_tisserand_invariant"],
            neo["orbital_data"]["epoch_osculation"],
            neo["orbital_data"]["eccentricity"],
            neo["orbital_data"]["semi_major_axis"],
            neo["orbital_data"]["inclination"],
            neo["orbital_data"]["ascending_node_longitude"],
            neo["orbital_data"]["orbital_period"],
            neo["orbital_data"]["perihelion_distance"],
            neo["orbital_data"]["perihelion_argument"],
            neo["orbital_data"]["aphelion_distance"],
            neo["orbital_data"]["perihelion_time"],
            neo["orbital_data"]["mean_anomaly"],
            neo["orbital_data"]["mean_motion"]
        ]
        data_list.append(data)

    return data_list

page_limit = 1000

all_data = []
print("Starting loading the NEO data")
for page in range(0, page_limit):
    print("Loading page {}".format(page))
    page_data = load_page_data(page)
    if not page_data:
        break
    all_data.extend(page_data)
print("Finished loading the NEO data")

with open("neo_api_data.csv", 'wb') as output:
    writer = csv.writer(output, delimiter=',')
    writer.writerows(all_data)
