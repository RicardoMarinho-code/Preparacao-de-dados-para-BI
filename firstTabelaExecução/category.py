def getCategory (row):
    """
    Define a categoria com base no valor da coluna "Resultado Lei".

    Mapeia o código numérico para uma string de categoria correspondente.
    Se na coluna tiver algum desses valores abaixo na coluna "Resultado Lei",
    será o seguinte nome

    2           |   Discricionário
    3           |   PAC
    6,7,8,9     |   Emendas
    0           |   Fundo Social

    Args:
        row (pd.Series): Uma linha de um DataFrame do Pandas.
    """
    
    category_map = {
        2: "Discricionário",
        3: "PAC",
        6: "Emendas",
        7: "Emendas",
        8: "Emendas",
        9: "Emendas",
        0: "Fundo Social"
    }
    resultado_lei = row["Resultado Lei"]
    # .get() busca a chave no dicionário. Se não achar, retorna o valor original.
    return category_map.get(resultado_lei, resultado_lei)