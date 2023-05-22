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

    print(MASSA_MINIMA)

if __name__ == '__main__':
    main()