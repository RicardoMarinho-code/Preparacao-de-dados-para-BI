def getPmcmv (row):
    """
    Verifica se a ação do governo na linha pertence ao PMCMV.
    Se o valor na coluna "Ação Governo" for um dos códigos específicos,
    vai ser "sim". Caso contrário, vai ser "não":

    00AF, 00CW, 00CX, 00CY, 00TI

    Args:
        row (pd.Series): Uma linha de um DataFrame do Pandas.
    """

    pmcmv_codes = {"00AF", "00CW", "00CX", "00CY", "00TI"}

    if row["Ação Governo"] in pmcmv_codes:
        return "sim"
    else:
        return "não"