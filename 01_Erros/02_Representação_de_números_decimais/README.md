# Representação de números decimais

Um sistema em ponto flutuante é definido por uma base *β*, por uma precisão *p* e por limitantes *m* e *M* para o valor do expoente. Para indicar um determinado sistema em ponto flutuante, escrevemos:

*F*(*β*, *p*, *m*, *M*)

Um número qualquer representado nesse sistema F é escrito da seguinte forma:

$x =  ± 0.d1d2…dp × β^e$

onde o expoente *e* é um inteiro tal que *m* ≤ *M* e *d*1 ≠ 0, pois a representação deve estar sempre normalizada e *d*1, *d*2, …, *dp* ∈ {0, 1, …, *β* − 1} 

Uma fração decimal (chamada simplesmente de números decimais em alguns contextos) é número racional que pode ser representado com frações cujo denominadores são potências de 10. Por exemplo, os decimais 0.8 e 14.89 representam as frações 8/10 e 1489/100.

Esses números decimais podem ser representados como aproximações em sistemas em ponto flutuante com a base diferente da base 10.

O processo de conversão de um número decimal para um número ponto flutuante na base β pode ser realizado da seguinte maneira. Multiplique o número x pela base β. Em seguida, calcule a parte inteira de β * x e a parte fracionária de β * x. Observe que se β * x ≥ 1 então x ≥ 1/β. Logo, se a parte inteira de β * x representa o primeiro dígito do número ponto flutuante x na base β. Em seguida, x recebe o valor da parte fracionária de β * x.

Considere que você queira representar número decimal 0.375 em um sistema em ponto flutuante com a base 2.


| x | 2*x | integerPart(2*x) | FractionalPart(2*x) |
| --- | --- | --- | --- |
| 0.375 | 0.75 | 0 | 0.75 |

O primeiro dígito de *x* no [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185) é 0.

Continuando o processo

| x | 2*x | integerPart(x) | FractionalPart(x) |
| --- | --- | --- | --- |
| 0.375 | 0.75 | 0 | 0.75 |
| 0.75 | 1.5 | 1 | 0.5 |

O segundo dígito de *x* no [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185) é 1.

Continuando o processo

| x | 2*x | integerPart(x) | FractionalPart(x) |
| 0.375 | 0.75 | 0 | 0.75 |
| 0.75 | 1.5 | 1 | 0.5 |
| --- | --- | --- | --- |
| 0.5 | 1.0 | 1 | 0.0 |

O terceiro dígito de *x* no [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185) é 1.

Logo, o número (0.375)10 é representado como (0.011)2. Como o primeiro dígito do [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185) não pode ser zero, então (0.011)2 = 0.11 × 2 − 1.

Observe que esse processo pode continuar indefinidamente. Neste caso, podemos interromper o processo considerando a precisão do nosso [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185).

Sua tarefa é dado um número decimal *x* e um sistema em ponto flutuante *F*(*β*, *p*, *m*, *M*), encontre a representação de *x* no sistema *F*.

**Entrada**

A entrada é composta por duas linhas. A primeira linha contém uma fração decimal. A segunda linha é composta por 4 números inteiros representando a base *β*, a precisão *p* e os limitantes do expoente *m* e *M*.

**Saída**

A saída é composta por uma string representando os dígitos do [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185) e um inteiro representando o expoente no [sistema em ponto flutuante](https://moodle2.quixada.ufc.br/mod/vpl/view.php?id=54185).

**Restrições:**

- *M* ≥ 0
- *m* ≤ 0
- *β* > 0
- *p* ≥ 0
- *x* < 0

**Entrada**

```
0.1
2 10 -5 5
```

**Saída**

```
0.1100110011 -3
```

**Entrada**

```
0.2
2 10 -5 5
```

**Saída**

```
0.1100110011 -2
```


# Resolução

### Podemos escrever uma função para converter um número decimal para um número ponto flutuante na base β. <br> Para isso, escreveremos uma função chamada <strong>decimalRepresentation</strong> que recebe como parâmetros respectivamente:
```python
numero:float # numero decimal
base:int # base do sistema
precisao:int # precisao do sistema
expoente_min:int # expoente minimo
expoente_max:int # expoente maximo
```
### E retorna uma <strong>string</strong> com a representação do número decimal no sistema ponto flutuante já normalizada.

### Desta forma, podemos escrever o código da seguinte forma:
```python
def decimalRepresentation(number:float, base:int, precision:int, m:int, M:int):
    x = number # copia o numero decimal para x
    integerPart = 0 # parte inteira do numero
    fractionalPart = 0.0 # parte fracionaria do numero
    binNumber = "" # armazena a representacao binaria do numero
    firstOne = False # flag que indica se o primeiro 1 ja foi encontrado
    contZero = 0 # contador de zeros a esquerda do primeiro 1
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
```

### Exemplos de saída:
```python
print(decimalRepresentation(0.1, 2, 10, -5, 5)) # 0.1100110011 -3
print(decimalRepresentation(0.2, 2, 10, -5, 5)) # 0.1100110011 -2
print(decimalRepresentation(0.3, 2, 10, -5, 5)) # 0.1001100110 -1
```

## Solução para avaliação automática
```python
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
```