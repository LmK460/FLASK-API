
from flask import Flask, jsonify
from flask import render_template
from flask import request
import socket
import threading



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temperatura', methods=['GET'])
def Temperature():

    #result = last_measures[0]
    #print(result)
    
    return jsonify('35')


@app.route('/humidade', methods=['GET'])
def Humidity():

    #result = last_measures[['hum']]
    #print(result)
    
    return jsonify('35')

@app.route('/luz', methods=['GET'])
def Luz():

    #result = last_measures['light']
    
    return jsonify('1')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080, debug=True)

