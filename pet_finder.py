
def petFinder():
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