def get_name():
    name = input("Как вас зовут?\n")
    return name

username = get_name()
print(f"hello, {username}!")