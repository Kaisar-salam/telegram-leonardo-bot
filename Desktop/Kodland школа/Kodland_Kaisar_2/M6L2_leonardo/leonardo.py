import json
import requests
import time
from config import token
# API-ключ Leonardo
api_key = token
authorization = "Bearer %s" % api_key

# Заголовки для всех запросов к API
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": authorization
}

# URL для генерации изображения
url = "https://cloud.leonardo.ai/api/rest/v1/generations"


def generate_image(prompt, filename="result.jpg"):
    # Тело запроса:
    # описываем, какую картинку хотим получить
    payload = {
        "height": 512,   # высота изображения
        "width": 512,    # ширина изображения
        "modelId": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",  # модель Leonardo Creative
        "prompt": prompt                                 # текстовый запрос
    }

    # Отправляем POST-запрос и запускаем генерацию
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)

    # Из ответа получаем ID генерации
    # по нему потом будем забирать результат
    generation_id = response.json()['sdGenerationJob']['generationId']

    # Ждём, пока сервер сгенерирует изображение
    time.sleep(20)

    # URL для получения результата генерации
    result_url = "https://cloud.leonardo.ai/api/rest/v1/generations/%s" % generation_id

    # Отправляем GET-запрос и получаем результат
    response = requests.get(result_url, headers=headers)

    # Преобразуем ответ сервера в словарь
    data = response.json()

    # Достаём ссылку на первую сгенерированную картинку
    image_url = data["generations_by_pk"]["generated_images"][0]["url"]

    # Скачиваем изображение по ссылке
    image_data = requests.get(image_url).content

    # Сохраняем изображение в файл
    with open(filename, "wb") as file:
        file.write(image_data)

    # Возвращаем ссылку на изображение
    return image_url


# Пример вызова функции генерации изображения
# image_link = generate_image("An oil painting of a cat", "image.jpg")
# print("Изображение сохранено")