a = 5

def convert_num_sequence_to_str(sequence):
    str_list = []
    for item in sequence:
        str_list.append(str(item))
    return str_list


result = convert_num_sequence_to_str([1, 2, 3])
print(result)
print(a)


def login1(user, password):
    print(user, password)


login1("user1", "sdfsdfds")

def login2(params):
    user, password = params
    print(user, password)

u1 = ["user1", "dfsdf"]
login2(u1)
