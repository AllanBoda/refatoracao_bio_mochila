from mochila_genetico import calcular_peso_e_valor, funcao_fitness, crossover_um_ponto, mutacao_bit_flip

def test_calcular_peso_e_valor():
    itens = [{"peso": 2, "valor": 30}, {"peso": 3, "valor": 40}]
    solucao = [1, 1]
    peso, valor = calcular_peso_e_valor(solucao, itens)
    assert peso == 5
    assert valor == 70

def test_crossover():
    pai1 = [1, 0, 1]
    pai2 = [0, 1, 0]
    filho1, filho2 = crossover_um_ponto(pai1, pai2)
    assert len(filho1) == len(pai1)
    assert len(filho2) == len(pai2)

def test_mutacao():
    individuo = [1, 1, 0]
    mutado = mutacao_bit_flip(individuo, taxa_de_mutacao=1.0)
    assert mutado != individuo
