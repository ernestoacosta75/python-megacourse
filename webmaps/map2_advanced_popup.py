import folium
import pandas

map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles= "Mapbox Bright")  # Creating the Map object

# Adding some points markers on top of the base map
fg = folium.FeatureGroup(name="My Map")

dataFrame = pandas.read_csv("Volcanoes.txt") #Reading .csv file into a DataFrame

latList = list(dataFrame["LAT"]) #Getting the LAT colum values in a list
lonList = list(dataFrame["LON"]) #Getting the LON colum values in a list
nameList = list(dataFrame["NAME"].str.cat(dataFrame["LOCATION"], sep=":")) #Getting the NAME and LOCATION colums in a list

html = """<h4>Volcano information:</h4>
Name and Location: %s
"""

for lt, ln, name in zip(latList, lonList, nameList):    #Iterating both list to fill the FeatureGroup of points
    iframe = folium.IFrame(html=html % name, width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map_html_popup_simple.html") # Saving it as HTML file




