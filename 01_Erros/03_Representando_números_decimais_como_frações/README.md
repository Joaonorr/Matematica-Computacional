# Representando números decimais como frações

O número decimal $(0.375)_{10}$ pode ser representado no sistema em ponto flutuante $F(2, 5, -2, 2)$ como:<br>
$$0.11 × 2 ^{− 1}$$
<br>ou seja, 

$$
\begin{matrix}
(\frac{1}{2} + \frac{1}{4}) × 2 ^{− 1} &=&
                         (\frac{1}{4} + \frac{1}{8})\\ \\&=&
                                     \frac{3}{8}
\end{matrix}
$$
Neste caso, o erro absoluto da representação é 0.

Já o número $(0.1)_{10}$ pode ser representado no sistema ponto flutuante $F(2, 5,  − 5, 5)$ como $(0.11001) × 2^{−3}$ que pode ser representado como fração da seguinte maneira:<br>


$$
\begin{matrix}
(\frac{1}{2} + \frac{1}{4} + \frac{1}{32}) × 2 ^{− 3} &=&
                         (\frac{1}{16} + \frac{1}{32} + \frac{1}{256})\\ \\&=&
                                     \frac{25}{256}
                                    \\
\end{matrix}
$$

Note que o erro absoluto dessa representação é:

$$
\begin{matrix}
\\
\frac{1}{10} − \frac{25}{256} &=&
                         \frac{6}{2560}\\ \\&=&
                                     \frac{3}{1280}
\end{matrix}
$$

### Entrada
A entrada é composta por duas linhas. A primeira linha contém uma fração decimal. A segunda linha é composta por 4 números inteiros representando a base β, a precisão *p* e os limitantes do expoente *m* e *M*.

### Saída
A saída é composta por duas linhas. A primeira linha é composta por uma fração relacionada com representação da fração decimal no sistema em ponto flutuante *F(β, p, m, M)*. A segunda linha é composta por uma fração relacionada com o erro absoluto da representação no sistema em ponto flutuante *F(β, p, m, M)*.

### Restrições:

- M ≥ 0
- m ≤ 0
- β > 0
- p ≥ 0
- x < 0

Entrada

    0.1
    2 5 -5 5
Saída

    25/256
    3/1280

---
Entrada

    0.01 
    2 5 -5 5
Saída

    underflow  
---
Entrada

    0.01
    2 5 -6 6
Saída

    5/512
    3/12800
---
Entrada

    0.01
    2 10 -6 6
Saída

    655/65536
    9/1638400

---

# Resolução
Para a resolução deste problema, podemos escrever uma função para realizar a conversão de um número decimal para a base β, chamaremos ela de _decimalRepresentationFraction_.
A função recebe como parâmetros:
```python
numero:float # numero decimal
base:int # base do sistema
precisao:int # precisao do sistema
expoente_min:int # expoente minimo
expoente_max:int # expoente maximo
```
E retorna uma string com a representação do número e a taxa de erro.
obs: caso o número seja menor que o expoente mínimo, retorna a string "underflow"

O código da função é o seguinte:
```python
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
```

Você pode ver que a taxa de erro é calculada pela função _absoluteError_ que recebe como parâmetros o número decimal e a representação do número no sistema ponto flutuante.
```python
number:float # numero decimal
number_fractional:float # numero fracionario
```
E retorna a taxa de erro.

O código da função _absoluteError_ é o seguinte:
```python
def absoluteError(realValue:float, aproxValue:float):
        return Fraction(str(realValue)) - Fraction(aproxValue) # calcula o erro absoluto

```

Exemplos de saída:
```python
print(decimalRepresentationFraction(0.1, 2, 5, -5, 5)) # 25/256↵3/1280

print(decimalRepresentationFraction(0.01, 2, 5, -5, 5)) # underflow

print(decimalRepresentationFraction(0.01, 2, 5, -6, 6)) # 5/512↵3/12800

print(decimalRepresentationFraction(0.01, 2, 10, -6, 6)) # 655/65536↵9/1638400
```

Solução para avaliação automática:
```python
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
```