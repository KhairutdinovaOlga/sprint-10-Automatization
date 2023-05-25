import configuration
import requests
import data

# функция создает нового пользователя
def post_new_user(user_body):
    # При обращении к функциией передают полный путь до документации, а так же заголовки и параметры запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body,
                         headers=data.headers)
# Переменной присваивается вызов функции
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# Функция создания нового набора пользователя
def post_new_user_kit(user_kit_body):
    # При обращении к функциией передают полный путь до документации, а так же заголовки и параметры запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=user_kit_body,
                         headers=data.headers_kit)
