import pandas as pd

def carregar_dados(motoristas_csv, rotas_csv, custos_csv):
    motoristas = pd.read_csv(motoristas_csv)
    rotas = pd.read_csv(rotas_csv)
    custos = pd.read_csv(custos_csv)

    matriz_df = custos.pivot(index="id_motorista",
                             columns="id_rota",
                             values="custo").sort_index().sort_index(axis=1)

    matriz_np = matriz_df.to_numpy()
    return motoristas, rotas, custos, matriz_df, matriz_np
