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