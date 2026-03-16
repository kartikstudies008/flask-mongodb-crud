from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
users = db["users"]

# Load webpage
@app.route("/")
def home():
    return render_template("index.html")

# CREATE user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    result = users.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

# READ users
@app.route("/users", methods=["GET"])
def get_users():
    data = []
    for user in users.find():
        user["_id"] = str(user["_id"])
        data.append(user)
    return jsonify(data)

# UPDATE user
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    users.update_one({"_id": ObjectId(id)}, {"$set": request.json})
    return jsonify({"message": "User updated"})

# DELETE user
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    users.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)