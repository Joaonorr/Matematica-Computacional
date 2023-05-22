# Paraquedismo

A velocidade de um paraquedista em queda livre é dado por

$$
v = \frac{gm}{c} (1-e^{-\frac{c}{m}t})
$$

onde

- $g$ representa a gravidade ($9,8m/s^2$)
- $m$ representa a massa do paraquedista.
- $c$ representa coeficiente de arrasto
- $t$ representa o tempo

Um paraquedista deseja atingir uma velocidade máxima de $V m/s$ em seu salto de paraquedas. Determine a massa mínima do seu corpo, considerando que ele está usando um paraquedas com um coeficiente de arrasto de $C Kg/s$ e que ele deseja atingir a velocidade máxima $V$ em $t$ segundos após a abertura do paraquedas. Considere que a massa do paraquedista está entre 50 e 100 kg. Resolva com o método da bisseção considerando como critério de parada quando o intervalo da solução for menor 0.001.

# Entrada

A entrada é composta por três números $c, v, t$ representando o coeficiente de arrasto, a velocidade máxima que o paraquedista deseja atingir e o tempo após a abertura do paraquedas.

# Saída

A saída é composta de uma única linha contendo a massa mínima do paraquedista com 2 casas decimais.

# Exemplos

Entrada

    15 35 9

Saída

    59.84

---

Entrada

    20 35 9 

Saída

    79.79

# Resolução

Para resolver esse problema, vamos utilizar o método da bisseção. Para isso, vamos definir uma função que recebe o valor de $m$ e retorna o valor de $v$.

- constantes estão definidas em maiúsculo
- variáveis estão definidas em minúsculo


```python
def velocidade(COEF_ARRASTO: float, MASSA: float, TEMPO: float) -> float:
    
    VELOCIDADE = (9.8*MASSA/COEF_ARRASTO)*(1-math.exp(-COEF_ARRASTO/MASSA*TEMPO))
    
    return VELOCIDADE
```

Vamos definir também a função de bisseção, que recebe os valores de $c, v, t$ e retorna o valor de $m$.

```python
# Função que calcula a massa mínima do paraquedista
def bissecao(COEF_ARRASTO: float, VELOCIDADE_MAX: float, TEMPO: float, MASSA_1: int, MASSA_2: int) -> float:
    
    # Enquanto a diferença entre as massas for maior que 0.001
    while math.fabs(MASSA_2 - MASSA_1)/2 > 0.001:
        
        MASSA_INTE = (MASSA_1 + MASSA_2)/2 # Calcula a massa intermediária

        if velocidade(COEF_ARRASTO, MASSA_INTE, TEMPO) < VELOCIDADE_MAX:
            MASSA_1 = MASSA_INTE
        else:
            MASSA_2 = MASSA_INTE

    return MASSA_INTE
```

Note que a função de bisseção recebe dois valores de massa, que são os limites do intervalo. Para resolver o problema, vamos definir esses valores como 50 e 100, que são os valores mínimos e máximos da massa do paraquedista.

Na função principal, vamos ler os valores de $c, v, t$ e chamar a função de bisseção.

```python
def main():

    MASSA_1 = 50

    MASSA_2 = 100

    COEF_ARRASTO, VELOCIDADE_MAX, TEMPO = map(float, input().split())

    MASSA_MINIMA = bissecao(COEF_ARRASTO, VELOCIDADE_MAX, TEMPO, MASSA_1, MASSA_2)

    print(truncar_numero_decimal(MASSA_MINIMA, 2))
```

A função `truncar_numero_decimal` é utilizada para truncar o número de casas decimais de um número. Ela recebe o número e a quantidade de casas decimais que devem ser mantidas.

```python
# Função que trunca um número decimal
def truncar_numero_decimal(numero, casas_decimais):
    string_formatada = '%.12f' % numero

    parte_inteira, separador, parte_decimal = string_formatada.partition('.')

    parte_decimal_truncada = (parte_decimal + '0' * casas_decimais)[:casas_decimais]

    numero_truncado = '.'.join([parte_inteira, parte_decimal_truncada])

    return numero_truncado
```

O código completo pode ser visto abaixo.

```python
import math

# Função que trunca um número decimal
def truncar_numero_decimal(numero, casas_decimais):
    string_formatada = '%.12f' % numero
    parte_inteira, separador, parte_decimal = string_formatada.partition('.')
    parte_decimal_truncada = (parte_decimal + '0' * casas_decimais)[:casas_decimais]
    numero_truncado = '.'.join([parte_inteira, parte_decimal_truncada])
    return numero_truncado

# Função que calcula a velocidade do paraquedista
def velocidade(COEF_ARRASTO: float, MASSA: float, TEMPO: float) -> float:
    
    VELOCIDADE = (9.8*MASSA/COEF_ARRASTO)*(1-math.exp(-COEF_ARRASTO/MASSA*TEMPO))
    
    return VELOCIDADE

# Função que calcula a massa mínima do paraquedista
def bissecao(COEF_ARRASTO: float, VELOCIDADE_MAX: float, TEMPO: float, MASSA_1: int, MASSA_2: int) -> float:
    
    # Enquanto a diferença entre as massas for maior que 0.001
    while math.fabs(MASSA_2 - MASSA_1)/2 > 0.001:
        
        massa_inter = (MASSA_1 + MASSA_2)/2 # Calcula a massa intermediária

        if velocidade(COEF_ARRASTO, massa_inter, TEMPO) < VELOCIDADE_MAX:
            MASSA_1 = massa_inter
        else:
            MASSA_2 = massa_inter

    return massa_inter

def main():

    MASSA_1 = 50

    MASSA_2 = 100

    COEF_ARRASTO, VELOCIDADE_MAX, TEMPO = map(float, input().split())

    MASSA_MINIMA = bissecao(COEF_ARRASTO, VELOCIDADE_MAX, TEMPO, MASSA_1, MASSA_2)

    print(truncar_numero_decimal(MASSA_MINIMA, 2))

if __name__ == '__main__':
    main()
```

