fruits = eval(input())

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as e:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)