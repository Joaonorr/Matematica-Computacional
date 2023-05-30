# Brincadeira do Augusto

- [Problema](#problema)
- [Entrada](#entrada)
- [Saída](#saída)
- [Exemplos](#exemplos)

## Problema

Augusto gosta muito da seguinte brincadeira: 

dada a sequência 1, 2, 3, 4, 5 qual é a próximo número? Às vezes é muito fácil responder, às vezes pode ser bem difícil. Augusto notou que essas perguntas podem ser resolvidas descrevendo a sequência usando polinômios. Por exemplo, a seqüência 1, 2, 3, 4, 5 pode ser facilmente entendida como um polinômio trivial, $P(n)=n$ . O próximo número será 6. Mas sequências ainda mais complexas, como 1, 2, 4, 7, 11, podem ser descritas por um polinômio. Neste caso, o polinômio que descreve esta sequência é $\frac{1}{2}n^{2}-\frac{1}{2}n+1$ . Note que mesmo se os membros da sequência são inteiros, os coeficientes polinomiais podem ser quaisquer números reais.

Um polinômio é uma expressão da seguinte forma:

$$P(n)=a_{k}n^{k}+a_{k-1}n^{k-1}+...+a_{1}n+a_{0}$$

- Se $a_{k}≠0$ , o número $D$ é chamado de grau do polinômio. Note que a função constante $P(n)=C$ pode ser considerado como polinômio de grau 0.

Sua tarefa é dada uma sequência com comprimento $N$ encontre o menor grau de um polinômio que pode ser usado para descrever uma sequência.

## Entrada

A entrada do problema é composta por duas linhas. A primeira linha possui um inteiro $N$ representando o comprimento da sequência dada.

A segunda linha contém N números inteiros $x_0,x_1,..,x_{n−1}$ separados por um espaço. Esses números forma a sequência dada.

## Saída

Imprima um inteiro D representando o menor grau possível de um polinômio $P(n)$ tal que $P(i)=x_{i}$, para todo $i=0,..,n−1$.

## Exemplos

Entrada

    5
    1 2 3 4 5

Saída

    1

---

Entrada

    5
    1 2 4 7 11

Saída

    2

---

## Resolução

```python
def polinomio(SEQUENCIA: list, TAMANHO: int, grau:int) -> int:
    # Enquanto a soma da sequência for diferente de 0
    while sum(SEQUENCIA) != 0:
        # Atualiza a sequência
        SEQUENCIA = [(SEQUENCIA[i+1] - SEQUENCIA[i])/(grau+1) for i in range(TAMANHO - 1)]
        # Atualiza o tamanho
        TAMANHO -= 1
        # Atualiza o grau
        grau += 1
    # Retorna o grau
    return grau - 1

def main():
    # Entrada
    TAMANHO = int(input())
    SEQUENCIA = list(map(int, input().split()))

    # Chama a função polinomio
    x = polinomio(SEQUENCIA, TAMANHO, 0)

    # Imprime o resultado
    print(x)

if __name__ == '__main__':
    main()
```

Esse código define uma função chamada polinomio que calcula o grau de um polinômio a partir de uma sequência de números. Em seguida, a função main é definida para obter a entrada do usuário e chamar a função polinomio. Aqui está uma explicação passo a passo do que o código faz:

1. A função polinomio recebe três argumentos: SEQUENCIA (uma lista de números), TAMANHO (o tamanho da sequência) e grau (o grau inicial do polinômio).
2.  O código entra em um loop while que continua até que a soma de todos os elementos da sequência seja igual a zero.
3. Dentro do loop, a sequência atual é impressa usando print(SEQUENCIA).
4. A sequência é então atualizada usando uma list comprehension. Cada elemento da nova sequência é calculado subtraindo o elemento seguinte pelo elemento atual e dividindo o resultado por grau + 1. Isso é feito usando a expressão (SEQUENCIA[i+1] - SEQUENCIA[i])/(grau+1) em um loop que percorre todos os elementos da sequência, exceto o último.
5. O tamanho da sequência é diminuído em 1 (TAMANHO -= 1), pois agora a nova sequência tem um elemento a menos.
6. O grau é incrementado em 1 (grau += 1), pois o cálculo do novo elemento do polinômio aumenta o grau em 1.
7. O loop continua até que a soma de todos os elementos da sequência seja zero.
8. Quando o loop termina, a função retorna grau - 1, que é o grau final do polinômio calculado.
9. A função main é definida para lidar com a entrada do usuário e chamar a função polinomio.
10. A entrada do tamanho (TAMANHO) é obtida do usuário usando input() e convertida para um número inteiro usando int().
11. A sequência (SEQUENCIA) é obtida do usuário usando input() e é convertida em uma lista de inteiros usando list(map(int, input().split())).
12. A função polinomio é chamada com os argumentos SEQUENCIA, TAMANHO e 0 para calcular o grau do polinômio.
13. O resultado é armazenado na variável x.
14. O valor de x é impresso usando print(x).

Em resumo, o código calcula o grau de um polinômio a partir de uma sequência de números fornecida pelo usuário.
