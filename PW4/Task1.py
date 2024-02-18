class OrdinaryFraction:
    def __init__(self, fraction):
        self.fraction = fraction

    def is_correct_fraction(self):
        x, y = self.fraction
        return ("Fraction is incorrect", "Fraction is correct")[x / y < 1]


fraction1 = OrdinaryFraction([int(x) for x in input("Enter 2 number: ").split(' ')])
print(OrdinaryFraction.is_correct_fraction(fraction1))
