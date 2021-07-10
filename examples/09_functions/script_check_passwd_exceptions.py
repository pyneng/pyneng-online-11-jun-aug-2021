
def check_passwd(username, password):
    if type(username) != str or type(password) != str:
        raise ValueError("Надо передавать строки")
    if len(password) < 8:
        print("Пароль слишком короткий")
        return False
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} установлен")
        return True
    print("#"*40)


data = [
    ["user1", "sdkfhjsaldfh35"],
    ["user2", "sdkf"],
    ["user3", "sdfssfdkjhkjuser3"],
    [10, 20]
]
correct_users = []
wrong_users = []
for user, passwd in data:
    print(user, passwd)
    try:
        check = check_passwd(user, passwd)
    except ValueError as error:
        print(error)
    else:
        if check:
            correct_users.append(user)
        else:
            wrong_users.append(user)

print(correct_users)
print(wrong_users)

