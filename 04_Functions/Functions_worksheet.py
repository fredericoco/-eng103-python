print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def factors(num1):
    a = []
    for i in range(2, num1 + 1):
        if num1 % i == 0:
            a.append(i)

    return (a)


print(factors(12))
print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:#


def share_factors(num2, num3):
    a = factors(num2)
    b = factors(num3)
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                result = True
            else:
                result = False
                return result


print(share_factors(12, 19))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " "]


def finder(letter):
    for i in range(0, len(alphabet)):
        if letter == alphabet[i]:
            return (i + 1)


print(type(finder("b")))
# A2a:


print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def mason(name):
    code = []
    for letter in name:
        a = str(finder(letter))
        code.append(a)

    return ("".join(code))


print(mason("bob"))
print(int(mason("bob")) - 21)
print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password(word):
    sum = 0
    a = mason(word)
    for i in range(0, len(word) + 1):
        sum += int(a[i])
    return int(a) - sum


print(password("bob"))
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime_decider(num):
    prime = False
    for i in range(2, num):
        if num % i == 0:
            prime = True
    return prime


print(prime_decider(3))
print(prime_decider(123))
print(prime_decider(17))
print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit
def digit_prime(user_input):
    if str(user_input).isdigit():
        if prime_decider(int(user_input)):
            return False
        else:
            return True
    else:
        return "Not valid input"
# A3b:
print(digit_prime(102))

# -------------------------------------------------------------------------------------- #
