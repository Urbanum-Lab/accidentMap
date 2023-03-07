import time

import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

df = pd.read_csv("data/raw/balesetek_jav_fullos.csv")
df.dropna(axis=1, inplace=True)

# bad characters
df["Város"] = [e.replace("ďż˝", "ü") for e in df["Város"]]

df = df.drop(columns=["Unnamed: 0", "#", "Utca"])

# cannot correct bad characters
points2streets = {}
streets = []
for _, row in df.iterrows():
    try:
        lat = row["LAT"]
        lon = row["LON"]
        if (lat, lon) not in points2streets.keys():
            geodata = geolocator.reverse(str(lat) + "," + str(lon))
            time.sleep(0.05)
            street = geodata.address.split(",")[:-6]
            street = [e for e in street if not e.isnumeric()]
            points2streets[(lat, lon)] = " ".join(street)
        else:
            street = points2streets[(lat, lon)]
        streets.append(street)
    except Exception as e:
        print(e)
        streets.append("nan")
        continue

df["street"] = streets
df.to_csv("data/interim/cleaned.csv", index=False)
