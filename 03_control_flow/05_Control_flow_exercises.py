print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in range(0, 5):
    print(x[i])
# A1a:



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in range(0, len(x), 2):
    print(x[i])
# A1b:



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in range(0,5):
    if x[i] % 2 == 0:
        print(x[i])
# A1c:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
print(names[0][0])

print(names[1][0])
for i in range(0, 2):
    list = []
    list.append(names[i][0])
print(list)

# A2a:




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

for i in range(0,len(names)):
    c=[]
    c.append((names[i].index(' ')))
print(c)

# A2b:




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
name_short = []
for i in range(0,len(names)):
    a = names[i][0]
    b= names[i][names[i].index(' ')+1]
    name_short.append(a+b)

print(name_short)
# A2c:


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
for a_list in list_of_lists:
    if len(a_list) == len(set(a_list)):
        print(a_list)
#
# # A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

#A4a:
cont = True
# while cont:
#     a = input("Enter a number greater than 100")
#     if int(a)> 100:
#         cont = False
#     else:
#         print("higher number")


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise


# def prime(num):
#     root = int(round((int(num))**0.5))
#     factors = [i for i in range(2, root+1) if num % i == 0]
#     return not factors
#
# while cont:
#     b = input("Enter number greater than 100")
#     if int(b) > 100:
#         if prime(int(b)) == True:
#             print("number is prime")
#         else:
#             print("number is not prime")
#         cont = False
#     else:
#         print("Enter a higher number")
#

# A4b: