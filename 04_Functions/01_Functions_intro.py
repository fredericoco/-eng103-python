# def woof(number_of_woofs):
#     print("Woof!"*number_of_woofs)
#
#
# def greeting(name: str):
#     print(f"Hello to you, {name}")
#

# def double_plus_one(num1: int, num2: int):
#     ans = num1 * 2 + num2
#     return ans
#
#
# x = double_plus_one(5, 2)
# print(x)
# #  multiple arguments


def shopping(name, *items, shout=False):
    if shout:
        name = name.upper()
    for item in items:
        print(f"{name}!Don't forget to buy {item}")


shopping("David", "banana", "apple", "nuts", "orange", True)

"""""
Three quote marks create a space for commenting on code
"""""
