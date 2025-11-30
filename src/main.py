import os
from dados import carregar_dados
from guloso import algoritmo_guloso
from hungaro import algoritmo_hungaro
from saida import exibir_atribuicoes, salvar_csv, salvar_json
from visual import heatmap_matriz, barras_custos

def main():
    # Carregar dados
    motoristas, rotas, custos, matriz_df, matriz_np = carregar_dados(
        "../data/motoristas.csv", "../data/rotas.csv", "../data/custos.csv"
    )

    # Criar pasta de resultados se não existir
    os.makedirs("../resultados", exist_ok=True)

    # Visualização da matriz
    heatmap_matriz(matriz_df, "../resultados/matriz_custos.png")

    # Algoritmo guloso
    atrib_g, custo_g = algoritmo_guloso(custos)
    exibir_atribuicoes("Algoritmo Guloso", atrib_g, custo_g)
    salvar_csv("../resultados/atribuicoes_guloso.csv", atrib_g)
    salvar_json("../resultados/atribuicoes_guloso.json", atrib_g, custo_g)
    barras_custos(atrib_g, "../resultados/custos_guloso.png", "Custos - Guloso")

    # Algoritmo Húngaro
    atrib_h, custo_h = algoritmo_hungaro(matriz_np, motoristas, rotas)
    exibir_atribuicoes("Algoritmo Húngaro", atrib_h, custo_h)
    salvar_csv("../resultados/atribuicoes_hungaro.csv", atrib_h)
    salvar_json("../resultados/atribuicoes_hungaro.json", atrib_h, custo_h)
    barras_custos(atrib_h, "../resultados/custos_hungaro.png", "Custos - Húngaro")

if __name__ == "__main__":
    main()

