# Inheritance and Polymorphism
class Mammal:
    def __init__(self, name):
        self.warm_blooded = True
        self.name = name

    def reproduce(self):
        print("Giving birth to live young")


class Horse(Mammal):
    def __init__(self, horse_name, jockey: str):
        super().__init__(horse_name)
        self.legs = 4
        self.jockey = jockey

    def reproduce(self):  # method overloading
        print("giving birth to live foals")


class Pony(Horse):
    def __init__(self, pony_name, cuteness_rating=10):
        super().__init__(pony_name, None)
        self.cuteness_rating = cuteness_rating

    def give_birth(self):  # method overloading
        super().reproduce()

    def give_birth(self, number_of_offspring=1):
        for i in range(number_of_offspring):
            super().reproduce()


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barbs = True

    def reproduce(self):
        print("laying eggs")


# perry = Platypus("perry")
# print(perry.poisonous_barbs)
# print(perry.reproduce())
# p = Pony("Twinkle toes")
# print(p.legs)
# p.reproduce()
# p.give_birth(4)
# # m = Mammal("Charlie")
# h = Horse("deez", "name")
# # print(h.name)
# # h.reproduce()
# print(h.jockey)

p = Pony("Sausage")
print(type(p))
print(type(p) is Pony)
print(type(p) is Horse)
