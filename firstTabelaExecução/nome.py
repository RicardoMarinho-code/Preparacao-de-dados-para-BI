def takeName (document):
    document[["Ação Governo"]]

    """
    Adiciona o mesmo nome da coluna "Nome", após o código (nome em Ação governo)
    com o seguinte padrão abaixo:

    Ação Governo	|   Nome
    00AF            |   FAR 00AF
    00CW            |   Cidades 00CW
    00CX            |   Rural 00CX
    00CY            |   FDS 00CY
    00TI            |   FNHIS Sub-50 00TI
    0648            |   FNHIS Legado 0648
    0E64            |   Oferta Pública 0E64
    10SJ            |   FNHIS Antigo 10SJ
    20Z9            |   PBQP-H 20Z9
    8873            |   FNHIS Est/Proj 8873
    00XF            |   Fundo Social 00XF

    """

    document["Nome"] = document["Ação Governo"].apply(lambda x: f"FAR {x}" if x == "00AF" else
                                                            f"Cidades {x}" if x == "00CW" else
                                                            f"Rural {x}" if x == "00CX" else
                                                            f"FDS {x}" if x == "00CY" else
                                                            f"FNHIS Sub-50 {x}" if x == "00TI" else
                                                            f"FNHIS Legado {x}" if x == "0648" else
                                                            f"Oferta Pública {x}" if x == "0E64" else
                                                            f"FNHIS Antigo {x}" if x == "10SJ" else
                                                            f"PBQP-H {x}" if x == "20Z9" else
                                                            f"FNHIS Est/Proj {x}" if x == "8873" else
                                                            f"Fundo Social {x}" if x == "00XF" else x)
                                                            
    return document