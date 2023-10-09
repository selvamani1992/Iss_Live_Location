# ISS Live Tracker
The ISS Live Tracker is a real-time tracking application for the International Space Station (ISS) using Python and Streamlit. The International Space Station orbits the Earth at an altitude of approximately 400 km, moving at a speed of about 28,000 kilometers per hour. This application collects latitude and longitude coordinates of the ISS at regular intervals using APIs that provide live ISS position data. <br>

## How it Works
The application utilizes the following technologies and components: <br>
**Streamlit:** The web application framework used to create the user interface. <br>
**Folium:** A Python wrapper for Leaflet.js, which is used to create interactive maps. <br>
**Python Requests:** Used for making HTTP requests to the API that provides live ISS position data. <br>
**MongoDB:** A NoSQL database used to store the collected ISS location data. <br> <br>

## Features
**Live Tracking:** The application provides real-time tracking of the ISS on an interactive map. The ISS position is updated at regular intervals. <br>
**Historical Data:** The application stores historical ISS location data in a MongoDB database, allowing users to view past movements. <br>
**Map Visualization:** The ISS movement is visualized on a map, and a marker represents the current location. Past locations are connected with a line on the map. <br>

## Note
The application updates the ISS location every 15 seconds. You can adjust the update interval according to your preference. <br>
The application uses the Open Notify API to fetch live ISS position data. <br>
Enjoy tracking the International Space Station in real-time! <br>
