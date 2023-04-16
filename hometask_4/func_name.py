def get_name():
    name = input("Введите имя\n")
    name_size = len(name)
    if name_size < 2:
        print('Error. The name is too short. The name must contain more than 1 character')
        return None
    elif name_size > 10:
        print('Error. The name is too long. The name must contain less than 11 character')
        return None
    else:
        return name


user = get_name()
print(user)