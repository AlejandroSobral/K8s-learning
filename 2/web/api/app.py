import docker
from flask import Flask, request, jsonify, render_template, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import yaml


def read_yaml_config():
    with open(f"/{__file__.rsplit('.', 1)[0]}.yaml", 'r') as f:
        return yaml.safe_load(f)


cfg_params= read_yaml_config() #Configuration parameters

MONGODB_HOST = "172.18.0.2:27017"
MONGODB_DATABASE = "FirstDB"
MONGODB_COLLECTION = "CollectOne"

# Connect to MongoDB
client = MongoClient(MONGODB_HOST)
db = client[MONGODB_DATABASE]
collection = db[MONGODB_COLLECTION]

app = Flask(__name__, static_folder='static')



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/items', methods=['POST', 'GET'])
def manage_items():
    if request.method == 'POST':
        # Add a new item
        data = request.form
        object = {
            "name":data["name"],
            "role":data["role"]
        }
        if data is None:
            return jsonify({'error': 'Missing data'}), 400
        collection.insert_one(object)
        return redirect('/items')
    

        
    elif request.method == 'GET':
        # Get all items
        items = list(collection.find({}))
        items = [dict(item) for item in items]
        return render_template('items.html', items=items)

@app.route('/items/delete/<string:item_id>', methods=['POST', 'DELETE'])
def delete_item(item_id):
    if request.method == 'POST':
        try:
            deletion_result = collection.delete_one({'_id': ObjectId(item_id)})
            if deletion_result.deleted_count == 1:
                return redirect('/items')
                
            else:
                return jsonify({'error': 'Item not found'}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred during deletion'}), 500

        # This will not be executed due to the hidden field
        # You can optionally handle any logic here if needed.
        pass
    elif request.method == 'DELETE':
        try:
            deletion_result = collection.delete_one({'_id': ObjectId(item_id)})
            if deletion_result.deleted_count == 1:
                return jsonify({'message': 'Item deleted successfully'}), 200
            else:
                return jsonify({'error': 'Item not found'}), 404
        except Exception as e:
            return jsonify({'error': 'An error occurred during deletion'}), 500
    else:
        return jsonify({'error': 'Unsupported method'}), 405

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)