# oop - object-oriented Programing
# Abstraction
# Encapsulation
class Dog:
    def __init__(self, breed, hair_length, legs=4,
                 criminal_record=None):  # Initialisation, dunder (double underscore) init
        self.animal_kind = "canine"  # class variable
        self.legs = legs
        self.criminal_record = criminal_record
        self.breed = breed
        self.set_hair_length(hair_length)
        print(self.bark())

    def set_hair_length(self, hair_length):
        if hair_length in ("short", "medium", "long"):
            return hair_length
        else:
            print("Hair length must be short, medium or long. Defaulting to medium")
            return "medium"

    def bark(self):  # method
        return "Woof!" + self.animal_kind

    def loud_bark(self):  # two functions are interchangeable
        return self.bark().upper()


fido = Dog("Dalmatian", "medium", 3, "naughty dog")

# pluto = Dog()
print(fido.animal_kind)
# fido.animal_kind = "giraffe"
print(fido.bark())
print(fido.loud_bark())
print(fido.breed)

# print(fido.animal_kind)
# Dog.animal_kind = "arachnid"
# print(fido.animal_kind)
# class Ronaldo:
#     def __init__(self, nationality, shirt_number):
#         self.nationality = nationality
#         self.shirt_number = shirt_number
#
#     def siu(self, num):
#         return "si" + "uuu" * num
#
#     def loud_siu(self, num):
#         return self.siu(num).upper()
#
#
# Ronnie = Ronaldo("portuguese", 7)
# R9 = Ronaldo("brilliant", 9)
#
# print(Ronnie.siu(10))
# print(Ronnie.loud_siu(10))
