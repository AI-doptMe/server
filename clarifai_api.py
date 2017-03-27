from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read('config.ini')
apikey2 = config.get('clarifai','apikey')
apisecret2 = config.get('clarifai','apisecret')
os.environ["CLARIFAI_APP_ID"] = apikey2
os.environ["CLARIFAI_APP_SECRET"] = apisecret2


def clarifai_api(image_url):
    app = ClarifaiApp()
    model = app.models.get('Pets')
    image = ClImage(url=image_url)
    prediction = model.predict([image])
    #print prediction
    return prediction
