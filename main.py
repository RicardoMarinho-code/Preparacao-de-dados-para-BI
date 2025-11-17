from firstTabelaExecução.nome import takeName
from firstTabelaExecução.category import getCategory
from firstTabelaExecução.position import getDate
from firstTabelaExecução.pmcmv import getPmcmv
from firstTabelaExecução.topay import getTopay
import pandas as pd
import os

file_name = "000000 - Folha com resultado primário 03 11 2025.xlsx"

script_dir = os.path.dirname(os.path.abspath(__file__))

full_file_path = os.path.join(script_dir, file_name)

document = pd.read_excel(full_file_path, header=10)
document = document.fillna(0)

try:


    document = takeName(document)
    document = getTopay(document)

    document['PMCMV'] = document.apply(getPmcmv, axis=1)
    document['Categoria'] = document.apply(getCategory, axis=1)


    dataDF1 = getDate(file_name)
    if dataDF1:
        document['Posição'] = dataDF1

    # --- Adicionando múltiplas planilhas ---

    # 1. Crie os outros DataFrames que você deseja adicionar.
    #    Substitua estes exemplos pelos seus dados reais.
    # A segunda planilha conterá a coluna 'Posição' da primeira.
    df2 = pd.DataFrame(document['Posição'])
    document['Categoria'] = document.apply(getCategory, axis=1)


    dados_planilha3 = {'Info': ['X', 'Y', 'Z'], 'Valores': [100, 200, 300]}
    df3 = pd.DataFrame(dados_planilha3)

    # 2. Use o ExcelWriter para salvar cada DataFrame em uma aba.
    with pd.ExcelWriter("arquivo_modificado.xlsx", engine='xlsxwriter') as writer:
        document.to_excel(writer, sheet_name='Resultado Primário', index=False)
        df2.to_excel(writer, sheet_name='Segunda Planilha', index=False)
        df3.to_excel(writer, sheet_name='Terceira Planilha', index=False)
        # Adicione mais chamadas .to_excel() para mais planilhas

    print("Arquivo 'arquivo_modificado.xlsx' com múltiplas planilhas salvo com sucesso.")

except Exception as e:
    print(f'Ocorreu um erro: {e}')
