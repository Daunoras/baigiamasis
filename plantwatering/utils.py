import requests
from django.contrib.auth.forms import User
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from .models import Plant

def fetch_api_data(part:str):
    # url examples:
    # https://perenual.com/api/species/details/[ID]?key=[YOUR-API-KEY] -detail view
    # https://perenual.com/api/species-list?key=[YOUR-API-KEY]&q=[PLANT-NAME] -list, search by name
    # API key sk-4ZiR66169c759a2575057
    # part must be "/details/[ID]?key=[YOUR-API-KEY]" for single plant data and
    #  "-list?key=[YOUR-API-KEY]&q=[PLANT-NAM E]" for plant search by name
    url = f"https://perenual.com/api/species{part}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        data = None
    return data

def plant_from_api_data(data, user):
    if data:
        sciname = data["scientific_name"][0]
        watering = (str(data["watering_general_benchmark"]["value"])
                        + ' ' + data["watering_general_benchmark"]["unit"])
        r =requests.get(data["default_image"]["regular_url"])
        image_temp = NamedTemporaryFile()
        image_temp.write(r.content)
        image_temp.flush()
        plant_instance = Plant(sciname=sciname, watering=watering, owner=user)
        plant_instance.pic.save('pic.jpg', File(image_temp), save=True)
        plant_instance.save()

def select_object_and_create(id):
    part = f"/details/{id}?key=sk-4ZiR66169c759a2575057"
    selected_data = fetch_api_data(part)
    if selected_data:
        plant_from_api_data(selected_data)