# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = (-(b / (2 * a)))
        x2 = (-(b / (2 * a)))
        print(x1, x2)
    elif d > 0:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        print(min(x1, x2))
        print(max(x1, x2))
    elif d < 0:
        print("Нет корней")

# считываем данные
a, b, c = int(input()), int(input()), int(input())

solve(a, b, c)