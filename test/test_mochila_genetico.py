import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from original.mochila_genetico import (
    calcular_peso_e_valor,
    funcao_fitness,
    criar_individuo,
    criar_populacao_inicial,
    crossover_um_ponto,
    mutacao_bit_flip,
    algoritmo_genetico_mochila
)

def test_calcular_peso_e_valor():
    itens = [
        {"peso": 2, "valor": 30},
        {"peso": 3, "valor": 40},
        {"peso": 5, "valor": 60}
    ]
    solucao = [1, 0, 1]
    peso, valor = calcular_peso_e_valor(solucao, itens)
    assert peso == 7
    assert valor == 90

def test_funcao_fitness_valida():
    itens = [
        {"peso": 2, "valor": 30},
        {"peso": 3, "valor": 40}
    ]
    solucao = [1, 1]
    fitness = funcao_fitness(solucao, itens, capacidade_mochila=6)
    assert fitness == 70

def test_funcao_fitness_invalida():
    itens = [
        {"peso": 4, "valor": 50},
        {"peso": 5, "valor": 60}
    ]
    solucao = [1, 1]
    fitness = funcao_fitness(solucao, itens, capacidade_mochila=5)
    assert fitness == 0

def test_criar_individuo():
    individuo = criar_individuo(5)
    assert len(individuo) == 5
    assert all(gene in [0, 1] for gene in individuo)

def test_criar_populacao_inicial():
    populacao = criar_populacao_inicial(10, 4)
    assert len(populacao) == 10
    for individuo in populacao:
        assert len(individuo) == 4

def test_crossover_um_ponto():
    pai1 = [1, 1, 1, 1]
    pai2 = [0, 0, 0, 0]
    filho1, filho2 = crossover_um_ponto(pai1, pai2)
    assert len(filho1) == 4
    assert len(filho2) == 4
    assert filho1 != pai1 or filho2 != pai2  # Mudança esperada

def test_mutacao_bit_flip():
    individuo = [1, 1, 1, 1]
    mutado = mutacao_bit_flip(individuo, taxa_de_mutacao=1.0)
    assert mutado == [0, 0, 0, 0]

def test_algoritmo_genetico_mochila_execucao():
    itens = [
        {"nome": "A", "peso": 1, "valor": 10},
        {"nome": "B", "peso": 2, "valor": 20},
        {"nome": "C", "peso": 3, "valor": 30}
    ]
    melhor_solucao, valor_final, peso_final, historico = algoritmo_genetico_mochila(
        itens, capacidade_mochila=4, tamanho_populacao=10,
        numero_geracoes=5, taxa_mutacao=0.1, tamanho_torneio=2
    )
    assert isinstance(melhor_solucao, list)
    assert isinstance(valor_final, int)
    assert isinstance(peso_final, int)
    assert isinstance(historico, list)
    assert len(historico) == 5
