# for loops

l = ['a','b','c']
# for letter in l:
#     if letter == 'b':
#         print(letter.upper())
#     else:
#         print(letter)

# for i in range(1,10+1):
#     for letter in l:
#         print(i,letter)


me = {'name':'Jeff', 'age':21, 'job':'drug dealer'}
# for thing in me:
#     print(me[thing])

for key, value in me.items():
    if key == 'age':
        print(f'My {key} is {value} years old')
    else:
        print(f"My {key} is {value}")

for index, letter in enumerate(l):
    print(f"{letter} is in position {index}")