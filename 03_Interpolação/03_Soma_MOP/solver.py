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

    