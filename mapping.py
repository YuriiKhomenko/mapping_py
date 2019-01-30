import folium as f
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"]) 
names = list(data["NAME"])

def get_color(elevation):
  if elevation < 1000:
    return "green"
  elif 1000 <+ elevation < 3000:
    return "yellow"
  else:
    return "red"

map = f.Map(location=[51.11, 17.03])

fg = f.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, names):
  fg.add_child(f.CircleMarker(location=[lt,ln], radius=6, popup=name, fill_color=get_color(el), color="black", fill_opacity=0.9))

map.add_child(fg)
map.save('Map.html')
 
