def getTopay (document):
    try:
        document["A Pagar"] = document["DESPESAS EMPENHADAS"] - document["DESPESAS PAGAS"]
        return document
    except KeyError:
        print("Erro: Verifique os nomes das colunas 'DESPESAS EMPENHADAS' e 'DESPESAS PAGAS'.")