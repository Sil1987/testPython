from flask import Flask
import Priscillamethod

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/derde")
def OtherJSON():
    vara= 12
    return "{\Opdracht\": \"Hele andere reactie\" ,\"Aantal:\""+str(vara)+"\"}"

@app.route("/fourth")
def vierde():
    return Priscillamethod.priscillamethode()
