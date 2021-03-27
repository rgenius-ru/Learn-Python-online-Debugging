import random as rnd


class Astronaut:
    def __init__(self, astronaut_id, name, parameters):
        self.name = name
        self.id = astronaut_id
        self.vital_parameters = parameters


class SpaceShuttle:
    def __init__(self):
        self.data = rnd.sample(range(100), 100)


class Calculation:
    def __init__(self, num1, num2, num3, astronaut_data):
        self.i1 = num1
        self.i2 = num2
        self.i3 = num3
        self.data = astronaut_data

    def result(self, _number):
        _number = (self.data[self.i1] - self.data[self.i2] - self.data[self.i3]) / _number
        _number = self.data[self.i3] / _number
        return _number


class Check:
    def __init__(self, val1, val2, err_text):
        self.val1 = val1
        self.val2 = val2
        self.text = err_text

    def val1_more_than_val2(self):
        if self.val1 > self.val2:
            print(self.text)


if __name__ == '__main__':
    pass
