from fractions import Fraction

def absoluteError(realValue:float, aproxValue:float):
        return Fraction(str(realValue)) - Fraction(aproxValue) # calcula o erro absoluto

def decimalRepresentationFraction(number:float, base:int, precision:int, m:int, M:int):
    x = number # copia o numero decimal para x
    integerPart = 0 # parte inteira do numero
    fractionalPart = 0.0 # parte fracionaria do numero
    binNumber = "" # armazena a representacao binaria do numero
    firstOne = False # flag que indica se o primeiro 1 ja foi encontrado
    contZero = 0 # contador de zeros a esquerda do primeiro 1
    number_fractional = 0 # numero fracionario
    cont = 1 # contador de casas decimais
    while True:        
        _x = x * base
        integerPart = int(_x)
        fractionalPart = _x - integerPart
        if integerPart == 1: 
            number_fractional += 1 * Fraction(base** -cont) # soma a parte fracionaria do numero
            firstOne = True        
        cont += 1
        if firstOne:
            binNumber += str(integerPart)
        else:
            contZero += 1
        if fractionalPart == 0.0 or len(binNumber) == precision:
            break
        x = fractionalPart

    if contZero < m or contZero > M:
        return "underflow"
    else:
        return ("{}\n{}").format(Fraction(number_fractional), absoluteError(number, number_fractional))

def main():
    decimal = float(input())
    base, precision, m, M = map(int, input().split())

    print(decimalRepresentationFraction(decimal, base, precision, m, M))

if __name__ == "__main__":
    main()