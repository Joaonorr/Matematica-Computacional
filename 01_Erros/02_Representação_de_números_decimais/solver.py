def decimalRepresentation(number:float, base:int, precision:int, m:int, M:int):
    x = number
    integerPart = 0
    fractionalPart = 0.0
    binNumber = ""
    firstOne = False
    contZero = 0
    while True:
        _x = x * base
        integerPart = int(_x)
        fractionalPart = _x - integerPart
        if integerPart == 1:
            firstOne = True        
        if firstOne:
            binNumber += str(integerPart)
        else:
            contZero += 1
        if fractionalPart == 0.0 or len(binNumber) == precision:
            break
        x = fractionalPart

    return "0.{} -{}".format(binNumber, contZero)



def main():
    decimal = float(input())
    base, precision, m, M = map(int, input().split())

    print(decimalRepresentation(decimal, base, precision, m, M))

if __name__ == "__main__":
    main()