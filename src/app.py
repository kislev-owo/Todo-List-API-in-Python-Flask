from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)   


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[1]
    return jsonify(todos)  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)


""" 07
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
"""


""" 05 parte 2

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)
"""

""" 05

def hello_world():
    # suppose you have some information in a json variable
    some_data = { "name": "Bobby", "lastname": "Rixer" }
    # you can convert that variable into a json string like this
    json_text = jsonify(some_data)
    # and then you can return it on the response body like this
    return (json_text)
"""   

""" 03.3
def hello_world():
    return "<h1>Hello!</h1>"
"""