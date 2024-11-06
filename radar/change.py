import requests
import json

# URL для отправки конфигурационного запроса
endpoint = "http://localhost:4000/config"

# Параметры конфигурации для отправки на сервер
config_params = {
    "measurementsPerRotation": 360,
    "rotationSpeed": 10,
    "targetSpeed": 500
}

# Заголовки запроса
headers = {
    "Content-Type": "application/json"
}

# Отправка PUT-запроса с конфигурационными данными
try:
    response = requests.put(endpoint, headers=headers, data=json.dumps(config_params))

    # Проверка успешности запроса
    if response.ok:
        print("Запрос выполнен успешно:", response.json())
    else:
        print("Ошибка при выполнении запроса:", response.status_code, response.text)
except requests.RequestException as e:
    print("Произошла ошибка сети:", e)
