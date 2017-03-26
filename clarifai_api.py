from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
os.environ["CLARIFAI_APP_ID"] = 'vc4olAMylUp_8fus_8sO-CLcbJC8uegeLvr0F428'
os.environ["CLARIFAI_APP_SECRET"] = 'lA95zrEuyIeWBaiv07QHm7O0r-2_KIgO2MC2cz8d'

app = ClarifaiApp()
model = app.models.get('Pets')
image = ClImage(url='http://www.doggies.com/images-new/breed-guide-dog-photos/Chihuahua_face.jpg')
print(model.predict([image]))
