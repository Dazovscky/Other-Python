list=[]   #Создаем пустой список
for i in range(4):  #Счетчик для входных данных
    str = input()  #Водные даннык
    digits=[int(x) for x in str.split(',')] #Обработка входных данных
    list.append(digits) #Создаем матрицу из входных данных

for i in range(len(list)): #Счетчик списка list
    row_num = list[i][0] #Кол-во строк
    col_num = list[i][1] #Кол-во столбцов
    matrix = [[0 for col in range(col_num)] for row in range(row_num)] #Создаем матрицу

    val = 1 #Создаем переменную
    for row in range(row_num): #Заполняем матрицу значениями
        for col in range(col_num):
            matrix[row][col]= val
            val +=  1

    print(matrix) #Выводим матрицу на экран

