from flask import Flask
import json
from pet_finder import *
import requests
import hashlib
import xmltodict
import petfinder
app = Flask(__name__)

@app.route("/imageUpload",methods=['POST'])
def imageUpload():
    image=request.form['image']

#work in progress
@app.route("/petFinder")
def petFinderAPI():
    data = json.dumps(xmltodict.parse(petFinder()))
    jsonData = json.loads(data)
    print jsonData['petfinder']['pets']['pet'][0]['breeds']
    for index in range(20):
        print jsonData['petfinder']['pets']['pet'][index].get('name')
        print jsonData['petfinder']['pets']['pet'][index]['breeds']['breed']
        #print jsonData['petfinder']['pets']['pet'][index]
    return data

if __name__ == "__main__":
    app.run()
