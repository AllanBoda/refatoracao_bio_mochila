from algoritmo import algoritmo_genetico_mochila

class ControllerMochila:
    def executar_algoritmo(self, itens, capacidade):
        resultado = algoritmo_genetico_mochila(
            itens=itens,
            capacidade_mochila=capacidade,
            tamanho_populacao=10,
            numero_geracoes=20,
            taxa_mutacao=0.05,
            tamanho_torneio=3
        )
        melhor_solucao, valor_total, peso_total, _ = resultado

        return {
            "solucao": melhor_solucao,
            "valor": valor_total,
            "peso": peso_total
        }
