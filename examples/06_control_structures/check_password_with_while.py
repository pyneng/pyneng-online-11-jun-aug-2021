username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Пароль слишком короткий\n")
        password = input("Введите пароль еще раз: ")
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя\n")
        password = input("Введите пароль еще раз: ")
    elif len(set("0123456789") & set(password)) < 3:
        print("В пароле должны быть min 3 уникальных цифры\n")
        password = input("Введите пароль еще раз: ")
    else:
        print(f"Пароль для {username} прошел все проверки")
        password_correct = True

print("#"*40)

# while (
#     len(password) < 8 or username.lower() in password.lower()
#     or len(set("0123456789") & set(password)) < 3
# ):
#     print(f"Пароль для {username} не прошел проверки")
#     password = input("Введите пароль еще раз: ")
# 
# print(f"Пароль для {username} прошел все проверки")

