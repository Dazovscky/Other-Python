def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    print(x, y)

# считываем данные
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

# вызываем функцию
get_middle_point(x1, y1, x2, y2)