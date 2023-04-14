from fractions import Fraction

class SystemFloat:
    def __init__(self, base:int, precision:int, min:int, max:int):
        self.base = base
        self.precision = precision
        self.min = min
        self.max = max

    def maxValue(self):
        sum = 0
        for i in range(self.precision):
            sum += Fraction(self.base - 1, self.base ** (i+1))
        return Fraction((self.base ** self.max) * (sum))
          
    def minValue(self):
        return Fraction(1 , self.base) * Fraction(1 , (self.base** -self.min))


def main():
    f = input()
    f = f.split(" ")
    base = int(f[0])
    precision = int(f[1])
    min = int(f[2])
    max = int(f[3])

    sf = SystemFloat(base, precision, min, max)

    maxValue = sf.maxValue()
    minValue = sf.minValue()

    print(maxValue) if '/' in str(maxValue) else print(str(maxValue) + "/1")
    print(minValue) if '/' in str(minValue) else print(str(minValue) + "/1")




if __name__ == "__main__":
    main()