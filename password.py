import re #Импорт библиотеки
passwords = input("Enter password: ") #Ввод взодных данных
passwords = passwords.split(",") #Создание списка через ","

accepted_pass = [] #Создаем пустой список для паролей
for i in passwords: #Перебор паролей

    if len(i) < 4 or len(i) > 6: #Проверка пароля на кол-во символов
        continue

    elif not re.search("([a-z])+", i): #Проверка пароля на наличие букв нижнего регистра
        continue

    elif not re.search("([A-Z])+", i): #Проверка пароля на наличие букв верхнего регистра
        continue

    elif not re.search("([0-9])+", i): #Проверка пароля на наличие цифр
        continue

    elif not re.search("([*#+@])+", i): #Проверка пароля на наличие допустимых символов
        continue

    elif re.search("([ ])+", i): #Проверка пароля на наличие отступа
        continue

    else:
        accepted_pass.append(i) #Если все ХОРОШО добавляем пароль в список допустимых

print((" ").join(accepted_pass)) #Выводим допустимые пароли на эекран