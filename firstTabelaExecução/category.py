def category (category):
    """
    Se na coluna tiver algum desses valores abaixo na coluna "Ação Governo",
    será o seguinte nome

    2   |   Discricionário
    3   |   PAC
    6   |   Emendas
    7   |   Emendas
    8   |   Emendas
    9   |   Emendas
    0   |   Fundo Social

    """    
    if category == 2:
        return "Discricionário"
    elif category == 3:
        return "PAC"
    elif category in [6, 7, 8, 9]:
        return "Emendas"
    elif category == 0:
        return "Fundo Social"
    else:
        return category
        
    