import matplotlib.pyplot as plt

def heatmap_matriz(matriz_df, caminho_png):
    plt.figure(figsize=(6,4))
    plt.imshow(matriz_df.values, cmap="Blues")
    plt.colorbar(label="Custo")
    plt.xticks(ticks=range(matriz_df.shape[1]), labels=matriz_df.columns)
    plt.yticks(ticks=range(matriz_df.shape[0]), labels=matriz_df.index)
    plt.title("Matriz de Custos (Motoristas x Rotas)")
    plt.tight_layout()
    plt.savefig(caminho_png, dpi=150)
    plt.close()

def barras_custos(atribuicoes, caminho_png, titulo):
    motoristas = [m for m, _, _ in atribuicoes]
    custos = [c for _, _, c in atribuicoes]
    plt.figure(figsize=(6,4))
    plt.bar(motoristas, custos, color="#4e79a7")
    plt.ylabel("Custo individual")
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(caminho_png, dpi=150)
    plt.close()
