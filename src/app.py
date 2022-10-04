from flask import Flask, jsonify, request, json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

todos = [
    { "label": "Prueba1", "done": False },
    { "label": "Prueba2", "done": False },
    { "label": "Prueba3", "done": False }
    ]

@app.route('/', methods=['GET'])  # GET By Default
def hello_world():
    return "Hello, World!"

@app.route('/todos', methods=['GET'])  # GET By Default
def todo():
    json_text = jsonify(todos)
    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
