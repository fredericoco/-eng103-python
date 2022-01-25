# oop - object oriented Programing
class Dog:
    animal_kind = "canine"  # class variable

    def bark(self):  # method
        return "Woof!" + self.animal_kind

    def loud_bark(self):  # two functions are interchangeable
        return self.bark().upper()


fido = Dog()
lassie = Dog()
pluto = Dog()
print(fido, type(fido))
print(fido.animal_kind)
print(fido.bark())
print(fido.loud_bark())
print(fido.animal_kind)
Dog.animal_kind = "arachnid"
print(fido.animal_kind)
# class Ronaldo:
#     animal_kind = "Portuguese"
#
#     def siu(self, num):
#         return "si" + "uuu" * num
#
#     def loud_siu(self):
#         return self.siu().upper()
#
#
# Ronnie = Ronaldo()
# print(Ronnie.loud_siu())
