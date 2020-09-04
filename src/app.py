from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)


@app.route('/todos', methods=['GET'])
def hello_world():
    # suppose you have some information in a json variable
    some_data = { "name": "Bobby", "lastname": "Rixer" }
    # you can convert that variable into a json string like this
    json_text = jsonify(some_data)
    # and then you can return it on the response body like this
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[1]
    print("This is the position to delete: ",position)
    return jsonify(todos)  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)