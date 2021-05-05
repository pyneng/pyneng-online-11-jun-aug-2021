def check_password(
    username, password, *, min_len=8, check_numbers=False, spec_symbols=None
):
    if len(password) < min_len:
        return False
    elif username.lower() in password.lower():
        return False
    elif check_numbers and len(set("0123456789") & set(password)) == 0:
        return False
    elif spec_symbols and len(set(spec_symbols) & set(password)) == 0:
        return False
    else:
        return True


def select_correct_passwd(check_data, verbose=True, **kwargs):
    print(kwargs)
    correct = []
    incorrect = []
    for user, passwd in check_data:
        check = check_password(user, passwd, **kwargs)
        if check:
            correct.append([user, passwd])
        else:
            incorrect.append([user, passwd])
    if verbose:
        print(correct, incorrect)
    return correct, incorrect


data = [
    ["user1", "passwerwer"],
    ["user2", "passwer2334wer"],
    ["user3", "pasr23334wer"],
    ["user4", "pasrw"],
]

ok, not_ok = select_correct_passwd(
    data, verbose=True, min_len=2
)
print("Правильные", ok)
print(not_ok)
