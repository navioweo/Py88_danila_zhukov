#1

first_name, second_name, third_name, fourth_name, fifth_name = 'Misha', 'Ignat', 'Ilya', 'Pasha', 'Andrei'
names = (first_name, second_name, third_name, fourth_name, fifth_name)
print(names)

#2
one, two, three, four, five = names
print(one, two, three, four, five)

#3
one, five = five, one
print(one, two, three, four, five)

#4
one = three = four = five = two
print(one, three, four, five)



