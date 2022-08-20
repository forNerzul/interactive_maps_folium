import folium # import folium module
m = folium.Map(location=[-25.30218449112151, -57.581171630786194], zoom_start=20) # create map object
folium.Marker(  [-25.30218449112151, -57.581171630786194], 
                popup="<i>Penguin House 2.0</i> <img src='penguin.jpeg' width='80px'>", 
                tooltip="Retiro Espiritual para programadores, creemos en el moustro de spaghetti volador",
                icon=folium.Icon(icon='heart', icon_color='red')).add_to(m) # add marker to map
m.save('map.html') # save map to html file
