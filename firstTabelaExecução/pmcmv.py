def pmcmv (govvernmmentAction):
    """
    Se na coluna tiver algum desses nomes abaixo na coluna "Ação Governo",
    vai ser "sim". Caso contrário, vai ser "não":

    00AF
    00AF
    00CW
    00CW
    00CW
    00CW
    00CX
    00CY
    00CY
    00TI
    00TI
    00TI
    00TI
    00TI

    """
    if govvernmmentAction in ["00AF", "00CW", "00CX", "00CY", "00TI"]:
        return "sim"
    else:
        return "não"