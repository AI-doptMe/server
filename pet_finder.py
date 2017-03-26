import requests
import hashlib
def petFinder():
    apiKey = "a3c7ab98952cd4109db691674901ac59"
    apiSecret="dc72e05d6cb02cbed2aff439111eea77"
    apiCombine = apiSecret+"key="+apiKey
    hashMD5 = hashlib.md5(apiCombine).hexdigest()
    petURL ="http://api.petfinder.com/pet.find?location=33193&animal=dog&key="+apiKey
    print(petURL)
    petInfo = requests.get(petURL).text
    return petInfo
