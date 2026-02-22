import requests
import time
from config import token

prompt = input(" Что ты хочешь увидеть на картинке? ")

url = "https://cloud.leonardo.ai/api/rest/v1/generations"
payload = {
    "prompt": prompt,
    "width": 1024,
    "height": 1024,
    "num_images": 1,
    "modelId": "7b592283-e8a7-4c5a-9ba6-d18c31f258b9",
    "seed": 1994276235,
    "sd_version": "KINO_2_1",
    "alchemy": False,
    "promptMagic": False,
    "highContrast": False,
    "transparency": "disabled",
    "ultra": False,
    "public": True,
    "styleUUID": "111dc692-d470-4eec-b791-3475abac4c46",
    "elements": [],
    "userElements": [],
    "controlnets": [],
    "contextImages": []
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + token
}

# Отправить запрос на генерацию изображения
response = requests.post(url, json=payload, headers=headers)

# Получаем ID изображения
id = response.json()["sdGenerationJob"]["generationId"]

# Получаем результат (ссылка на картинку)
for i in range(10):
    url = "https://cloud.leonardo.ai/api/rest/v1/generations/" + id
    response = requests.get(url, headers=headers)
    time.sleep(1.5)
    
    # Достаем ссылку на картинку
    links = response.json()["generations_by_pk"]["generated_images"]
    if links:
        link = links[0]["url"]
        break

print("Вот твоя картинка: " + link)