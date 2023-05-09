import gpxpy
import shapely.geometry as geometry
from shapely.geometry import LineString
import pyproj 
import osmnx as ox
import geopandas as gpd
import shapely
import folium

# parse the GPX file
with open('at_centerline_full.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

track_points = [(point.latitude, point.longitude) for point in gpx.tracks[0].segments[0].points]

# check if the GPX file's coordinates are in degrees
if -180 <= track_points[0][0] <= 180 and -180 <= track_points[0][1] <= 180:
    print("The coordinates were in degrees")
    transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
    track_points = [transformer.transform(point[1], point[0]) for point in track_points]
else :
    print("The coordinates are in metres")

track_linestring = LineString(track_points)

# Create the buffer
buffer_distance = 3219 # this is a radius of 2 miles in meters
buffer_polygon = track_linestring.buffer(buffer_distance)

# Define the original and desired projections
inProj = pyproj.Proj(init='epsg:3857') # Web Mercator
outProj = pyproj.Proj(init='epsg:4326') # WGS 84

# Convert the coordinates of the Polygon object
buffer_polygon_4326 = shapely.ops.transform(lambda x, y: pyproj.transform(inProj, outProj, x, y), buffer_polygon)

# extract all the toilets within the buffer zone
toilets = ox.geometries.geometries_from_polygon(buffer_polygon_4326, tags={'amenity': 'toilets'})

# print the number of toilets found
print(f"Number of toilets found within the buffer zone: {len(toilets)}")

# extract the track points from the GPX file
track_points = [(point.latitude, point.longitude) for point in gpx.tracks[0].segments[0].points]

# define the map center as the midpoint of the track
midpoint = (sum([point[0] for point in track_points])/len(track_points), sum([point[1] for point in track_points])/len(track_points))

# create a Folium map object centered on the track
map_ = folium.Map(location=midpoint, zoom_start=12)

# add the GPX track to the map as a blue line
folium.PolyLine(locations=track_points, color='blue').add_to(map_)

# add the toilets to the map as red dots
for _, row in toilets.iterrows():
    location = row.geometry.centroid.coords[0][::-1]
    folium.CircleMarker(location=location, radius=5, color='red', fill=True, fill_color='red').add_to(map_)

# add the buffer zone to the map as a transparent polygon
folium.GeoJson(buffer_polygon_4326, style_function=lambda x: {'fillColor': 'transparent', 'color': 'green'}).add_to(map_)

# display the map
map_