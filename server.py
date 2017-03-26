from flask import Flask, request, url_for, send_from_directory, jsonify
import time
from pet_finder import *
import requests
import hashlib
import json
import os
from werkzeug.utils import secure_filename

CURRENT_PATH = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(CURRENT_PATH, 'uploads')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    print CURRENT_PATH
    print UPLOAD_FOLDER
    return "It works!"

@app.route("/imageUpload",methods=['GET', 'POST'])
def imageUpload():
    print "request in"
    file = request.files['photo']
    print(file.filename)
    if file.filename == '':
        return "No selected file"
    if file:
        fn = file.filename.split('.')
        filename = secure_filename(fn[0]) + '_' + str(int(time.time())) + '.' + fn[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_path = url_for('uploaded_file', filename=filename)
        #TODO
        print "petfinder"
        pets = petFinderAPI(image_path)

        print image_path
        return jsonify({
            'status': 200,
            'message': "Welcome to NeuroKnight's Backend API",
            'data' : pets,
            'location': image_path
        })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#work in progress
@app.route("/petFinder")
def petFinderAPI():
    return petFinder('http://www.yourpurebredpuppy.com/dogbreeds/photos-CD/chihuahuasf1.jpg');


if __name__ == "__main__":
    app.run()
