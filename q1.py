city1 = str(input())
city2 = str(input())
city3 = str(input())
if len(city1) < len(city2) < len(city3):
    print(city1, city3)
elif len(city1) < len(city3) < len(city2):
    print(city1, city2)
elif len(city2) < len(city1) < len(city3):
    print(city2, city3)
elif len(city2) < len(city3) < len(city1):
    print(city2, city1)
elif len(city3) < len(city1) < len(city2):
    print(city3, city2)
elif len(city3) < len(city2) < len(city1):
    print(city3, city1)