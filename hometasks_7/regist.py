import json
from authenficator import authenticate


def register():
    username = input("Введите имя пользователя: ")
    with open("users.json") as f:
        users = json.load(username)
    if username in users:
        print("Пользователь с таким именем уже существует")
    else:
        password = input("Введите пароль: ")
        users[username] = password
        with open("users.json", "w") as f:
            json.dump(users, f)
            print("Пользователь успешно зарегистрирован")


while True:
    action = input("Введите 'r' для регистрации или 'a' для аутентификации: ")
    if action == "r":
        register()
    elif action == "a":
        authenticate()
    else:
        print("Неверный ввод")