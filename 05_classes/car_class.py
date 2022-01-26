class Car:
    def __init__(self, make, maximum_speed):
        self.make = make
        self.maximum_speed = maximum_speed
        self._current_speed = 0

    def get_speed(self):
        return self._current_speed

    def acceleration(self, value_a):
        self._current_speed = min(self.maximum_speed, self._current_speed + value_a)
        # if self.current_speed +value_a > self.maximum_speed:
        #     self.current_speed = self.maximum_speed
        # else:
        #     self.current_speed += value_a
        # return self.current_speed

    def brake(self, value_b):
        self._current_speed = max(0, self._current_speed - value_b)
        # if self.current_speed - value_b < 0:
        #     self.current_speed = 0
        # else:
        #     self.current_speed -= value_b


if __name__ == "__main__":
    print("Car class __name__ is"+ __name__)
