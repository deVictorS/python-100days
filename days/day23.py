#SERVER FLASK

from flask import Flask, request

day23 = Flask(__name__)

@day23.route('/login', methods["POST"])
def login():
    user = request.form.get("username")
    senha = request.form.get("password")

    if user == "admin" and senha == "Victor123":
        return "Bem vindo"
    else:
        return "Falha"
    
day23.run(host = "0.0.0.0", port = 5000)