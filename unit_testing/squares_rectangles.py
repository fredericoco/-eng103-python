class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        return self.width * self.height

    def perimeter_calc(self):
        return self.width * 2 + self.height * 2


class square(rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def number_surrounding(self, other):
        return int(self.area_calc() / other.area_calc())


# bob = rectangle(10, 6)
# alice = square(4)
# print(bob.perimeter_calc())
# print(bob.area_calc())
# print(alice.area_calc())
# print(alice.perimeter_calc())
# print(alice.number_surrounding(square(1)))
