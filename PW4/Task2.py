class Vector:
    def __init__(self, vector_a, vector_b):
        self.vector_a = vector_a
        self.vector_b = vector_b

    def vectors_addition(self):
        x1, y1 = self.vector_a
        x2, y2 = self.vector_b
        return [x1 + x2, y1 + y2]

    def vector_subtraction(self):
        x1, y1 = self.vector_a
        x2, y2 = self.vector_b
        return [x1 - x2, y1 - y2]


Vector1 = Vector([int(a) for a in input("Enter the coordinates of vector A: ").split(' ')],
                 [int(b) for b in input("Enter the coordinates of vector B: ").split(' ')])
print(f"Сума векторів A та B: {Vector.vectors_addition(Vector1)} "
      f"\nРізниця векторів A та B: {Vector.vector_subtraction(Vector1)}")
