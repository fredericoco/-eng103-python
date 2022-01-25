# upper_limity = input("What is your chosen upper limit?\n")
# lower_limity = input("What is your chosen lower limit?\n")
def number_input(upper_limit, lower_limit):
    user_input1 = True
    while user_input1:
        if upper_limit.isdigit() and lower_limit.isdigit():
            user_input1 = False
        else:
            print("please enter in a valid number in digits")


#  The two variables below determine the two words printed by the game when something is
#  dividable by 3, 5 or 15 without having a remainder


 #word_at = input("Please enter the word which will be printed when dividable by 3")
# word_bt = input("Please enter the word which will be printed when dividable by 5")

def word_input(word_a, word_b):
    user_input2 = True
    while user_input2:
        if not (word_a and word_b).isdigit():
            user_input2 = False
        else:
            print("please enter a valid word")


#  for loop over the range created by the user
# The modular determines whether it's a factor of 3,5, or 15 and therefore printing the word when appropriate

def fizzbuzz(upper_limit, lower_limit, word_a, word_b):
    number_input(upper_limit, lower_limit)
    word_input(word_a, word_b)
    for i in range(lower_limit, upper_limit):
        if i % 15 == 0:
            print(word_a + word_b)
        elif i % 5 == 0:
            print(word_b)
        elif i % 3 == 0:
            print(word_a)
        else:
            print(i)


#fizzbuzz(upper_limity=input("What is your chosen upper limit?\n"), lower_limity=input("What is your chosen lower limit?\n"),word_a=input("Please enter the word which will be printed when dividable by 3"), word_b =input("Please enter the word which will be printed when dividable by 5"))
#fizzbuzz(100,1,"s","fg")