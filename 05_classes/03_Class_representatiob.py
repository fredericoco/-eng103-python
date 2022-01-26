# class location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f" latitude ={self.latitude},longitude = {self.longitude}"
# #can be used for debugging
#
#     def __str__(self):
#         return f"{self.latitude},{self.longitude}"
#
#
#
# null = location(0, 0)
# print(repr(null))
# print(null)

class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog"

    def __repr__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog years old dog"
        else:
            return self.__str__()


fido = Dog(5)
print(fido)
print(f"Fido is a {fido:dog}")
