def polinomio(n, grau, coeficientes) -> float:
    """
    Retorna o valor do polinômio no ponto n.

    Args:
        n (float): Valor de entrada.
        grau (int): Grau do polinômio.
        coeficientes (list): Lista de coeficientes do polinômio.

    Returns:
        float: Valor do polinômio no ponto n.
    """
    return sum(coeficientes[i] * (grau - i) * (n ** (grau - i - 1)) for i in range(grau + 1))

def comprimento_curva(grau, coeficientes, a, b) -> float:
    """
    Calcula o comprimento de uma curva definida por um polinômio.

    Args:
        grau (int): Grau do polinômio.
        coeficientes (list): Lista de coeficientes do polinômio.
        a (float): Limite inferior de integração.
        b (float): Limite superior de integração.

    Returns:
        float: Comprimento da curva.
    """
    def integrando(x) -> float:
        return (1 + polinomio(x, grau, coeficientes) ** 2) ** 0.5

    def trapezoidal(g, a, b) -> float:
        h = b - a
        return ((g(a) + g(b)) * h) / 2.0

    def trapezoidal_quad(g, a, b, eps) -> float:
        mid = (a + b) / 2.0
        tot = trapezoidal(g, a, b)

        if abs(trapezoidal(g, a, mid) + trapezoidal(g, mid, b) - tot) > eps:
            return trapezoidal_quad(g, a, mid, eps / 2.0) + trapezoidal_quad(g, mid, b, eps / 2.0)
        else:
            return tot

    return trapezoidal_quad(integrando, a, b, 1e-7)

def main():
    GRAU = int(input())

    COEFICIENTES = list(map(int, input().split()))

    PONTOS = list(map(int, input().split()))

    VALUE = comprimento_curva(GRAU, COEFICIENTES, PONTOS[0], PONTOS[1])

    print('{:.5f}'.format(VALUE))

if __name__ == '__main__':
    main()
