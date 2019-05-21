import folium
import pandas

dataFrame = pandas.read_csv("Volcanoes.txt") #Reading .csv file into a DataFrame

latList = list(dataFrame["LAT"]) #Getting the LAT colum values in a list
lonList = list(dataFrame["LON"]) #Getting the LON colum values in a list
elevList = list(dataFrame["ELEV"]) #Getting the LON colum values in a list
nameList = list(dataFrame["NAME"].str.cat(dataFrame["LOCATION"], sep=":")) #Getting the NAME and LOCATION colums in a list

'''This function returns a color depending on
the elevation value.'''
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles= "Mapbox Bright")  # Creating the Map object

# Adding some points markers on top of the base map
fgv = folium.FeatureGroup(name="Volcanoes")    # FeatureGroup fro volcanoes

for lt, ln, name, elev in zip(latList, lonList, nameList, elevList):    #Iterating both list to fill the FeatureGroup of points
    #fg.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon(color=color_producer(elev))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=9,
                                     popup=name,
                                     fill_color=color_producer(elev),
                                     color='grey',
                                     fill_opacity=0.8))


fgp = folium.FeatureGroup(name="Population")    # FeatureGroup fro volcanos

# Adding a GeoJson Polygon layer
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
                            else 'orange' if 10000000 <= x["properties"]["POP2005"] < 20000000
                            else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

# Adding the LayerControl
map.add_child(folium.LayerControl())

map.save("Map1.html") # Saving it as HTML file




