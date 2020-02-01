from flask import Flask, jsonify, request
import os
import pymongo
from pprint import pprint
import datetime

# Intialize
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))



# app.congig['MONGO_DBNAME'] = 'zamindar'

# Database 
mongo = pymongo.MongoClient('mongodb+srv://avi123:avi123@cluster0-xfmlr.gcp.mongodb.net/test?retryWrites=true&w=majority',
 maxPoolSize=50, connect=False)
db = mongo.testingseller
collection = db.seller

user = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}
collection.insert_one(user)




@app.route('/',methods=['GET'])
def get():
    return jsonify({'addha-zamindar' : 'Soumya Jagdev'})

## Run Server 
if __name__ == '__main__':
    app.run(debug=True)