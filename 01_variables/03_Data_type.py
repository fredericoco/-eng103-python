import  math
# # i = 375
# f=3.75
# c = 3j +2
# print(c,type(c))
#
# add = 3+5
# subtract = 3-5
# multiply =3*5
# divide = 3/5
# power = 3**2
# modular =  13 % 3
# whole_divide = 13 // 3
#print(math.sqrt(25))

#Strings!

single = 'String in single quotes'
double = "String in double qoutes"
Single_in_double = "This is David's string"
Double_in_single = 'This is a "string"'
both = "this is David's \"string\""
print(both)


#indexing and slicing
hi = "Hello World!"
print(hi[6]) #Python starts counting at zero!
print(hi[0])
print(hi[-1])
print(hi[3:8])
print(len(hi))

#Methods

white_space = "         lots of white space          "
print(len(white_space))
print(white_space.strip())
print(white_space.upper())
print(white_space.lower())
print(white_space.strip().capitalize())
print(white_space.count(" "))
print(white_space.replace("o", "ooooooo").replace("i", "oooo").replace("a", "ooooo"))

# F-Strings (formatted strings)

a = math.pi
print(a)
print(f"Pi to 3dp: {a:.3f}")
print(f"Pi to 5dp: {a:.5f}")
print(f"Pi to 0dp: {a:.0f}")

big = 22534453.433454563
print(f"{big:5.3f}")


score = 16
max_score = 26

print(f"you scored {score/max_score:.2f}")
print(f"you scored {score/max_score:.2%}")
t = True
f = False

print(t, type(t))
print(3 != 5)

age = 16
drink = 'alcohol'

print(age > 18 and drink == 'alcohol')
print(age > 18 or drink == 'alcohol')
hi = "Hello World"

n = None

print(n, type(n))

print(type(15) is int)
