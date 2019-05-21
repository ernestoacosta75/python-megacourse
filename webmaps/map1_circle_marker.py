import folium
import pandas

map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles= "Mapbox Bright")  # Creating the Map object

# Adding some points markers on top of the base map
fg = folium.FeatureGroup(name="My Map")

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


for lt, ln, name, elev in zip(latList, lonList, nameList, elevList):    #Iterating both list to fill the FeatureGroup of points
    fg.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=9,
                                     popup=name,
                                     fill_color=color_producer(elev),
                                     color='grey',
                                     fill_opacity=0.8))

map.add_child(fg)

map.save("Map1.html") # Saving it as HTML file


'''
for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html") # Saving it as HTML file '''



