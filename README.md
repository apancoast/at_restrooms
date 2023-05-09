# Description
This repository contains Python code that reads a GPX file containing GPS coordinates of a track, creates a buffer zone around the track, and finds all the toilets within that buffer zone using OpenStreetMap data. It then visualizes the GPX track, buffer zone, and toilet locations on an interactive map using the Folium library.

# Usage
- Clone the repository to your local machine.
- Replace the at_centerline_full.gpx file with your own GPX file containing the track for which you want to find toilets.
- Install the required Python libraries: gpxpy, shapely, pyproj, osmnx, geopandas, and folium.
- Run the Python script map_at_restrooms.py.
- The script will output the number of toilets found within the buffer zone and display an interactive map in your default web browser showing the GPX track, buffer zone, and toilet locations.

# Sources
GPX file source: [Gaia GPS](https://www.gaiagps.com/datasummary/folder/dedfe4c3-dc0e-496e-b505-c47f14548a52/?layer=GaiaTopoRasterFeet)
StackOverflow Q&A: [Retrieve Campsites Within a Specific Radius Around a GPX Route from OSM](https://stackoverflow.com/questions/75144426/retrieve-campsites-within-a-specific-radius-around-a-gpx-route-from-osm)
Code manipulated by [Poe](Poe.com), a GPT-3 based language model.