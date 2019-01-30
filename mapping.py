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

volcanoes = f.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, names):
  volcanoes.add_child(f.CircleMarker(location=[
                      lt, ln], radius=6, popup=name, fill_color=get_color(el), color="black", fill_opacity=0.9))

population = f.FeatureGroup(name="World population")

population.add_child(f.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {
    "fillColor": "green" if x["properties"]["POP2005"] < 10e6 else "orange" if 10e6 <= x["properties"]["POP2005"] < 20e6 else "red"}))

map.add_child(volcanoes)
map.add_child(population)

map.add_child(f.LayerControl())

map.save('Map.html')
 
