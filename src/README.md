Projeto Integrador — Alocação Ótima de Motoristas às Rotas  
Grupo 5 — Projeto e Análise de Algoritmos  
MidWest Logistics S/A  
Data: 30 de novembro de 2025

Integrantes do grupo:
- Renato Morais
- Gabriel Dantas
- Guilherme Aguiar
- Flaelisnanda

===========================================
📌 Descrição do Projeto
===========================================

Este projeto resolve o problema de atribuição 1-para-1 entre motoristas e rotas, buscando minimizar o custo total da operação logística. O custo pode representar tempo, distância, risco ou uma combinação ponderada desses fatores.

O problema é modelado como uma atribuição em grafo bipartido e resolvido por dois métodos:
- Algoritmo Guloso (simples e rápido, mas não ótimo)
- Algoritmo Húngaro (garante solução ótima)

===========================================
📁 Estrutura do Repositório
===========================================

- src/ → Código-fonte (carregamento, algoritmos, main)
- data/ → Arquivos CSV com motoristas, rotas e custos
- resultados/ → Arquivos gerados (atribuições, gráficos, JSON)
- docs/ → Relatório técnico e slides de apresentação
- README.txt → Este arquivo de descrição

===========================================
⚙️ Pré-requisitos
===========================================

- Python 3.9 ou superior
- Bibliotecas:
  - pandas
  - numpy
  - scipy
  - matplotlib

Instalação dos pacotes:
