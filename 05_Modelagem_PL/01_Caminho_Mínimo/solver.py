from ortools.linear_solver import pywraplp


def encontrar_caminho_minimo(num_vertices, num_arestas, vertice_inicial, vertice_final, arestas):
    solver = pywraplp.Solver.CreateSolver('GLOP')

    x = {}
    for (u, v, w) in arestas:
        x[u, v] = solver.BoolVar('x[{}, {}]'.format(u, v))

    # Adiciona o objetivo
    objetivo = solver.Objective()
    for (u, v, w) in arestas:
        objetivo.SetCoefficient(x[u, v], w)
    objetivo.SetMinimization()

    # Adiciona as restrições
    for u in range(num_vertices):
        soma_saida = solver.Sum(x[u, v] for (i, v, _) in arestas if i == u)
        soma_entrada = solver.Sum(x[i, u] for (i, v, _) in arestas if v == u)
        if u == vertice_inicial:
            solver.Add(soma_saida - soma_entrada == 1)
        elif u == vertice_final:
            solver.Add(soma_saida - soma_entrada == -1)
        else:
            solver.Add(soma_saida - soma_entrada == 0)

    # Resolve o problema
    results = solver.Solve()

    # Retorna os resultados
    if results == pywraplp.Solver.OPTIMAL:
        valor_objetivo = objetivo.Value()
        caminho_minimo = [(u, v, x[u, v].solution_value()) for (u, v, _) in arestas]
        return valor_objetivo, caminho_minimo
    else:
        return None, None


def main():
    num_vertices, num_arestas, vertice_inicial, vertice_final = map(int, input().split())

    arestas = []
    for _ in range(num_arestas):
        vertice_origem, vertice_destino, peso_aresta = map(int, input().split())
        arestas.append((vertice_origem, vertice_destino, peso_aresta))

    valor_objetivo, caminho_minimo = encontrar_caminho_minimo(num_vertices, num_arestas, vertice_inicial, vertice_final, arestas)

    if valor_objetivo is not None and caminho_minimo is not None:
        print('Solução:')
        print('Valor objetivo =', valor_objetivo)
        for (u, v, valor) in caminho_minimo:
            print("x[{}, {}] = {}".format(u, v, valor))
    else:
        print('O problema não possui uma solução ótima.')


if __name__ == '__main__':
    main()
