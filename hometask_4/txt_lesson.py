def check_name():
    name = input("Введите имя\n")
    return name

username = check_name()
name_size = len(username)
if name_size < 2:
    print('Error. The name is too short. The name must contain more than 1 character')

elif name_size > 10:
    print('Error. The name is too long. The name must contain less than 11 character')

else:
    print(username)
