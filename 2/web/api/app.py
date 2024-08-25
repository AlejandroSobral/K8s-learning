from flask import Flask, request, jsonify
from pymongo import MongoClient

# Replace with your actual MongoDB connection details
MONGODB_HOST = "mongodb://localhost:5002"  # Replace with container name
MONGODB_DATABASE = "FirstDB"
MONGODB_COLLECTION = "CollectOne"

# Connect to MongoDB
client = MongoClient(MONGODB_HOST)
db = client[MONGODB_DATABASE]
collection = db[MONGODB_COLLECTION]

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world from a Container!\r\n"


@app.route('/items', methods=['POST', 'GET'])
def manage_items():
    if request.method == 'POST':
        # Add a new item
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Missing data'}), 400
        collection.insert_one(data)
        return jsonify({'message': 'Item added successfully'}), 201
    elif request.method == 'GET':
        # Get all items
        items = list(collection.find({}))
        # Convert ObjectId to string before returning
        items = [dict(item) for item in items]
        return jsonify(items)
    else:
        return jsonify({'error': 'Unsupported method'}), 405


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)