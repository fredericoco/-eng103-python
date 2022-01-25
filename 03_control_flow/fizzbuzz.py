#  These two variables are the upper  and lower limit of the fizzbuzz game,
#  they determine when the game starts and stops
user_input1 = True
while user_input1:
    upper_limit = input("What is your chosen upper limit?\n")
    lower_limit = input("What is your chosen lower limit?\n")
    if upper_limit.isdigit() and lower_limit.isdigit():
        user_input1 = False
    else:
        print("please enter in a valid number in digits")

#  The two variables below determine the two words printed by the game when something is
#  dividable by 3, 5 or 15 without having a remainder
user_input2 = True
while user_input2:
    word_a = input("Please enter the word which will be printed when dividable by 3")
    word_b = input("Please enter the word which will be printed when dividable by 5")
    if not (word_a and word_b).isdigit():
        user_input2 = False
    else:
        print("please enter a valid word")

#  for loop over the range created by the user
# The modular determines whether it's a factor of 3,5, or 15 and therefore printing the word when appropriate
for i in range(int(lower_limit), int(upper_limit)+1):
    if i % 15 == 0:
        print(word_b+word_a)
    elif i % 5 == 0:
        print(word_b)
    elif i % 3 == 0:
        print(word_a)
    else:
        print(i)
