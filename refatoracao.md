# Refatoração - Projeto Bio-Mochila

## Pontos Refatorados

- **Separação de responsabilidades**: Divisão da lógica do algoritmo genético em um módulo separado.
- **Melhoria na coesão**: Extração de funções e modularização da GUI.
- **Criação de testes**: Implementação de testes para `calcular_peso_e_valor`, `funcao_fitness`, `crossover_um_ponto`, etc.
- **Nomenclatura**: Melhoria na clareza dos nomes de variáveis e funções.
- **Código duplicado**: Redução de duplicação com funções auxiliares reutilizáveis.

## Técnicas Utilizadas

Baseadas no livro *Refatoração* de Martin Fowler e nos sites:
- [refactoring.com](https://refactoring.com/catalog/)
- [refactoring.guru](https://refactoring.guru/refactoring/techniques)

### Técnicas específicas:
- **Extract Function**
- **Extract Class**
- **Replace Magic Number with Symbolic Constant**
- **Separate UI from Business Logic**
- **Encapsulate Field**

## Justificativa

Essas alterações visam:
- Melhor legibilidade e manutenção.
- Capacidade de testar e validar a lógica fora da GUI.
- Redução de erros em mudanças futuras.
