from pprint import pprint


def check_user_list(user_passwd_data):
    correct_users = []
    wrong_users = []
    for user, passwd in user_passwd_data:
        check = check_passwd(user, passwd)
        if check:
            correct_users.append(user)
        else:
            wrong_users.append(user)
    return correct_users, wrong_users


def check_passwd(username, password):
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


def main():
    data = [
        ["user1", "sdkfhjsaldfh35"],
        ["user2", "sdkf"],
        ["user3", "sdfssfdkjhkjuser3"],
    ]
    pprint(check_user_list(data))
    ok, not_ok = check_user_list(data)
    print(ok)
    print(not_ok)


main()
