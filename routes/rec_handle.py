from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/rec', methods=['POST'])
def rec():
    data = request.get_data()
    url = 'http://localhost:5001/rec'
    headers = {'Content-Type': 'application/json'}

    # instead of sending the data, print the details of the data being received in the stream
    print(json.loads(data))
    # response = requests.post(url, data=data, headers=headers)
    return data

if __name__ == "__main__":
    app.run(debug=True)