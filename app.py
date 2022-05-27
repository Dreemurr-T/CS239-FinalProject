from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__, static_folder='./static')
CORS(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/1',methods=['POST','GET'])
def update_1():
    node_f = open('./static/data/childnode1.json')
    edge_f = open('./static/data/childpic1.json')
    key_node_f = open('./static/data/corenode1.json')
    key_link_f = open('./static/data/keylinks1.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/2',methods=['POST','GET'])
def update_2():
    node_f = open('./static/data/childnode2.json')
    edge_f = open('./static/data/childpic2.json')
    key_node_f = open('./static/data/corenode2.json')
    key_link_f = open('./static/data/keylinks2.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/3',methods=['POST','GET'])
def update_3():
    node_f = open('./static/data/childnode3.json')
    edge_f = open('./static/data/childpic3.json')
    key_node_f = open('./static/data/corenode3.json')
    key_link_f = open('./static/data/keylinks3.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/4',methods=['POST','GET'])
def update_4():
    node_f = open('./static/data/childnode4.json')
    edge_f = open('./static/data/childpic4.json')
    key_node_f = open('./static/data/corenode4.json')
    key_link_f = open('./static/data/keylinks4.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/5',methods=['POST','GET'])
def update_5():
    node_f = open('./static/data/childnode5.json')
    edge_f = open('./static/data/childpic5.json')
    key_node_f = open('./static/data/corenode5.json')
    key_link_f = open('./static/data/keylinks5.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/6',methods=['POST','GET'])
def update_6():
    node_f = open('./static/data/childnode6.json')
    edge_f = open('./static/data/childpic6.json')
    key_node_f = open('./static/data/corenode6.json')
    key_link_f = open('./static/data/keylinks6.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })


@app.route('/7',methods=['POST','GET'])
def update_7():
    node_f = open('./static/data/childnode7.json')
    edge_f = open('./static/data/childpic7.json')
    key_node_f = open('./static/data/corenode7.json')
    key_link_f = open('./static/data/keylinks7.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/8',methods=['POST','GET'])
def update_8():
    node_f = open('./static/data/childnode8.json')
    edge_f = open('./static/data/childpic8.json')
    key_node_f = open('./static/data/corenode8.json')
    key_link_f = open('./static/data/keylinks8.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/9',methods=['POST','GET'])
def update_9():
    node_f = open('./static/data/childnode9.json')
    edge_f = open('./static/data/childpic9.json')
    key_node_f = open('./static/data/corenode9.json')
    key_link_f = open('./static/data/keylinks9.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

@app.route('/10',methods=['POST','GET'])
def update_10():
    node_f = open('./static/data/childnode10.json')
    edge_f = open('./static/data/childpic10.json')
    key_node_f = open('./static/data/corenode10.json')
    key_link_f = open('./static/data/keylinks10.json')
    node_data = json.load(node_f)
    edge_data = json.load(edge_f)
    key_node = json.load(key_node_f)
    key_link = json.load(key_link_f)

    return jsonify({
        "node":node_data,
        "edge":edge_data,
        "coreNode": key_node,
        "keyLink": key_link,
    })

if __name__ == '__main__':
    app.run(port=5000)