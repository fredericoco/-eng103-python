#  These two variables are the upper  and lower limit of the fizzbuzz game,
#  they determine when the game starts and stops
upper_limit = int(input("What is your chosen upper limit?"))
lower_limit = int(input("What is your chosen lower limit?"))
#  The two variables below determine the two words printed by the game when something is
#  dividable by 3, 5 or 15 without having a remainder
word_a = input("Please enter the word which will be printed when dividable by 3")
word_b = input("Please enter the word which will be printed when dividable by 5")

#  for loop over the range created by the user
# The modular determines whether it's a factor of 3,5, or 15 and therefore printing the word when appropriate
for i in range(lower_limit, upper_limit+1):
    if i % 15 == 0:
        print(word_b+word_a)
    elif i % 5 == 0:
        print(word_b)
    elif i % 3 == 0:
        print(word_a)
    else:
        print(i)
