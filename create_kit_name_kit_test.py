import sender_stand_request
import data

def get_user_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_user_kit_body = data.user_kit_body.copy()
    # изменение значения в поле Name
    current_user_kit_body["name"] = name
    # возвращается новый словарь с нужным значением Name
    return current_user_kit_body

def get_new_user_token():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_headers_dict = data.headers_kit.copy()
    # Сохранение  ответа на запрос о создании пользователя
    response = sender_stand_request.post_new_user(data.user_body)
    # Сохранение  ответа на запрос о создании пользователя в формате json
    response_json = response.json()
    # Сохранение  в переменнцую параметра authToken
    auth_token = response_json["authToken"]
    # изменение значения в поле Authorization
    current_headers_dict["Authorization"] = "Bearer " + auth_token
    # возвращается новый словарь с нужным значением Authorization
    return current_headers_dict

def positive_assert(name):

    # В переменную user_body сохраняется обновленное тело запроса
    user_kit_body = get_user_kit_body(name)
    # В переменную user_kit_response сохраняется результат запроса на создание набора пользователя:
    user_kit_response_body = sender_stand_request .post_new_user_kit(user_kit_body)

    # Проверяется, что код ответа равен 201
    assert user_kit_response_body.status_code == 201
    # Проверяется что параметр name в ответе соответствует параметру name в запросе
    assert user_kit_response_body.json()["name"] == user_kit_body["name"]

# Подготовка к тесту 3 негативная проверка
# Функция для негативной проверки
def negative_assert_code_400(name):

    # В переменную user_kit_body сохраняется обновлённое тело запроса
    user_kit_body = get_user_kit_body(name)

    # В переменную response сохраняется результат запроса
    user_kit_response_body = sender_stand_request.post_new_user_kit(user_kit_body)

    # Проверка, что код ответа равен 400
    assert user_kit_response_body.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert user_kit_response_body.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert user_kit_response_body.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские, латинские буквы, " \
                                         "специальные символы, пробел или цифры."\
                                         "Длина должна быть не менее 1 и не более 511 символов"

# Подготовка к тестам 10 и 11 негативная проверка
# Функция для негативной проверки
# В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_code_400_no_name(user_kit_body):
    user_kit_response_body = sender_stand_request.post_new_user_kit(user_kit_body)
    # Проверь, что код ответа — 400
    assert user_kit_response_body.status_code == 400

    # Проверь, что в теле ответа атрибут "code" — 400
    assert user_kit_response_body.json()["code"] == 400

    # Проверь текст в теле ответа в атрибуте "message"
    assert user_kit_response_body.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 1. Успешное создание набора пользователя
# Параметр name состоит из 1 символа
def test_create_user_1_letter_in_name_get_success_response():
    positive_assert("A")
# Тест 1 PASSED

# Тест 2. Успешное создание набора пользователя
# Параметр fisrtName состоит из 511 символов
def test_create_user_511_letter_in_name_get_success_response():
    positive_assert("Abcgedbnkpfhnssdxzsnmnnzcueusiqkjonbdhwrsnqgsyxqkxrwaqagpyzatdrqkvcstyjdgbkckpv"
                    "ohwkpowwubgwatnjqoghhlbpweicxbdujmnjcabfqxkpoyghhzzquflcwduboikycwudbhoomnhovgf"
                    "vxnfoutennbcmjbnyvfbcytdwmbabxyqvibtpewqfrvzigttqeidpujdrlhumzqneluctoieumllfhp"
                    "rbxiyyhzdouzmngssibciinufdipnbbtzwkakdiqwniupzplzfppyiwsfpbuzglfxuzrzgpgqftfvjw"
                    "haigmvzidzdsergvozqeztwpasgocqtqlixwxbofzuhjqvtqdjkphmenltwaieentfkrzzhfshlsknl"
                    "spwghxdvqouwecinaaytqxrialbjbpvjjoxjqxaolukaxtlxcykcqfsutlzrzcyyvyuvucwgxfapfwg"
                    "gasrqvzalgfcfddpuqaanolobvjshlqjluxhh")
# Тест 2 PASSED

# Тест 3. Ошибка (0 символов)
# Параметр Name состоит из 0 символов
def test_create_user_0_letter_in_name_get_error_response():
    negative_assert_code_400("")
# Тест 3 FAILED Expected code :400  Actual code :201

# Тест 4. Ошибка (512 символов)
# Параметр Name состоит из 512 символов
def test_create_user_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcgedbnkpfhnssdxzsnmnnzcueusiqkjonbdhwrsnqgsyxqkxrwaqagpyzatdrqkvcstyjdgbkckpv"
                             "ohwkpowwubgwatnjqoghhlbpweicxbdujmnjcabfqxkpoyghhzzquflcwduboikycwudbhoomnhovgf"
                             "vxnfoutennbcmjbnyvfbcytdwmbabxyqvibtpewqfrvzigttqeidpujdrlhumzqneluctoieumllfhp"
                             "rbxiyyhzdouzmngssibciinufdipnbbtzwkakdiqwniupzplzfppyiwsfpbuzglfxuzrzgpgqftfvjw"
                             "haigmvzidzdsergvozqeztwpasgocqtqlixwxbofzuhjqvtqdjkphmenltwaieentfkrzzhfshlsknl"
                             "spwghxdvqouwecinaaytqxrialbjbpvjjoxjqxaolukaxtlxcykcqfsutlzrzcyyvyuvucwgxfapfwg"
                             "gasrqvzalgfcfddpuqaanolobvjshlqjluxhha")
# Тест 4 FAILED Expected code :400  Actual code :201

# Тест 5. Успешное создание набора пользователя
# Параметр Name состоит из латинских символов
def test_create_user_english_letter_in_name_get_success_response():
    positive_assert("QWErty")
# Тест 2 PASSED

# Тест 6. Успешное создание набора пользователя
# Параметр Name состоит из русских символов
def test_create_user_russian_letter_in_name_get_success_response():
    positive_assert("Закуска")
# Тест 6 PASSED

# Тест 7. Успешное создание набора пользователя (Пробел в имени)
# В параметре Name есть пробелы
def test_create_user_has_space_in_name_get_success_response():
    positive_assert("Вино и шоколад")
# Тест 7 PASSED

# Тест 8. спешное создание набора пользователя (спец.символы)
# Параметр Name содержит запрещенные символы
def test_create_user_has_special_symbol_in_name_get_success_response():
    positive_assert("\"@#$%\",")
# Тест 8 PASSED

# Тест 9. Успешное создание набора пользователя (цифры)
# Параметр Name содержит цифры
def test_create_user_has_number_in_name_get_success_response():
    positive_assert("12345")
# Тест 9 PASSED

# Тест 10. Ошибка
# В запросе нет параметра Name
def test_create_user_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_kit_body
    # Иначе можно потерять данные из исходного словаря
    user_kit_body = data.user_kit_body.copy()
    # Удаление параметра firstName из запроса
    user_kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_code_400_no_name(user_kit_body)
# Тест 10 FAILED Expected code :400  Actual code :500

# Тест 11. Ошибка
# Параметр Name не тот тип данных
def test_create_user_number_type_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    user_kit_body = get_user_kit_body(123)
    # В переменную response сохрани результат вызова функции
    user_kit_response_body = sender_stand_request.post_new_user_kit(user_kit_body)
    # Проверка кода ответа
    assert user_kit_response_body.status_code == 400
# Тест 11 FAILED Expected code :400  Actual code :201
