x = 1
y = 2
print(x,y)
def local_scope():
    x = 500
    y = 700
    return x ,y
#only part of this local scope
x,y = local_scope()
print(x,y)