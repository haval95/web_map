import folium
import pandas as pd

# Create a map object
country_map = folium.Map(location=[33.3152, 44.3661], zoom_start=6)

# Add a marker for Iraq
# folium.Marker(location=[33.3152, 44.3661], popup='Iraq').add_to(country_map)
# folium.CircleMarker(location=[33.3152, 44.3661],radius=5, fill_color="PuBu", tooltip="haval").add_to(country_map)

fg = folium.FeatureGroup(name="my map")

volcanoes = pd.read_csv("volcanoes.csv")

cordinates = list(map(list, zip(volcanoes["Latitude"], volcanoes["Longitude"], volcanoes["Name"], volcanoes["Elev"])))

def get_color_based_on_elv(elv) -> str:
    elv= int(elv.replace("m","").replace(",", ""))
    
    if elv >=  2000:
        return "red"
    elif elv >= 500:
        return "green"
    return "blue"

for cordinate in cordinates:
    fg.add_child(folium.CircleMarker(location=cordinate[0:2],tooltip=cordinate[2],popup=cordinate[3] ,radius=6, fill_color = get_color_based_on_elv(cordinate[3]), color=get_color_based_on_elv(cordinate[3]), fill_opacity=0.7)) 
country_map.add_child(fg)
 

# Display the map
country_map.save("map1.html")

