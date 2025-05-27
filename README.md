# Bio-Mochila - Problema da Mochila com Algoritmos Bio-inspirados

Projeto desenvolvido como parte da disciplina de **Algoritmos Avançados** do curso de Engenharia de Software.  
O objetivo é resolver o Problema da Mochila utilizando **algoritmos genéticos**, além de realizar uma **refatoração completa** com base em boas práticas de engenharia de software (Martin Fowler), testes automatizados e arquitetura modular.

---

## Objetivos

- Refatorar código legado de outra equipe (sem alterar o original)
- Aplicar boas práticas de projeto e refatoração (Fowler)
- Modularizar a arquitetura: GUI, Controller e Lógica
- Adicionar testes automatizados com `pytest`
- Criar documentação técnica detalhada e apresentação
- Modernizar a interface com uma estética inspirada nos anos 80 (GUI Neon)

---

## Estrutura do Projeto

```bash
bio-mochila/
├── algoritmo.py               # Núcleo do algoritmo genético
├── controller.py              # Controlador da lógica
├── gui.py                     # Interface gráfica (versão simples)
├── main.py                    # Ponto de entrada da aplicação
├── test/
│   └── test_mochila_genetico.py  # Testes automatizados com pytest
├── documentation/
│   ├── refatoracao.md         # Documentação da refatoração
│   └── processo.md            # Processo de desenvolvimento
├── original/                  # Cópia do código original da equipe fornecida
│   ├──  LICENSE               # Licensa 
│   ├──  README.MD             # README do projeto antigo
│   ├──  interface_mochila.py  # Interface gráfica antiga (Neon anos 80)
│   ├──  mochila_genetico.py   # Controlador antigo da lógica
│   ├──  requirementas.txt     # Requerimentos do projeto
│   └──  test.md               # Arquivo de teste do projeto antigo
└── README.md                  # Este arquivo
```

---

## Funcionalidades

- Execução do algoritmo genético para resolver o Knapsack Problem
- Interface gráfica com botão para execução e visualização do resultado
- Testes unitários para funções principais do algoritmo
- Modularização clara seguindo padrão MVC
- Documentação completa do processo e da refatoração

---

## Documentação

- [Documentação da Refatoração](documentation/refatoracao.md)
- [Documentação do Processo de Trabalho](documentation/processo.md)
- [Testes Automatizados](test/test_mochila_genetico.py)

---

## Executando o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/bio-mochila.git
   cd bio-mochila
   ```

2. Instale as dependências (recomenda-se um ambiente virtual):
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a interface:
   ```bash
   python main.py
   ```

4. Rode os testes:
   ```bash
   pytest test/
   ```

---

## Tecnologias e Ferramentas

- Python 3.10+
- Tkinter (GUI)
- Pytest (Testes)
- PEP8 + Flake8 (Análise de código)
- Git + GitHub
- ChatGPT (IA Assistente)

---

## Licença

Este projeto está licenciado sob os termos da licença MIT.

---

## Créditos

Projeto desenvolvido por [Seu Nome] como parte da disciplina de Algoritmos Avançados — Engenharia de Software.
