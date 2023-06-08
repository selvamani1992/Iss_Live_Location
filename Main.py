import streamlit as st
import folium
import pymongo
from streamlit_folium import folium_static
import requests
import ast
import datetime
import time

iconSat = folium.features.CustomIcon('IssSat.png', icon_size=(50, 50))
locations = []
client = pymongo.MongoClient("mongodb://@ac-hdblj4l-shard-00-00.xb5edcj.mongodb.net:27017,ac-hdblj4l-shard-00-01.xb5edcj.mongodb.net:27017,ac-hdblj4l-shard-00-02.xb5edcj.mongodb.net:27017/?ssl=true&replicaSet=atlas-7gqhz2-shard-0&authSource=admin&retryWrites=true&w=majority")
iss = client['ISS'] #creating database
iss_data = iss['location'] #creating collection
st.set_page_config(page_title="ISS Live Location", page_icon="",layout="wide")
# Function to update the map
def update_map(latitude, longitude, locations):
    global m
    m = folium.Map(location=[0, 0], tiles="Stamen Terrain", zoom_start=1.475, width="100%", height="100%")

    # Add a marker for the current location
    folium.Marker([latitude, longitude],tooltip=[latitude, longitude],icon=iconSat).add_to(m)

    # Add a line connecting the past locations
    if len(locations) > 1:
        split_locations = split_line(locations)
        for segment in split_locations:
            folium.PolyLine(segment, color="red", weight=2.5, opacity=1,dash_array='5, 5').add_to(m)
    # Display the updated map
    folium_static(m)

def split_line(line):
    split_locations = []
    prev_lon = line[0][1]
    segment = []
    for lat, lon in line:
        if abs(lon - prev_lon) > 180:  # Check if the line crosses the map boundaries
            split_locations.append(segment)
            segment = []

        segment.append([lat, lon])
        prev_lon = lon

    split_locations.append(segment)
    return split_locations
st.markdown(
    """
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .sidebar .sidebar-content {
        width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title('ISS Live Tracker')

st.write("This project focuses on real-time tracking of the International Space Station (ISS) using Python and "
         "Streamlit. The International Space Station orbits the Earth at an altitude of approximately 400 km "
         "and moves at a speed of about 28,000 kilometers per hour. By utilizing APIs that provide live ISS position "
         "data, the project collects latitude and longitude coordinates of the ISS at regular intervals.")

col1,col2,col3 = st.columns([2,8,1])
with col2:
    with st.empty():
        # Create a Folium map
        m = folium.Map(location=[0, 0], tiles="Stamen Terrain", zoom_start=1.475, width="100%", height="100%")
        # Display the initial map
        folium_static(m)
        # Collect latitude and longitude dynamically
        while True:
            response = requests.get('http://api.open-notify.org/iss-now.json')
            x = response.text
            a = ast.literal_eval(x)
            date = datetime.datetime.fromtimestamp(a['timestamp'])
            latitude = float(a['iss_position']['latitude'])
            longitude = float(a['iss_position']['longitude'])
            data = dict(timestamp=date,latitude=latitude,longitude=longitude)
            iss_data.insert_one(data)

            # Create a tuple with latitude and longitude
            location = (latitude, longitude)

            # Append the location to the list
            locations.append(location)

            # Update the map
            update_map(latitude, longitude, locations)

            # Wait for 15 seconds before collecting the next location
            time.sleep(15)
