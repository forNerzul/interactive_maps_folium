from turtle import fillcolor
import folium # import folium module
mapita = folium.Map(location=[-25.30218449112151, -57.581171630786194], zoom_start=20) # create map object

# custom icon
penguIcon = folium.features.CustomIcon("static/img/pengu.jpeg", icon_size=(50, 50)) # create custom icon

# add marker to map
folium.Marker(  
    [-25.30220677071593, -57.58151499503942], 
    popup="<h1>Heladeria El Helado Feliz</h1> <img src='static/img/heladin.jpeg' width='250px'> <p>Abiertos desde 1806, cerrados cuando hay luna llena, pioneros en ingenieria heladil</p>", 
    tooltip="Helados recalentados en microondas, una propuesta ideal para descontracturarse.",
    icon=folium.Icon(prefix='glyphicon',icon='home', icon_color='white', color='orange')
    ).add_to(mapita)

# add another marker to map whith custom icon
folium.Marker(  
    [-25.30218449112151, -57.581171630786194], 
    popup="<h1>Penguin House 2.0</h1> <img src='static/img/penguin_house.jpeg' width='250px'> <p>Si tu codigo no se rompio, algo estas haciendo mal kp.</p>", 
    tooltip="Retiro Espiritual para programadores, creemos en el moustro de spaghetti volador",
    icon=penguIcon
    ).add_to(mapita)

# add a circle to map
folium.Circle( 
    location= [-25.30218449112151, -57.581171630786194],
    radius=100,
    popup="<p> Area buena onda!</p>",
    fill=True,
    fillcolor="blue"
    ).add_to(mapita)

# save map to file    
mapita.save('templates/map.html')

