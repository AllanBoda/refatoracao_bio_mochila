# Refatoracao.md - Projeto Bio-Mochila

## Objetivo da Refatoração

Melhorar a estrutura e qualidade do código de um projeto que resolve o Problema da Mochila com algoritmo genético, implementado originalmente por outro grupo. As melhorias seguem boas práticas de design e as técnicas do livro "Refatoração" de Martin Fowler.

---

## Pontos Refatorados

### 1. **Separar responsabilidades (GUI vs Lógica)**

* **Antes**: Tudo em `interface_mochila.py`, inclusive chamadas diretas para a lógica do algoritmo.
* **Depois**: Criado `controller.py` para gerenciar a comunicação entre a interface e o algoritmo.
* **Técnica usada**: *Extract Class*, *Separate UI from Business Logic*.

### 2. **Modularização e Redução de Complexidade**

* Funções muito longas foram divididas em subfunções com nomes descritivos.
* **Exemplo**: a função `executar_algoritmo_genetico()` foi dividida em etapas claras (validação, execução, exibição).
* **Técnica usada**: *Extract Function*.

### 3. **Constantes para evitar mágic numbers**

* **Antes**: Parâmetros como largura do canvas, tempo de animação etc., estavam "soltos".
* **Depois**: Criadas constantes nomeadas no topo do arquivo.
* **Técnica usada**: *Replace Magic Number with Symbolic Constant*.

### 4. **Testabilidade**

* Adicionados testes com `pytest` no diretório `tests/`.
* Testes cobrem: fitness, criação de população, crossover e mutação.
* **Técnica usada**: *Introduce Test*, *Encapsulate Field*.

### 5. **Nomeação descritiva**

* Renomeadas variáveis e funções para nomes mais expressivos.
* **Exemplo**: `btn_executar_ag` → `botao_executar_algoritmo`.
* **Técnica usada**: *Rename Method*, *Rename Variable*.

---

## Técnicas Aplicadas (Fowler)

* Extract Function
* Extract Class
* Rename Method
* Replace Magic Number with Constant
* Separate UI from Business Logic
* Introduce Assertion
* Introduce Explaining Variable
* Remove Dead Code

---

## Ferramentas Utilizadas

* **Lint**: `flake8`, `pylint`
* **Testes**: `pytest`
* **AI Assistente**: ChatGPT (OpenAI)
* **Controle de Versão**: Git + GitHub (repo separado)

---

## Justificativa Geral

A refatoração foi planejada para:

* Tornar o sistema mais legível e reutilizável.
* Separar camadas de interface, lógica e controle.
* Facilitar testes automatizados.
* Eliminar código duplicado e tornar a estrutura mais limpa para futuras manutenções.

---

## Resultados Esperados

* Manutenção e compreensão facilitadas.
* Maior cobertura de testes.
* Interface desacoplada da lógica do problema.
* Código com padrões consistentes e validado por linters.

---

## Referências

* Martin Fowler - *Refatoração: Aperfeiçoando o Design de Códigos Existentes*
* [https://refactoring.guru/refactoring/techniques](https://refactoring.guru/refactoring/techniques)
* [https://refactoring.com/catalog/](https://refactoring.com/catalog/)

---

*Este documento faz parte da entrega do projeto de Refatoração de Algoritmos Bio-inspirados para o curso de Algoritmos Avançados em Engenharia de Software.*
