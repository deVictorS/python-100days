#SERVER FLASK

from flask import Flask, request, render_template, url_for, redirect
from day30 import iniciar_monitoramento

app = Flask(__name__)
iniciar_monitoramento(app)

@app.route('/')
def index():
    return render_template("login.html")

def home():
    return "Monitor integrado"

@app.route('/login', methods=["POST"])
def login():
    user = request.form.get("username")
    senha = request.form.get("password")

    if user == "admin" and senha == "admin":
        return redirect("/inicio")
    else:
        return "Falha"
    
@app.route("/inicio")
def inicio():
    return "Menu inicial"
    
app.run(host = "0.0.0.0", port = 5000)