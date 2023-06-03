
def polinimio(n, grau, COEFICIENTES):
    return sum([COEFICIENTES[i]*n**i for i in range(0, grau+1)])

def simpson(INTERVALO_INICIAL, INTERVALO_FINAL, GRAU, COEFICIENTES):

    TAMANHO_DO_INTERVALO = (INTERVALO_FINAL - INTERVALO_INICIAL)/2

    f0 = polinimio(INTERVALO_INICIAL, GRAU, COEFICIENTES)

    f1 = polinimio(INTERVALO_INICIAL + TAMANHO_DO_INTERVALO, GRAU, COEFICIENTES)

    f2 = polinimio(INTERVALO_FINAL, GRAU, COEFICIENTES)

    return (TAMANHO_DO_INTERVALO / 3) * (f0 + 4 * f1 + f2)

def simpson_composto(INTERVALO_INICIAL, INTERVALO_FINAL, DISCRETIZACAO, GRAU, COEFICIENTES):
    
    soma = 0

    TAMANHO_DO_INTERVALO = (INTERVALO_FINAL - INTERVALO_INICIAL)/DISCRETIZACAO

    for i in range(DISCRETIZACAO):
        soma += simpson(INTERVALO_INICIAL + (i * TAMANHO_DO_INTERVALO), INTERVALO_INICIAL + (i + 1) * TAMANHO_DO_INTERVALO, GRAU, COEFICIENTES)

    return soma

def main():

    GRAU = int(input())

    COEFICIENTES = list(map(float, input().split()))
    COEFICIENTES.reverse()

    INTER_DE_INTEGRACAO_E_DISCRET = list(map(int, input().split()))

    VALUE = simpson_composto(INTER_DE_INTEGRACAO_E_DISCRET[0], INTER_DE_INTEGRACAO_E_DISCRET[1], INTER_DE_INTEGRACAO_E_DISCRET[2], GRAU, COEFICIENTES)

    print("%.5f" % VALUE)

if __name__ == '__main__':
    main()