from flask import Flask
from pet_finder import *
import requests
import hashlib
import petfinder
app = Flask(__name__)

@app.route("/imageUpload",methods=['POST'])
def imageUpload():
    image=request.form['image']

#work in progress
@app.route("/petFinder")
def petFinderAPI():
    petFinder();


if __name__ == "__main__":
    app.run()
