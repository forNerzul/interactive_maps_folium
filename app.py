from flask import Flask, render_template, request, url_for
import folium

app = Flask(__name__)

@app.route("/")
def index():
    # variables for the coords of the maps
    mapita_coords = [-25.30218449112151, -57.581171630786194]
    coords = {
        "coor_1": [-25.30220677071593, -57.58151499503942],
        "coor_2": [-25.30218449112151, -57.581171630786194]
    }

    # create map object
    mapita = folium.Map(location=mapita_coords, zoom_start=20) 

    # create custom icon
    penguIcon = folium.features.CustomIcon("static/img/pengu.jpeg", icon_size=(50, 50))

    # add marker to map
    folium.Marker(  
        coords["coor_1"],
        popup='<h1>Heladeria El Helado Feliz</h1> <img src="static/img/heladin.jpeg" width="250px"> <p>Abiertos desde 1806, cerrados cuando hay luna llena, pioneros en ingenieria heladil</p> <p><a class="btn btn-success" href="#"><i class="fa fa-whatsapp"> WhatsApp</i></a></p>', 
        tooltip="Helados recalentados en microondas, una propuesta ideal para descontracturarse.",
        icon=folium.Icon(prefix='glyphicon',icon='home', icon_color='white', color='orange')
    ).add_to(mapita)

    # add another marker to map whith custom icon
    folium.Marker(  
        coords["coor_2"],
        popup='<h1>Penguin House 2.0</h1> <img src="static/img/penguin_house.jpeg" width="250px"> <p>Si tu codigo no se rompio, algo estas haciendo mal kp.</p><p><a class="btn btn-success" href="#"><i class="fa fa-whatsapp"> WhatsApp</i></a></p>', 
        tooltip="Retiro Espiritual para programadores, creemos en el moustro de spaghetti volador",
        icon=penguIcon
    ).add_to(mapita)

    # now we need to save the map in order to use it in the template
    mapita.save('templates/map.html')

    return render_template('index.html')

@app.route("/mapa")
def mapa():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)