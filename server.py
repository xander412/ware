
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for GET request
@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

# Route for POST request
@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

