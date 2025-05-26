import random

def calcular_peso_e_valor(solucao, itens):
    peso_total, valor_total = 0, 0
    for i, incluído in enumerate(solucao):
        if incluído:
            peso_total += itens[i]["peso"]
            valor_total += itens[i]["valor"]
    return peso_total, valor_total

def funcao_fitness(solucao, itens, capacidade):
    peso, valor = calcular_peso_e_valor(solucao, itens)
    return valor if peso <= capacidade else 0

def criar_individuo(n):
    return [random.randint(0, 1) for _ in range(n)]

def criar_populacao_inicial(tam_pop, n_itens):
    return [criar_individuo(n_itens) for _ in range(tam_pop)]

def selecao_torneio(populacao, itens, capacidade, k=3):
    competidores = random.sample(populacao, k)
    return max(competidores, key=lambda ind: funcao_fitness(ind, itens, capacidade))

def crossover(pai1, pai2):
    corte = random.randint(1, len(pai1) - 1)
    return pai1[:corte] + pai2[corte:], pai2[:corte] + pai1[corte:]

def mutacao(individuo, taxa):
    return [1 - g if random.random() < taxa else g for g in individuo]

def algoritmo_genetico_mochila(itens, capacidade_mochila, tamanho_populacao, numero_geracoes, taxa_mutacao, tamanho_torneio=3, callback_geracao=None):
    n = len(itens)
    populacao = criar_populacao_inicial(tamanho_populacao, n)
    melhor = None
    melhor_fitness = -1

    for geracao in range(numero_geracoes):
        nova_pop = []
        avaliacoes = [(ind, funcao_fitness(ind, itens, capacidade_mochila)) for ind in populacao]
        elite = max(avaliacoes, key=lambda x: x[1])[0]
        nova_pop.append(elite)

        while len(nova_pop) < tamanho_populacao:
            p1 = selecao_torneio(populacao, itens, capacidade_mochila, tamanho_torneio)
            p2 = selecao_torneio(populacao, itens, capacidade_mochila, tamanho_torneio)
            f1, f2 = crossover(p1, p2)
            nova_pop.extend([mutacao(f1, taxa_mutacao), mutacao(f2, taxa_mutacao)])

        populacao = nova_pop[:tamanho_populacao]
        melhor_atual = max(populacao, key=lambda ind: funcao_fitness(ind, itens, capacidade_mochila))
        fitness_atual = funcao_fitness(melhor_atual, itens, capacidade_mochila)

        if fitness_atual > melhor_fitness:
            melhor = melhor_atual
            melhor_fitness = fitness_atual

        if callback_geracao:
            callback_geracao(geracao + 1, melhor_fitness)

    peso, valor = calcular_peso_e_valor(melhor, itens)
    return melhor, valor, peso, []
