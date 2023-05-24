# Busca Ternária

- [Problema](#problema)
    - [Entrada](#entrada)
    - [Saída](#saída)
    - [Exemplos](#exemplos)
    - [Dica](#dica)
- [Resolução](#resolução)
- [Solução](#solução)

# Problema
A busca ternária é um algoritmo de busca que divide o intervalo de busca em três partes iguais e realiza a busca em cada uma dessas partes. É uma variação da busca binária, que divide o intervalo de busca em duas partes iguais.

O funcionamento da busca ternária é simples:
- primeiro, é verificado se o elemento buscado está no primeiro terço do intervalo de busca. 
- Se estiver, a busca é realizada nesse terço. 
- Caso contrário, é verificado se o elemento está no segundo terço do intervalo. 
- Se estiver, a busca é realizada nesse terço. 
- Por fim, se o elemento não estiver nos dois primeiros terços, é verificado se ele está no terceiro terço do intervalo. 
- Se estiver, a busca é realizada nesse terço.

Dado um intervalo [l,h]:

    O primeiro intervalo [l,l+(h−l)/3]
    O segundo intervalo [l+(h−l)/3,l+2*(h−l)/3]
    O terceiro intervalo [l+2*(h−l)/3,h]

Dado um polinômio de grau $n$, um chute inicial da raiz da equação [l, h] e um tolerância, aplique o algoritmo de busca ternária para encontrar uma raiz da equação.

# Entrada

A entrada é composta por 4 linhas. A primeira linha contém um inteiro (2≤N≤9) representando o grau do polinômio. A segunda linha contém N+1 números reais. A terceira linha contém dois números reais l,h representando o chute inicial do intervalo da raiz. A quarta linha contém um número real denotando a tolerância utilizada no critério de parada.

# Saída

A saída é composta por duas linhas. A primeira linha contém a seguinte mensagem:

- busca ternaria realizou X iteracoes

A segunda linha contém a seguinte mensagem:

- a solucao está no intervalo [a,b]

- com a e b com 10 casas decimais.

# Exemplos

Entrada

    2
    -0.6 2.4 5.5
    5 10
    0.001

Saída

    busca ternaria realizou 9 iteracoes
    a solucao está no intervalo [5.627953056,5.628715135]

# Dica:

Modifique o seguinte algoritmo do método da bissecao:

```python
def calcular_f(n, a, x):
    resultado = 0
    for i in range(n+1):
        resultado = resultado * x + a[i]
    return resultado

def busca_binaria(n, a, limite_inferior, limite_superior, tolerancia):
    iteracao = 1
    while True:
        if abs(limite_superior - limite_inferior) < tolerancia:
            return limite_inferior, limite_superior, iteracao
        ponto_medio = limite_inferior + (limite_superior - limite_inferior) / 2
        if calcular_f(n, a, limite_inferior) * calcular_f(n, a, ponto_medio) < 0:
            limite_superior = ponto_medio
        else:
            limite_inferior = ponto_medio
        iteracao += 1

```

# Resolução

Primeiro, vamos fazer a função que calcula o valor do polinômio para um dado valor de x:

```python
def polinomio(x):
        # Inicialização do valor do polinômio
        valor_polinomio = 0

        # Cálculo do valor do polinômio
        for i in range(GRAU + 1):
            valor_polinomio += LISTA_COEFICIENTES[i] * x ** (GRAU - i)

        # Retorno do valor do polinômio
        return valor_polinomio
```

Agora, vamos fazer a função que realiza a busca ternária (note que a função polinomio(x) é chamada dentro da função busca_ternaria, pois ela é necessária apenas dentro dessa função, dessa forma, não é necessário declará-la globalmente, evita que ela seja acessada por outras partes do código e acaba recebendo menos parâmetros, pois não é necessário passar o grau do polinômio e a lista de coeficientes):

```python
def busca_ternaria(GRAU, LISTA_COEFICIENTES, chute_inicial, chute_final, TOLERANCIA):

    def polinomio(x):
        # Inicialização do valor do polinômio
        valor_polinomio = 0

        # Cálculo do valor do polinômio
        for i in range(GRAU + 1):
            valor_polinomio += LISTA_COEFICIENTES[i] * x ** (GRAU - i)

        # Retorno do valor do polinômio
        return valor_polinomio

    # Define o número de iterações
    numero_iteracoes = 1

    while (chute_final - chute_inicial) > TOLERANCIA:
        # Definição dos intervalos
        intervalo = (chute_final - chute_inicial)/3

        # Definição dos pontos
        ponto1 = chute_inicial + intervalo
        ponto2 = chute_final - intervalo

        # Verificação do intervalo que contém a raiz
        if polinomio(chute_final) * polinomio(ponto2) < 0:
            # Atualização do intervalo
            chute_inicial = ponto2
        elif polinomio(chute_inicial) * polinomio(ponto1) < 0:
            # Atualização do intervalo
            chute_final = ponto1
        else:
            # Atualização do intervalo
            chute_inicial = ponto1
            chute_final = ponto2

        # Incremento do número de iterações
        numero_iteracoes += 1

    # Impressão do resultado
    print("busca ternaria realizou " + str(numero_iteracoes) + " iteracoes")
    print("a solucao está no intervalo [{:.9f},{:.9f}]".format(chute_inicial, chute_final))
```

Por fim, vamos fazer a leitura dos dados de entrada e a chamada da função busca_ternaria:

```python
def main():
    # Leitura do grau do polinômio
    GRAU = int(input())

    # Leitura dos coeficientes do polinômio
    LISTA_COEFICIENTES = list(map(float, input().split()))

    # Leitura do chute inicial do intervalo da raiz
    CHUTE_INICIAL, CHUTE_FINAL = map(float, input().split())

    # Leitura da tolerância utilizada no critério de parada
    TOLERANCIA = float(input())

    # Impressão do resultado
    busca_ternaria(GRAU, LISTA_COEFICIENTES, CHUTE_INICIAL, CHUTE_FINAL, TOLERANCIA)

if __name__ == "__main__":
    main()
```

# Código completo:

```python
import math

def busca_ternaria(GRAU, LISTA_COEFICIENTES, chute_inicial, chute_final, TOLERANCIA):

    def polinomio(x):
        # Inicialização do valor do polinômio
        valor_polinomio = 0

        # Cálculo do valor do polinômio
        for i in range(GRAU + 1):
            valor_polinomio += LISTA_COEFICIENTES[i] * x ** (GRAU - i)

        # Retorno do valor do polinômio
        return valor_polinomio

    # Define o número de iterações
    numero_iteracoes = 1

    while (chute_final - chute_inicial) > TOLERANCIA:
        # Definição dos intervalos
        intervalo = (chute_final - chute_inicial)/3

        # Definição dos pontos
        ponto1 = chute_inicial + intervalo
        ponto2 = chute_final - intervalo

        # Verificação do intervalo que contém a raiz
        if polinomio(chute_final) * polinomio(ponto2) < 0:
            # Atualização do intervalo
            chute_inicial = ponto2
        elif polinomio(chute_inicial) * polinomio(ponto1) < 0:
            # Atualização do intervalo
            chute_final = ponto1
        else:
            # Atualização do intervalo
            chute_inicial = ponto1
            chute_final = ponto2

        # Incremento do número de iterações
        numero_iteracoes += 1

    # Impressão do resultado
    print("busca ternaria realizou " + str(numero_iteracoes) + " iteracoes")
    print("a solucao está no intervalo [{:.9f},{:.9f}]".format(chute_inicial, chute_final))

def main():
    # Leitura do grau do polinômio
    GRAU = int(input())

    # Leitura dos coeficientes do polinômio
    LISTA_COEFICIENTES = list(map(float, input().split()))

    # Leitura do chute inicial do intervalo da raiz
    CHUTE_INICIAL, CHUTE_FINAL = map(float, input().split())

    # Leitura da tolerância utilizada no critério de parada
    TOLERANCIA = float(input())

    # Impressão do resultado
    busca_ternaria(GRAU, LISTA_COEFICIENTES, CHUTE_INICIAL, CHUTE_FINAL, TOLERANCIA)

if __name__ == "__main__":
    main()
```