import json
import csv

def exibir_atribuicoes(titulo, atribuicoes, custo_total):
    print(f"=== {titulo} ===")
    for m, r, c in atribuicoes:
        print(f"{m} -> {r} (custo {c})")
    print(f"Custo total: {custo_total}\n")

def salvar_csv(caminho, atribuicoes):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["motorista", "rota", "custo"])
        for m, r, c in atribuicoes:
            w.writerow([m, r, c])

def salvar_json(caminho, atribuicoes, custo_total):
    dados = {
        "atribuições": [{"motorista": m, "rota": r, "custo": c} for m, r, c in atribuicoes],
        "custo_total": custo_total
    }
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
