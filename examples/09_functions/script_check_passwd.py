from pprint import pprint


def check_passwd(
    username, password, *, min_len=8, check_numbers=False,
    check_spec_sym=True
):
    """
    Функция проверяет пароль, возвращает True/False
    """
    print(f"{username=} {password=} {min_len=}")
    if len(password) < min_len:
        #print("Пароль слишком короткий")
        return False
    elif username.lower() in password.lower():
        #print("Пароль содержит имя пользователя")
        return False
    elif check_numbers and len(set("0123456789") & set(password)) < 3:
        #print("В пароле должны быть хотя бы 3 уникальных числа")
        return False
    else:
        #print(f"Пароль для пользователя {username} установлен")
        return True
    print("#" * 40)


def check_user_list(user_passwd_data, **kwargs):
    print(f"{kwargs=}")
    correct_users = []
    wrong_users = []
    for user, passwd in user_passwd_data:
        check = check_passwd(user, passwd, **kwargs)
        if check:
            correct_users.append(user)
        else:
            wrong_users.append(user)
    return correct_users, wrong_users


data = [
    ["user1", "sdkfhjsaldfh35"],
    ["user2", "sdkf"],
    ["user3", "sdfssfdkjhkjuser3"],
]
ok, not_ok = check_user_list(data, min_len=4, check_numbers=True)
print(ok)
print(not_ok)

