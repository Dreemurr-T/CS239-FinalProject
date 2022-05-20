from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/test',methods=['POST','GET'])
def update():
    node_f = open('./static/data/childnode1.json')
    edge_f = open('./static/data/childpic1.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data
    })



if __name__ == '__main__':
    app.run(port=5000)