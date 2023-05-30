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
