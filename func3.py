# объявление функции
def merge(numbers1, numbers2):
    s = []
    s.extend(numbers1 + numbers2)
    s.sort()
    return s

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))