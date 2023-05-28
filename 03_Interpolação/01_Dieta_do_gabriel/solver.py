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


def main():
    IDADES = [25, 45, 65] 
    MASSAS = [50, 60, 70, 80]
    CALORIAS = [
        [2500, 2350, 1900],  # 50
        [2850, 2700, 2250],  # 60
        [3200, 3000, 2750],  # 70
        [3550, 3350, 2850]   # 80
    ]

    idade, peso = map(int, input().split())

    if abs(peso - MASSAS[1]) <= abs(peso - MASSAS[2]):
        pesos = MASSAS[:3]
        calorias = CALORIAS[:3]
    else:
        pesos = MASSAS[1:]
        calorias = CALORIAS[1:]

    polinomios_idades = []
    
    for caloria in calorias:
        polinomios_idades.append(calcular_PolinomioLagrange(IDADES, caloria)(idade))

    polinomio_peso = calcular_PolinomioLagrange(pesos, polinomios_idades)(peso)

    print("%.5f" % polinomio_peso)


if __name__ == '__main__':
    main()
