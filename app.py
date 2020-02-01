from flask import Flask, jsonify, request
from flask.ext.pymongo import pymongo
import os


app = Flask(__name__)


## Run Server 


if __name__ == '__main__':
    app.run(debug=True)