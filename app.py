# https://pythonbasics.org/flask-sqlalchemy/

from flask import Flask, render_template, request, url_for, redirect
import folium

# starting with sqlalchemy
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model

class Emprendimientos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(120), nullable=False)
    direccion = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    web = db.Column(db.String(120), nullable=True)
    facebook = db.Column(db.String(120), nullable=True)
    instagram = db.Column(db.String(120), nullable=True)
    twitter = db.Column(db.String(120), nullable=True)
    youtube = db.Column(db.String(120), nullable=True)
    linkedin = db.Column(db.String(120), nullable=True)
    imagen = db.Column(db.String(120), nullable=True)

    # constructor for the model
    def __init__(self, nombre, descripcion, direccion, telefono, email, web, facebook, instagram, twitter, youtube, linkedin, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.web = web
        self.facebook = facebook
        self.instagram = instagram
        self.twitter = twitter
        self.youtube = youtube
        self.linkedin = linkedin
        self.imagen = imagen

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
        popup='''<div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1 class="text-center">Heladeria El Helado Feliz</h1>
                <img class="center-block" src="static/img/heladin.jpeg" width="250px">
                <p class="text-center">Abiertos desde 1806, cerrados cuando hay luna llena, pioneros en ingenieria heladil</p> 
                
            </div>  
        </div>
        <div class="row text-center">
            <a class="fa fa-whatsapp btn btn-success" href="#" style="color:white;">WhatsApp</a>
        </div>
    </div>''', 
        tooltip="Helados recalentados en microondas, una propuesta ideal para descontracturarse.",
        icon=folium.Icon(prefix='glyphicon',icon='home', icon_color='white', color='orange')
    ).add_to(mapita)

    # add another marker to map whith custom icon
    folium.Marker(  
        coords["coor_2"],
        popup='''
                <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1 class="text-center">Penguin House 2.0</h1>
                <img class="center-block" src="static/img/penguin_house.jpeg" width="250px">
                <p class="text-center">Si tu codigo no se rompio, algo estas haciendo mal kp.</p> 
                
            </div>  
        </div>
        <div class="row text-center">
            <a class="fa fa-whatsapp btn btn-success" href="#" style="color:white;">WhatsApp</a>
        </div>
    </div>''', 
        tooltip="Retiro Espiritual para programadores, creemos en el moustro de spaghetti volador",
        icon=penguIcon
    ).add_to(mapita)

    # now we need to save the map in order to use it in the template
    mapita.save('templates/map.html')

    return render_template('index.html')

# route to the folium generated map in the template, this will be used in the index.html trought an iframe.
@app.route("/mapa")
def mapa():
    return render_template('map.html')

# endpoint to add new emprendimiento request from form with POST method
@app.route("/crear_emprendimiento", methods=['GET', 'POST'])
def crear_emprendimiento(): # GET and POST methods
    if request.method == 'POST': # if the method is POST
        nombre = request.form['nombre'] # get the name from the form
        descripcion = request.form['descripcion'] # get the description from the form
        direccion = request.form['direccion'] # get the address from the form
        telefono = request.form['telefono'] # get the phone from the form
        email = request.form['email'] # get the email from the form
        web = request.form['web'] # get the web from the form
        facebook = request.form['facebook'] # get the facebook from the form
        instagram = request.form['instagram'] # get the instagram from the form
        twitter = request.form['twitter'] # get the twitter from the form
        youtube = request.form['youtube'] # get the youtube from the form
        linkedin = request.form['linkedin'] # get the linkedin from the form
        imagen = request.form['imagen'] # get the image from the form

        emprendimiento = Emprendimientos(nombre, descripcion, direccion, telefono, email, web, facebook, instagram, twitter, youtube, linkedin, imagen) # create object with the data from the form

        db.session.add(emprendimiento) # add the object to the database
        db.session.commit() # commit the changes to the database

    return render_template('crear_emprendimiento.html') # return the template

# endpoint for viewing all emprendimientos in the database
@app.route("/listar_emprendimientos")
def listar_emprendimientos():
    emprendimientos = Emprendimientos.query.all() # get all emprendimientos from the database
    return render_template('listar_emprendimientos.html', emprendimientos=emprendimientos) # pass the emprendimientos to the template

if __name__ == "__main__": # if we are running this file directly, run the app
    db.create_all() # create database tables
    app.run(debug=True) # run app in debug mode