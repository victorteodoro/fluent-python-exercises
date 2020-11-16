from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool_(self):
        return bool(abs(self))

    def __add__(self, otherVector):
        return Vector(self.x + otherVector.x, self.y + otherVector.y)

    def __sub__(self, otherVector):
        return Vector(self.x - otherVector.x, self.y - otherVector.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)


firstVector = Vector(3, 4)
secondVector = Vector(5, 12)

print("The first vector is", firstVector)
print("The second vector is", secondVector)

print("The size of the first vector is", abs(firstVector))
print("The size of the second vector is", abs(secondVector))

print("Is the first vector true?", bool(firstVector))
print("Is the second vector true?", bool(secondVector))

print("The sum of the vectors is", firstVector + secondVector)

print("The first vector times 3 is", firstVector * 3)
print("The second vector times 3 is", secondVector * 3)

print("Three times the first vector is", 3 * firstVector)
print("Three times the second vector is", 3 * secondVector)

print("Three times the first vector times 3 is", 3 * firstVector * 3)
print("Three times the second vector times 3 is", 3 * secondVector * 3)
