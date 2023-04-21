line_one = input("Введите строку один:\n")
line_two = input("Введите строке два:\n")
line_three = input("Введите строку три:\n")
line_four = input("Введите строку четыре:\n")

with open('examples.txt', 'w') as file:
    file.write(line_one + '\n')
    file.write(line_two + '\n')

with open('examples.txt', 'a') as file:
    file.write(line_three + '\n')
    file.write(line_four + '\n')

