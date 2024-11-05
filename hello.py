from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Maliyudo, World!</p>"

@app.route("/saludo")
def saludo():
    return "<p> saludos al poyo, al pajuo y al pinche teodoro y al vaginangel </p>"

@app.route("/about")
def sobres():
    return "<p> Brandon Alan Lopez Ruiz / Brandon.lopez@uabc.edu.mx </p>"