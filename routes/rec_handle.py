#create a function on a route that receives mp4 data in a data stream, not a whole mp4 file at once and supplies it to an api and awaits a response from said api.

from flask import Flask, request
import requests
import json

port = 5000

app = Flask(__name__)

@app.route('/rec', methods=['POST'])
def rec():
    data = request.stream.read()
    url = 'http://localhost:5001/rec'
    headers = {'Content-Type': 'application/json'}
    
    #instead of sending the data, print the details of the data being received in the stream
    print(data)
    

    # response = requests.post(url, data=data, headers=headers)
    # return response.text