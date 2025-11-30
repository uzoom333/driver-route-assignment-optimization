import numpy as np
from scipy.optimize import linear_sum_assignment

def algoritmo_hungaro(matriz_np, motoristas_df, rotas_df):
    rows, cols = linear_sum_assignment(matriz_np)
    atribuicoes, custo_total = [], 0
    for i, j in zip(rows, cols):
        m = motoristas_df.iloc[i]["id_motorista"]
        r = rotas_df.iloc[j]["id_rota"]
        c = matriz_np[i][j]
        atribuicoes.append((m, r, c))
        custo_total += c
    return atribuicoes, custo_total
