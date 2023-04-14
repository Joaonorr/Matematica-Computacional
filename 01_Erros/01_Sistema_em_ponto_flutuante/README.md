# Sistema em ponto flutuante

Um sistema em ponto flutuante é definido por uma base *β*, por uma precisão *p* e por limitantes *m* e *M* para o valor do expoente. Para indicar um determinado sistema em ponto flutuante, escrevemos:

*F*(*β*, *p*, *m*, *M*)

Um número qualquer representado nesse sistema F é escrito da seguinte forma:

$x =  ± 0.d1d2…dp × β^e$

onde o expoente *e* é um inteiro tal que *m* ≤ *M* e *d*1 ≠ 0, pois a representação deve estar sempre normalizada e *d*1, *d*2, …, *dp* ∈ {0, 1, …, *β* − 1} 

Sua tarefa é dado um sistema em ponto flutuante devolva o menor e o maior número representado nesse sistema F como uma fração.

**Entrada**

A entrada é composta por 4 números inteiros representando a base *β*, a precisão *p* e os limitantes do expoente *m* e *M*.

**Saída**

A saída é composta por dois números inteiros representando o numerador e o denominador do maior e do menor número representado no sistema em ponto flutuante.

**Restrições:**

- *M* ≥ 0
- *m* ≤ 0
- *β* > 0
- *p* ≥ 0

**Entrada**

```bash
10 4 -3 3
```

**Saída**

```bash
9999/10 
1/10000
```

---

**Entrada**

```bash
2 3 -3 3
```

**Saída**
```bash
7/1
1/16
```

# Resolução
    
Os sistemas computacionais representam os números reais por meio de um sistema de numeração em ponto flutuante com uma forma geral onde :

$$
F(β,p,m,M)
$$

- β é a base
- p é a precisão
- m é valor mínimo que o expoente pode assumir
- M é o valor máximo que o expoente pode assumir
---
## Maior valor:
O maior valor pode ser achado da seguinte forma:

$$
β^M * \sum\limits_{i = 1}^{p} \frac{β - 1}{β^i}
$$

Que pode ser escrita da seguinte forma na linguagem python:

```python
from fractions import Fraction

def maxValue(β, p, M):
    sum = 0
    for i in range(p):
        sum += Fraction(β - 1, β ** (i+1))
    return Fraction((β ** M) * (sum))

print(maxValue(2, 3, 3)) # Fraction(7, 1)
print(maxValue(3, 3, 4)) # Fraction(78, 1)
print(maxValue(2, 5, 10)) # Fraction(992, 1)
print(maxValue(10, 4, 3)) # Fraction(9999, 10)
```
---
## Menor valor:
O menor valor pode se achado da seguinte forma:

$$
\frac{1}{β} * \frac{1}{β^{-m}}
$$

Também podemos escrever da seguinte forma na linguagem python:

```python
from fractions import Fraction

def minValue(β, p, m):
        return Fraction(1 , β) * Fraction(1 , (β ** -m))

print(minValue(2, 3, -3)) # Fraction(1, 16)
print(minValue(3, 3, -4)) # Fraction(1, 243)
print(minValue(2, 5, -10)) # Fraction(1, 2048)
print(minValue(10, 4, -3)) # Fraction(1, 10000)
```
---
## Solução para avaliação automática:
```python
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
```