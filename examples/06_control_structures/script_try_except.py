# input_1 = input("Введите число: ")
#
# if input_1.strip().isdigit():
#     num1 = int(input_1)
#     print(num1 * 100)
# else:
#     print("надо вводить только числа")
# print("="*40)


input_1 = input("Введите число 1: ")
input_2 = input("Введите число 2: ")
try:
    num1 = int(input_1)
    num2 = int(input_2)
except ValueError as error:
    print(error)
    print("надо вводить только числа")
else:
    print("Делим", num1 / num2)
finally:
    print("="*40)
