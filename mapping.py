import folium

# Create a map object
country_map = folium.Map(location=[33.3152, 44.3661], zoom_start=6)

# Add a marker for Iraq
# folium.Marker(location=[33.3152, 44.3661], popup='Iraq').add_to(country_map)
# folium.CircleMarker(location=[33.3152, 44.3661],radius=5, fill_color="PuBu", tooltip="haval").add_to(country_map)

fg = folium.FeatureGroup(name="my map")

fg.add_child(folium.Marker(location=[33.3152, 44.3661], tooltip="Iraq"))

map_coordinates = [
    [40.7128, -74.0060, "New York"], 
    [35.6895, 139.6917, "Tokyo"], 
    [-33.8651, 151.2094, "Sydney"], 
    [48.8566, 2.3522, "Paris"], 
    [51.5074, -0.1278, "London"], 
    [-22.9068, -43.1729, "Rio de Janeiro"], 
    [55.7558, 37.6173, "Moscow"], 
    [19.4326, -99.1332, "Mexico City"], 
    [31.2304, 121.4737, "Shanghai"], 
    [37.7749, -122.4194, "San Francisco"]
]


for i in map_coordinates:
    fg.add_child(folium.Marker(location=i[0:2], tooltip=i[2]))
    
country_map.add_child(fg)
 
# Display the map
country_map.save("map1.html")

