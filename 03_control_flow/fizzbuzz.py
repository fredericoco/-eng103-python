upper_limit = int(input("What is your chosen upper limit?"))
lower_limit = int(input("What is your chosen lower limit?"))
word_a = input("Please enter the word which will be printed when divisable by 3")
word_b = input("Please enter the word which will be printed when divisable by 5")


for i in range(lower_limit, upper_limit+1):
    if i % 15 == 0:
        print(word_b +" "+ word_a)
    elif i % 5 == 0:
        print(word_b)
    elif i % 3 == 0:
        print(word_a)
    else:
        print(i)

