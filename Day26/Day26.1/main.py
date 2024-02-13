numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

new_list = [n + 1 for n in numbers]
print(new_list)

range_list = [item * 2 for item in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list = [name.upper() for name in names if len(name) >= 5]
print(new_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)