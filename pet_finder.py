import requests
import hashlib
import xmltodict
import json
import pprint
from flask import jsonify
from clarifai_api import *

def petFinder(image_url):
    color = ['White','black','Brown','tan']
    breed = ['Labrador','Chihuahua','Rottweiler','Terrier']
    #CALL CLARIFAI
    clarifai_prediction = clarifai_api(image_url)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(clarifai_prediction['outputs'][0]['data']['concepts'])
    clarifai_dict = clarifai_prediction['outputs'][0]['data']['concepts']
    topColor = None
    topBreed = None

    for concept in clarifai_dict:
        if concept['id'] in color:
            topColor = concept['id']
            break
    for concept in clarifai_dict:
        if concept['id'] in breed:
            topBreed = concept['id']
            break

    print topColor
    print topBreed


    #CONFIGS
    apiKey = "a3c7ab98952cd4109db691674901ac59"
    apiSecret="dc72e05d6cb02cbed2aff439111eea77"
    apiCombine = apiSecret+"key="+apiKey
    hashMD5 = hashlib.md5(apiCombine).hexdigest()
    petURL ="http://api.petfinder.com/pet.find?location=33193&animal=dog&breed="+topBreed+"&count=10&key="+apiKey
    print(petURL)

    #WEB REQUETS
    petInfo = requests.get(petURL).text
    data = json.dumps(xmltodict.parse(petInfo))
    jsonData = json.loads(data)
    largeImage = None
    returnList = []
    for index in xrange(len(jsonData['petfinder']['pets']['pet'])):
        name = jsonData['petfinder']['pets']['pet'][index].get('name')
        breed = jsonData['petfinder']['pets']['pet'][index]['breeds']['breed']
        contactEmail = jsonData['petfinder']['pets']['pet'][index]['contact']['email']
        contactPhone = jsonData['petfinder']['pets']['pet'][index]['contact']['phone']
        contactCity = jsonData['petfinder']['pets']['pet'][index]['contact']['city']
        petMedia = jsonData['petfinder']['pets']['pet'][index]['media']['photos']['photo']
        for pict in petMedia:
            print pict
            if pict['@size'] == 'x':
                largeImage = pict['#text']
                break
            if pict['@size'] == 'pn':
                largeImage = pict['#text']
                break;
            largeImage = pict['#text']
        print largeImage
        print name
        print breed
        print contactEmail
        print contactPhone
        print contactCity
        returnList.append({
            'name':name,
            'imageURL':largeImage,
            'breed':breed,
            'contactEmail':contactEmail,
            'contactPhone':contactPhone,
            'contactCity':contactCity
        })


    return json.dumps(returnList)
