from flask import Flask, request, url_for, send_from_directory, jsonify
import time
import requests
import hashlib
import petfinder
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
        print image_path
        return jsonify({
            'status': 200,
            'message': "Welcome to NeuroKnight's Backend API",
            'location': image_path
        })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#work in progress
@app.route("/petFinder")
def petFinderAPI():
    apiKey = "a3c7ab98952cd4109db691674901ac59"
    apiSecret="dc72e05d6cb02cbed2aff439111eea77"
    api = petfinder.PetFinderClient(api_key=apiKey, api_secret=apiSecret)
    petDict = []
    for pet in api.pet_find(
        animal="dog", location="33193", output="basic",
        breed="Labrador", count=1
    ):
        print(pet['name'], pet['id'])


    return petDict


if __name__ == "__main__":
    app.run()
