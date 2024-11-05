#OPERATOR OVERLOAD
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

vector1 = Vector(1, 2)
vector2 = Vector(6, 4)
#operator overload
result_vector = vector1 + vector2

print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Result vector: {result_vector}")
