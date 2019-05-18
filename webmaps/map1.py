import folium

map = folium.Map(location = [38.58, -99.09], zoom_start=6, tiles= "Mapbox Bright")  # Creating the Map object

# Adding some points markers on top of the base map
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html") # Saving it as HTML file



