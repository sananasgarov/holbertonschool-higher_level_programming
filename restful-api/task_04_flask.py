#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Bellekte saklanacak kullanıcı verileri (Başlangıçta boş)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    # Sadece kullanıcı adlarını (key'leri) liste olarak döndürür
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # Gelen verinin JSON olup olmadığını kontrol et
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Username eksik mi?
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Kullanıcı zaten var mı?
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Kullanıcıyı ekle
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)
