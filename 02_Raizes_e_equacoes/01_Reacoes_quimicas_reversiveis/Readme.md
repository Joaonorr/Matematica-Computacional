# Reações Químicas Reversíveis

As reações químicas reversíveis são aquelas que podem ocorrer tanto no sentido direto como no sentido inverso, ou seja, pode ser revertidas.

Por exemplo:

$$
2A + B \leftrightarrow C
$$

pode ser caracterizada pela seguinte relação de equilíbrio:

$$
K = \frac{C_c}{C_a^{2}C_b}
$$

onde $K$ é a constante de equilíbrio, $C_c$ é a concentração de $C$ e $C_a$ e $C_b$ são as concentrações de $A$ e $B$, respectivamente.

Vamos definir uma variável x representando o número de mols de C produzidos. A conservação de massa pode ser usada para reformular a relação de equilíbrio como

$$
K = \frac{C_{c_{0}}+x}{(C_{a_{0}}-2x)²(C_{b_{0}}-x)}
$$

Onde $C_{c_{0}}$, $C_{a_{0}}$ e $C_{b_{0}}$ são as concentrações iniciais de $C$, $A$ e $B$, respectivamente.

Dado o valor de $K$ e as concentrações iniciais $C_{c_{0}}$, $C_{a_{0}}$ e $C_{b_{0}}$, determine o valor de $x$ considerando o chute inicial de $x_{l}$ e $x_{u}$ com $n$ algarismos significativos, ou seja, o intervalo de (a, b) possui uma solução aproximada se $|b-a|$ é menor de $0.5 \times 10^{-n}$. 

## Entrada

A entrada é composta por um linha com 7 valores reais separados por espaço, sendo eles, respectivamente, $K$, $C_{a_{0}}$, $C_{b_{0}}$, $C_{c_{0}}$, $x_{l}$, $x_{u} $ e $ \epsilon $.

Os valores representam, respectivamente, a constante de equilíbrio, as concentrações iniciais de $A$, $B$ e $C$, o chute inicial inferior e superior do número de mols produzidos por $C$ e o limite de erro aceito.

## Saída

A saída é composta de uma única linha contendo o número de mols produzidos de $C$ com $n$ casas decimais. A solução deve ser truncada para $n$ casas decimais.

## Utilize a seguinte função:
    
```python
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
```

## Exemplos

Entrada

    0.016 42 28 4 0 20 2

Saída

    15.92
---

Entrada

    0.012 42 28 4 0 20 2

Saída

    15.35

# Resolução

Para resolver esse problema, vamos utilizar o método da bisseção. Para isso, vamos definir uma função que recebe o valor de $x$ e retorna o valor de $K$.
Note que estamos utilizando valores de $C_{a_{0}}$, $C_{b_{0}}$ e $C_{c_{0}}$ iguais a 42, 28 e 4, respectivamente apenas para facilitar a implementação.

```python
def f(x):
    return (4+x)/((42-2*x)**2*(28-x))
```

Agora, vamos definir a função que calcula o valor de $x$ utilizando o método da bisseção.

De forma simplificada, o método da bisseção consiste em dividir o intervalo de busca pela metade e verificar em qual dos dois intervalos a solução se encontra. Esse processo é repetido até que o intervalo de busca seja menor que o erro aceito.

```python
def bissecao(a, b, epsilon):
    if f(a)*f(b) > 0: # Se f(a) e f(b) possuem o mesmo sinal, não há solução
        return None
    else:
        while abs(b-a) > epsilon: # Enquanto o intervalo de busca for maior que o erro aceito
            x = (a+b)/2
            if f(x) == 0: # Se f(x) = 0, x é a solução
                return x
            elif f(a)*f(x) < 0: # Se f(a) e f(x) possuem sinais diferentes, a solução está no intervalo (a, x)
                b = x
            else: # Se f(b) e f(x) possuem sinais diferentes, a solução está no intervalo (x, b)
                a = x
        return x 
```

Agora, vamos ler os valores de entrada e chamar a função `bissecao` com os valores lidos.

```python
K, Ca0, Cb0, Cc0, xl, xu, epsilon = map(float, input().split())

x = bissecao(xl, xu, epsilon)
```

Por fim, vamos imprimir o valor de $x$ com 2 casas decimais.

```python
print(truncate(x, 2))
```
