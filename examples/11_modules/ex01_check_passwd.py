
def check_passwd(
    username, password, min_passwd_len=8, spec_sym=None, numbers=False
):
    if len(password) < min_passwd_len:
        return False
    elif username.lower() in password.lower():
        return False
    elif numbers and not set("0123456789") & set(password):
        return False
    elif spec_sym and not set(spec_sym) & set(password):
        return False
    else:
        return True

print("##########")

if __name__ == "__main__":
# не выполнять при импорте
    print("Тестовая проверка")
    print(check_passwd("user1", "sdkhf24352e8"))
    print(check_passwd("user2", "sdkhf24352e8"))
    print(check_passwd("user3", "sdkh"))

