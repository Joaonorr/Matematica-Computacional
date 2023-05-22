import math

def truncar_numero_decimal(numero, casas_decimais):

    string_formatada = '%.12f' % numero

    parte_inteira, separador, parte_decimal = string_formatada.partition('.')
    
    parte_decimal_truncada = (parte_decimal + '0' * casas_decimais)[:casas_decimais]

    numero_truncado = '.'.join([parte_inteira, parte_decimal_truncada])
    
    return numero_truncado


def bissecao(CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, mols_inicial, mols_final, ERRO_ACEITO):
    
    def concentracao(mols):
        return (CONC_C_0 + mols) / (((CONC_A_0 - 2*mols)**2) * (CONC_B_0 - mols))

    while math.fabs(mols_final - mols_inicial)/2 >= 1*10**(-ERRO_ACEITO-1):

        mols_intermediario = (mols_inicial + mols_final)/2

        if concentracao(mols_intermediario) < CONCENTRACAO:

            mols_inicial = mols_intermediario

        else:

            mols_final = mols_intermediario

    return mols_intermediario


def main():
    CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, MOLS_INICIAL, MOLS_FINAL, ERRO_ACEITO = map(float, input().split())
    
    x = bissecao(CONCENTRACAO, CONC_A_0, CONC_B_0, CONC_C_0, MOLS_INICIAL, MOLS_FINAL, ERRO_ACEITO)

    print(truncar_numero_decimal(x, int(ERRO_ACEITO)))


if __name__ == '__main__':
    main()