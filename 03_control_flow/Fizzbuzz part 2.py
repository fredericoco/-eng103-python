def number_input(upper_limit, lower_limit):
    user_input1 = True
    while user_input1:
        if upper_limit.isdigit() and lower_limit.isdigit():
            user_input1 = False
        else:
            print("please enter in a valid number in digits")


def word_input(word_a, word_b):
    user_input2 = True
    while user_input2:
        if not (word_a and word_b).isdigit():
            user_input2 = False
        else:
            print("please enter a valid word")


def fizzbuzz(upper_limit, lower_limit, word_a, word_b):
    for i in range(lower_limit, upper_limit):
        if i % 15 == 0:
            print(word_a + word_b)
        elif i % 5 == 0:
            print(word_b)
        elif i % 3 == 0:
            print(word_a)
        else:
            print(i)
        pass

#use global variables

# word_at = input("Please enter the word which will be printed when dividable by 3")
# word_bt = input("Please enter the word which will be printed when dividable by 5")
# upper_limity = input("What is your chosen upper limit?\n")
# lower_limity = input("What is your chosen lower limit?\n")

# number_input(upper_limity, lower_limity)
# word_input(upper_limity, lower_limity)
fizzbuzz(100,1,"fred","rick")

