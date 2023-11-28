from flask import Flask
import silmethods

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/derde")
def OtherJSON():
    vara= 12
    return "{\Opdracht\": \"Hele andere reactie\" ,\"Aantal:\""+str(vara)+"\"}"

@app.route("/game/<getal>")
def game1(getal):
    return silmethods.silgame(getal)
