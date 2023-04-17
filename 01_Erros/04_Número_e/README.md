# Número *e*

O número *e* pode ser calculado através da seguinte série:

$$
    e = \sum_{n=0}^{\infty} \frac{1}{n!}
$$

Podemos estimar o erro de aproximação para o valor *e* calculando a diferença entre a aproximação atual e proximação anterior. Para calcular o erro de aproximação relativo, podemos calcular da seguinte maneira:

$$
    error_{relativo} = \frac{e_{n} - e_{n-1}}{e_n}
$$

Onde $e_n$ é o valor de *e* calculado na iteração $n$.
Outra maneira de representar o cálculo do erro de aproximação relativo é:

$$
error_{relativo} = \frac{aproximacao_{atual} - aproximacao_{anterior}}
{aproximacao_{atual}}
$$

Ou seja, o erro de aproximação relativo é a diferença entre a aproximação atual e a aproximação anterior dividida pela aproximação atual.

Termo | aproximacao | erro_relativo (ε)
--- | --- | ---
1 | 1 |
2 | 2 | 0.5
3 | 2.5000000000 | 0.2000000000
4 | 2.6666666667 | 0.0625000000

Quando esse erro de aproximação relativo for menor que um certo ε podemos aceitar a aproximação atual de *e*
.

Sua tarefa é encontrar uma aproximação de *e* considerando que o erro de aproximação relativo deve ser menor que um valor ε
.

## Entrada

A entrada é composta por um número ponto flutuante com precisão dupla representando o valor de ε.

## Saída

A saída é composta por uma única linha contendo uma aproximação de *e* tal que o erro de aproximação relativo de *e* seja menor que ε. <br> 
<strong>Imprima essa aproximação com 15 casas decimais.</strong>

Entrada

    0.1
Saída

    2.666666666666667

---
Entrada

    0.01
Saída

    2.716666666666666

---
Entrada

    0.001
Saída

    2.718055555555555

# Resolução

Para resolver este problema, podemos escrever uma função que calcula o valor de *e* e outra função que calcula o erro de relativo.

A função que calcula o erro relativo:

```python
def relativeError(current_approach:float, previous_approach:float):
    return (current_approach - previous_approach) / current_approach # calcula o erro relativo
```
---

A função que calcula o valor de *e* é a seguinte:

```python
def epsilon(error:float):
    n = 1
    e_approach = 1/factorial(0) # atual valor de e
    e_previous = 0.0 # valor do e anterior
    while True:
        e_previous = e_approach # atualiza o valor do e anterior
        e_approach += 1/factorial(n) # atualiza o valor de e
        if relativeError(e_approach, e_previous) < error: # verifica se o erro relativo é menor que o erro
            break
        n += 1 # atualiza o valor de n
    return "{:.15}".format(e_approach) # retorna o valor de e com 15 casas decimais
```
Exemplos de saída da função que calcula o valor de *e*:
```python
print(epsilon(0.1)) # 2.66666666666667
print(epsilon(0.01)) # 2.71666666666667
print(epsilon(0.001)) # 2.71805555555556
```

---
A função que calcula o fatorial de um número *n* utilizada na função que calcula o valor de *e* é a seguinte:

```python
def factorial(n:int):
    if n == 0: 
        return 1 # caso base
    else: 
        return n * factorial(n-1) # caso recursivo
```

Exemplos de saída da função que calcula o fatorial:
```python	
print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(5)) # 120
print(factorial(10)) # 3628800
```

---
# Solução para avaliação automática

```python
def factorial(n:int):
    if n == 0: 
        return 1 # caso base
    else: 
        return n * factorial(n-1) # caso recursivo

def relativeError(current_approach:float, previous_approach:float):
    return (current_approach - previous_approach) / current_approach # calcula o erro relativo

def epsilon(error:float):
    n = 1
    e_approach = 1/factorial(0) # atual valor de e
    e_previous = 0.0 # valor do e anterior
    while True:
        e_previous = e_approach # atualiza o valor do e anterior
        e_approach += 1/factorial(n) # atualiza o valor de e
        if relativeError(e_approach, e_previous) < error: # verifica se o erro relativo é menor que o erro
            break
        n += 1 # atualiza o valor de n
    return "{:.15}".format(e_approach) # retorna o valor de e com 15 casas decimais

        
def main():
    error = float(input())
    print(epsilon(error))


if __name__ == "__main__":
    main()
```

