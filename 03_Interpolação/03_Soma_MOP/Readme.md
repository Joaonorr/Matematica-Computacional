# Soma MOP

- [Descrição](#descrição)
- [Entrada](#entrada)
- [Exemplos](#exemplos)
- [Solução](#solução)

## Descrição
Se nos são apresentados os primeiros k termos de uma sequência, é impossível dizer com certeza o valor do próximo termo, pois existem infinitamente muitas funções polinomiais que podem modelar a sequência.

Como exemplo, vamos considerar a seqüência de números de cubo. Isso é definido pela função geradora,

$$n3:(1,8,27,64,125,216,...)$$

Suponha que só recebêssemos os dois primeiros termos dessa sequência. Trabalhando no princípio de que “simples é melhor”, devemos assumir um relacionamento linear e prever que o próximo elemento seja $15 (8-1 = 7 = 15- 8)$. Mesmo se nos apresentassem os três primeiros termos, pelo mesmo princípio de simplicidade, um relacionamento quadrático deveria ser assumido.

Definiremos $OP(k,n)$ como o n-ésimo termo da função geradora polinomial ótima para os primeiros k termos de uma sequência. Deve ficar claro que $OP(k,n)$ irá gerar com precisão os termos da sequência para $n≤k$, e potencialmente o primeiro termo incorreto será $OP(k,k+1)$; em qual caso nós chamaremos isto de um $MOP$ (Mal OP).

Como base, se nos fosse dado apenas o primeiro termo de seqüência, seria mais sensato assumir constância; isto é, para $n≥2$, $OP(1,n)=a_{0}.$

Assim, obtemos os seguintes OPs para a seqüência cúbica:

$$OP(1,n)=1:(1,𝟏,1,1,...)$$

$$OP(2,n)=7n−6:(1,8,𝟏𝟓,...)$$

$$OP(3,n)=6n2−11n+6:(1,8,27,𝟓𝟖,...)$$

$$OP(4,n)=n3:(1,8,27,64,125,...)$$

Claramente, não existem $MOPs$ para $k ≥ 4$.

Considerando a soma dos $MOPs$, obtemos $1 + 15 + 58 = 74.$

Encontre a soma MOPs para um função geradora de uma sequência.

## Entrada

A entrada possui duas linhas. A primeira linha contém um inteiro D representando o grau do polinômio dado. A segunda linha $N+1$ inteiros representando $a_{d}, a_{d-1}, a_{0}$ representando os coeficientes do grau do polinômio dado tal que

$$P(n)=a_{0}+a_{1}n+a_{2}n^{2}+…+a_{D}n^{D}$$

Saída Devolve um inteiro representando a soma dos MOPS obtidas pelos polinômios $OP(1,N)+OP(2,N)+…+OP(D-1,N)$

## Exemplos

Entrada

    3
    1 0 0 0

Saída

    74

---

Entrada

    4
    1 -1 1 -1 1

Saída

    670

## Solução

O código abaixo resolve o problema. A solução é baseada na fórmula de Lagrange para interpolação polinomial. A fórmula de Lagrange é dada por:

$$P(x)=\sum_{i=0}^{n}y_{i}\prod_{j=0,j\neq i}^{n}\frac{x-x_{j}}{x_{i}-x_{j}}$$

Onde $x_{i}$ são os pontos conhecidos e $y_{i}$ são os valores correspondentes a esses pontos. No caso do problema, os pontos conhecidos são os valores de $OP(k,n)$ para $k=1,2,...,D-1$ e $n=1,2,...,N$. Os valores correspondentes são os valores de $OP(k,n)$ para $k=1,2,...,D-1$ e $n=k+1$. O código abaixo calcula os valores de $OP(k,n)$ para $k=1,2,...,D-1$ e $n=1,2,...,N$ e depois calcula os valores de $OP(k,n)$ para $k=1,2,...,D-1$ e $n=k+1$ usando a fórmula de Lagrange. Por fim, calcula a soma dos valores de $OP(k,n)$ para $k=1,2,...,D-1$ e $n=k+1$.

```python
def prod(lista):
    resultado = 1
    for x in lista:
        resultado *= x
    return resultado
    
def calcular_L(i, x):
    n = len(x)
    
    def calcular_num(a):
        return prod([(a - x[j]) for j in range(n) if j != i])
    
    den = prod([(x[i] - x[j]) for j in range(n) if j != i])
    
    return lambda a: calcular_num(a) / den
     
def calcular_PolinomioLagrange(x, y):
    if len(x) != len(y):
        raise RuntimeError("Tamanho das listas diferentes")
    else:
        n = len(x)
        return lambda a: sum([y[i] * calcular_L(i, x)(a) for i in range(n)])

# essa função calcula o polinomio de grau n
def polinimio(n, grau, lista):
    return sum([lista[i]*n**i for i in range(0, grau+1)])


def main():

    # Leitura dos dados de entrada
    GRAU = int(input())
    COEFICIENTES = list(map(int, input().split()))
    COEFICIENTES.reverse() # Invertendo a lista de coeficientes

    # Calculo da sequencia dado o grau e os coeficientes
    SEQUENCIA = [polinimio(i, GRAU, COEFICIENTES) for i in range(1, GRAU + 2)]

    # Criando lista apenas com os indices
    INDICES = [i for i in range(1, GRAU+1)]

    # Declarando lista que ira armazenar a sequencia MOP
    sequencia_MOP = []

    # Calculando a sequencia MOP
    for i in range(1, GRAU+1):
        # Pegando os indices e a sequencia até o indice i
        x = INDICES[:i]
        y = SEQUENCIA[:i]

        # Calculando o MOP e adicionando na lista
        MOP = calcular_PolinomioLagrange(x, y)(i+1)
        sequencia_MOP.append(MOP)

    # Imprimindo a soma da sequencia MOP de 1 até 
    print(sum(sequencia_MOP))

if __name__ == '__main__':
    main()
```

Aqui está uma breve explicação de cada linha do código:

- Linha 1: Define uma função chamada prod que recebe uma lista como entrada e retorna seu produto.

- Linha 5: Define uma função chamada calcular_L que recebe dois inputs i e x. Ele calcula o numerador e denominador do polinômio de Lagrange para cada índice i.

- Linha 14: Define uma função chamada calcular_PolinomioLagrange que recebe dois inputs x e y. Ele verifica se o comprimento de x é igual a y. Em seguida, ele calcula o polinômio de Lagrange para cada índice i em range(n) e retorna a soma de todos os polinômios de Lagrange.

- Linha 23: Define uma função chamada polinimio que recebe três inputs n, grau e lista. Ele calcula o polinômio para cada índice i em range(0, grau+1) usando a fórmula sum([lista[i]*n**i for i in range(0, grau+1)]).

- Linha 31: Define uma função chamada main que lê GRAU e COEFICIENTES da entrada. Ele inverte a lista COEFICIENTES e calcula SEQUENCIA usando a função polinimio para cada índice i em range(1, GRAU + 2). Ele cria a lista INDICES usando range(1, GRAU+1). Em seguida, ele calcula sequencia_MOP usando a função calcular_PolinomioLagrange para cada índice i em range(1, GRAU+1). Finalmente, ele imprime sum(sequencia_MOP).

Você pode assistir uma aula sobre interpolação via forma de lagrange [aqui](https://www.youtube.com/watch?v=Ty_kV-N7qB4)