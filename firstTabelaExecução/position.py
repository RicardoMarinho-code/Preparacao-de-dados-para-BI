import re

def getDate(filename: str):
    
    """
    Extrai a data do nome de um arquivo.

    A função busca por um padrão de data no formato 'DD MM AAAA' no nome do arquivo fornecido.

    Args:
        filename (str): O nome do arquivo, por exemplo:
                        "000000 - Folha com resultado primário 03 11 2025.xlsx"

    Returns:
        str: A data encontrada no formato 'DD/MM/AAAA' ou None se nenhuma data for encontrada.
    """

    match = re.search(r'(\d{2})\s(\d{2})\s(\d{4})', filename)
    if match:
        return f"{match.group(1)}/{match.group(2)}/{match.group(3)}"
    return None