import math
def square(side):
    space = side * side
    return math.ceil(space)

num_space = int(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(num_space)}")