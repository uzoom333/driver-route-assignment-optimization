def algoritmo_guloso(custos_df):
    ordenado = custos_df.sort_values(by="custo")
    atribuicoes = []
    usados_m, usados_r = set(), set()
    custo_total = 0

    for _, linha in ordenado.iterrows():
        m, r, c = linha["id_motorista"], linha["id_rota"], linha["custo"]
        if m not in usados_m and r not in usados_r:
            atribuicoes.append((m, r, c))
            usados_m.add(m)
            usados_r.add(r)
            custo_total += c

    return atribuicoes, custo_total
