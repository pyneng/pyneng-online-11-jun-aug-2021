username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

while True:
    if len(password) < 8:
        print("Пароль слишком короткий")
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя")
    elif len(set("0123456789") & set(password)) < 3:
        print("В пароле должны быть min 3 уникальных цифры")
    else:
        print(f"Пароль для {username} прошел все проверки")
        break
        print("+"*50)
    password = input("Введите пароль еще раз: ")

print("#"*40)

# password_correct = False
# 
# while not password_correct:
#     if len(password) < 8:
#         print("Пароль слишком короткий")
#     elif username.lower() in password.lower():
#         print("Пароль содержит имя пользователя")
#     elif len(set("0123456789") & set(password)) < 3:
#         print("В пароле должны быть min 3 уникальных цифры")
#     else:
#         print(f"Пароль для {username} прошел все проверки")
#         password_correct = True
#         continue
#     password = input("Введите пароль еще раз: ")


# while (
#     len(password) < 8 or username.lower() in password.lower()
#     or len(set("0123456789") & set(password)) < 3
# ):
#     print(f"Пароль для {username} не прошел проверки")
#     password = input("Введите пароль еще раз: ")
#
# print(f"Пароль для {username} прошел все проверки")

