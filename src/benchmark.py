import numpy as np
import pandas as pd
from time import perf_counter
from guloso import algoritmo_guloso
from hungaro import algoritmo_hungaro

def gerar_instancia(n=8, seed=42):
    rng = np.random.default_rng(seed)
    motoristas = pd.DataFrame({
        "id_motorista": [f"M{i+1}" for i in range(n)],
        "nome": [f"M{i+1}" for i in range(n)],
        "experiencia_anos": rng.integers(1, 10, size=n)
    })
    rotas = pd.DataFrame({
        "id_rota": [f"R{i+1}" for i in range(n)],
        "descricao": [f"Rota {i+1}" for i in range(n)],
        "origem": ["Anápolis"]*n,
        "destino": [f"Destino {i+1}"]*n
    })
    custos = []
    base = rng.integers(5, 25, size=(n, n))
    for i in range(n):
        for j in range(n):
            custos.append({"id_motorista": motoristas.iloc[i]["id_motorista"],
                           "id_rota": rotas.iloc[j]["id_rota"],
                           "custo": int(base[i, j])})
    custos_df = pd.DataFrame(custos)
    matriz_df = custos_df.pivot(index="id_motorista", columns="id_rota", values="custo").sort_index().sort_index(axis=1)
    matriz_np = matriz_df.to_numpy()
    return motoristas, rotas, custos_df, matriz_df, matriz_np

def rodar_benchmark(n=8):
    motoristas, rotas, custos_df, matriz_df, matriz_np = gerar_instancia(n=n)
    t0 = perf_counter()
    atrib_g, custo_g = algoritmo_guloso(custos_df)
    t1 = perf_counter()
    atrib_h, custo_h = algoritmo_hungaro(matriz_np, motoristas, rotas)
    t2 = perf_counter()
    return {
        "n": n,
        "custo_guloso": custo_g,
        "tempo_guloso_ms": (t1 - t0) * 1000,
        "custo_hungaro": custo_h,
        "tempo_hungaro_ms": (t2 - t1) * 1000
    }

if __name__ == "__main__":
    for n in (8, 10):
        res = rodar_benchmark(n)
        print(res)
