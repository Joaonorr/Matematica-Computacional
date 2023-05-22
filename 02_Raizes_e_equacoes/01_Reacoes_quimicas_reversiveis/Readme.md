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
def concentracao(mols):
    return (CONC_C_0 + mols) / (((CONC_A_0 - 2*mols)**2) * (CONC_B_0 - mols))
```

Agora, vamos definir a função que calcula o valor de $x$ utilizando o método da bisseção.

De forma simplificada, o método da bisseção consiste em dividir o intervalo de busca pela metade e verificar em qual dos dois intervalos a solução se encontra. Esse processo é repetido até que o intervalo de busca seja menor que o erro aceito.

```python
def bissecao(CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, mols_inicial, mols_final, ERRO_ACEITO):
    # Função que retorna a concentração de C em função do número de mols de C
    def concentracao(mols):
        return (CONC_C_0 + mols) / (((CONC_A_0 - 2*mols)**2) * (CONC_B_0 - mols))
    #
    while math.fabs(mols_final - mols_inicial)/2 >= 1*10**(-ERRO_ACEITO-1):
        # Calcula o número de mols do intermediário
        mols_intermediario = (mols_inicial + mols_final)/2
        # Verifica se a concentração do intermediário é menor que a concentração desejada
        if concentracao(mols_intermediario) < CONCENTRACAO:

            mols_inicial = mols_intermediario

        else:

            mols_final = mols_intermediario

    return mols_intermediario
```

Agora, vamos ler os valores de entrada e chamar a função `bissecao` com os valores lidos.

```python
CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, MOLS_INICIAL, MOLS_FINAL, ERRO_ACEITO = map(float, input().split())
    
x = bissecao(CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, MOLS_INICIAL, MOLS_FINAL, ERRO_ACEITO)

```

Por fim, vamos imprimir o valor de $x$ com 2 casas decimais.

```python
print(truncar_numero_decimal(x, int(ERRO_ACEITO)))
```

Onde a função `truncar_numero_decimal` é definida como:

```python
def truncar_numero_decimal(numero, casas_decimais):
    # Função que retorna o número truncado com a quantidade de casas decimais desejada
    string_formatada = '%.12f' % numero
    # Separa a parte inteira da parte decimal
    parte_inteira, separador, parte_decimal = string_formatada.partition('.')
    # Trunca a parte decimal
    parte_decimal_truncada = (parte_decimal + '0' * casas_decimais)[:casas_decimais]
    # Junta a parte inteira com a parte decimal truncada
    numero_truncado = '.'.join([parte_inteira, parte_decimal_truncada])
    # Retorna o número truncado
    return numero_truncado
```

O código completo é mostrado abaixo.

```python
import math

def truncar_numero_decimal(numero, casas_decimais):

    string_formatada = '%.12f' % numero

    parte_inteira, separador, parte_decimal = string_formatada.partition('.')
    
    parte_decimal_truncada = (parte_decimal + '0' * casas_decimais)[:casas_decimais]

    numero_truncado = '.'.join([parte_inteira, parte_decimal_truncada])
    
    return numero_truncado


def bissecao(CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, mols_inicial, mols_final, ERRO_ACEITO):
    
    def concentracao(mols):
        return (CONC_C_0 + mols) / (((CONC_A_0 - 2*mols)**2) * (CONC_B_0 - mols))

    while math.fabs(mols_final - mols_inicial)/2 >= 1*10**(-ERRO_ACEITO-1):

        mols_intermediario = (mols_inicial + mols_final)/2

        if concentracao(mols_intermediario) < CONCENTRACAO:

            mols_inicial = mols_intermediario

        else:

            mols_final = mols_intermediario

    return mols_intermediario


def main():
    CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, MOLS_INICIAL, MOLS_FINAL, ERRO_ACEITO = map(float, input().split())
    
    x = bissecao(CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, MOLS_INICIAL, MOLS_FINAL, ERRO_ACEITO)

    print(truncar_numero_decimal(x, int(ERRO_ACEITO)))


if __name__ == '__main__':
    main()
```