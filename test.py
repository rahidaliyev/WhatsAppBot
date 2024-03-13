import json
import os
import random
from dotenv import load_dotenv
import pandas as pd
import requests
from ImageVM import ImageVM
global link 

def get_image(SEARCH_TERM):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    SEARCH_ENGINE_ID = "c2cfb4d8340e14562"
    URL = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": SEARCH_TERM,
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "searchType": "image",
    }
    list = []
    response = requests.get(URL, params=params)
    data = response.json()['items']
    for item in data:
        image_vm_object = ImageVM(
            kind=item['kind'],
            title=item['title'],
            link=item['link'],
            displayLink=item['displayLink'],
            fileFormat=item['fileFormat']
        )
        list.append(image_vm_object)
    link = random.choice(list).link
    print(link)
             
        
    
 
    
