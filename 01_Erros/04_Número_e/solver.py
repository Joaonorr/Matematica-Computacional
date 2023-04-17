def factorial(n:int):
    if n == 0: 
        return 1 # caso base
    else: 
        return n * factorial(n-1) # caso recursivo

def relativeError(current_approach:float, previous_approach:float):
    return (current_approach - previous_approach) / current_approach # calcula o erro relativo

def epsilon(error:float):
    n = 1
    e_approach = 1/factorial(0) # atual valor de e
    e_previous = 0.0 # valor do e anterior
    while True:
        e_previous = e_approach # atualiza o valor do e anterior
        e_approach += 1/factorial(n) # atualiza o valor de e
        if relativeError(e_approach, e_previous) < error: # verifica se o erro relativo é menor que o erro
            break
        n += 1 # atualiza o valor de n
    return "{:.15}".format(e_approach) # retorna o valor de e com 15 casas decimais

        
def main():
    error = float(input())
    print(epsilon(error))


if __name__ == "__main__":
    main()