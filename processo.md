# Refatoração do Projeto Bio-Mochila

## Como organizamos o trabalho de refatoração

Para garantir que o código original não fosse impactado, seguimos um processo estruturado de engenharia de software com controle de versão, ramificação e documentação.

---

## Etapas do Processo

### 1. **Clonagem segura**

* Criamos um **repositório separado** baseado no código original do grupo colega.
* Preservamos os arquivos originais intactos na pasta `/original/`.

### 2. **Criação da branch de trabalho**

* Criamos uma branch `refatoracao` para realizar todas as modificações de forma isolada.
* O Git foi utilizado para rastrear todas as mudanças.

### 3. **Organização em módulos**

* Dividimos os arquivos em `interface`, `controller` e `algoritmo`.
* Adicionamos pasta `tests/` com arquivos de teste.

### 4. **Validação Contínua**

* Rodamos `pytest` a cada alteração.
* Usamos `flake8` e `pylint` para verificar qualidade do código.

### 5. **Documentação e Slides**

* Documentamos o plano (`refatoracao.md`) e este processo (`processo.md`).
* Criamos slides destacando melhorias e antes/depois da refatoração.

---

## Garantias Adotadas

* O código original **não foi sobrescrito** nem alterado.
* Toda lógica foi testada antes e depois da refatoração.
* Os testes garantem que o algoritmo continua funcionando como esperado.
* Logs do Git mostram todas as mudanças feitas por etapa.

---

## Ferramentas Utilizadas

* **Git + GitHub**
* **pytest** para testes
* **flake8** e **pylint** para lint
* **VSCode** como IDE principal
* **ChatGPT** como assistente de refatoração

---

## Fluxo Final do Projeto

```bash
bio-mochila-refatorado/
├── original/                  # Código original intacto
├── refatorado/                # Nova estrutura com melhorias
├── tests/                     # Testes automatizados
├── refatoracao.md            # Plano de refatoração
├── processo.md               # Este documento
└── slides_apresentacao.pdf   # Material de apresentação
```

---

*Este documento foi entregue como parte da atividade de Refatoração do Projeto Bio-Mochila, disciplina de Algoritmos Avançados em Engenharia de Software.*
