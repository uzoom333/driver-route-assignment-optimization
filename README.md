# 🚛 Alocação Ótima de Motoristas às Rotas

Projeto Integrador da disciplina de **Projeto e Análise de Algoritmos (PAA)** — Ciência da Computação.

## 📌 Sobre

Este projeto resolve o problema de atribuição 1-para-1 entre motoristas e rotas, buscando minimizar o custo total da operação logística da empresa fictícia **MidWest Logistics S/A**. O custo pode representar tempo, distância, risco ou uma combinação ponderada desses fatores.

O problema é modelado como uma atribuição em **grafo bipartido** e resolvido por dois métodos:

- **Algoritmo Guloso** — abordagem simples e rápida, porém sem garantia de solução ótima
- **Algoritmo Húngaro** — garante a solução ótima com complexidade O(n³)

## 📂 Estrutura

```
├── src/                → Código-fonte
│   ├── main.py         → Ponto de entrada da aplicação
│   ├── dados.py        → Carregamento dos dados CSV
│   ├── guloso.py       → Implementação do algoritmo Guloso
│   ├── hungaro.py      → Implementação do algoritmo Húngaro
│   ├── visual.py       → Geração de gráficos e visualizações
│   ├── saida.py        → Exportação dos resultados (CSV/JSON)
│   └── benchmark.py    → Comparação de desempenho entre algoritmos
│
├── data/               → Dados de entrada
│   ├── motoristas.csv  → Cadastro de motoristas
│   ├── rotas.csv       → Informações das rotas
│   └── custos.csv      → Matriz de custos motorista × rota
│
├── resultados/         → Saída gerada
│   ├── atribuicoes_guloso.csv / .json
│   ├── atribuicoes_hungaro.csv / .json
│   ├── matriz_custos.png
│   └── custos_guloso.png
│
└── docs/               → Relatório técnico e apresentação
```

## ⚙️ Pré-requisitos

- Python 3.9+
- pandas
- numpy
- scipy
- matplotlib

```bash
pip install pandas numpy scipy matplotlib
```

## 🚀 Como executar

```bash
cd src
python main.py
```

Os resultados serão gerados na pasta `resultados/`.

## 🛠️ Tecnologias

- Python
- Pandas / NumPy — manipulação de dados
- SciPy — implementação do algoritmo Húngaro
- Matplotlib — visualização de dados

## 👥 Equipe — Grupo 5

- Renato Morais
- Gabriel Dantas
- Guilherme Aguiar
- Flaelisnanda

---

*Projeto desenvolvido para a disciplina de Projeto e Análise de Algoritmos — Novembro/2025*
