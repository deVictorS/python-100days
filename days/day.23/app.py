#SERVER FLASK

from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
    user = request.form.get("username")
    senha = request.form.get("password")

    if user == "" and senha == "":
        return redirect("/inicio")
    else:
        return "Falha"
    
@app.route("/inicio")
def inicio():
    return "Menu inicial"
    
app.run(host = "0.0.0.0", port = 5000)