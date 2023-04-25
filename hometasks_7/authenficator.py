def authenticate():
    username = input("Введите имя пользователя: ")
    with open("users.json", "r") as f:
        users = json.load(f)
    if username not in users:
        print("Пользователя с таким именем не существует")
    else:
        password = input("Введите пароль: ")
        if users[username] != password:
            print("Неверный пароль")
        else:
            print("Вы успешно вошли в систему")