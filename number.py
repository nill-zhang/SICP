from math import atan,cos,sin


class Number(object):
    """ base class for all the types defined later"""
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.__mul__(other)


class Complex(Number):
    """ base class for Complex numbers with different representations"""
    def add(self, other):
        return ComplexRI(self.real+other.real, self.imag+other.imag)

    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        angle = self.angle + other.angle
        return ComplexMA(magnitude, angle)


class ComplexRI(Complex):

    def __init__(self, real, imag):
        self.imag = imag
        self.real = real

    @property
    def magnitude(self):
        return (self.real**2+self.imag**2)**(1/2)

    @property
    def angle(self):
        return atan(self.imag, self.real)


class ComplexMA(Complex):

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

#todo rational number
#todo test

if __name__ == "__main__":
    pass
