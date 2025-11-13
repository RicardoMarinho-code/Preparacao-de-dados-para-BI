from firstTabelaExecução.takeTwoDigits import takeFirstTwoDigits
from firstTabelaExecução.topay import topay
import pandas as pd



# header mostra quais linhas planilha começa
# A contagem começa em 0. Se o cabeçalho está na linha 4 do Excel, use header=3.
primaryKey = pd.read_excel("000000 - Folha com resultado primário 28 10 2025.xlsx", header=10)
primaryKey = primaryKey.fillna(0)

#Para lista, colchete duplo
#baseSecundaria = primaryKey[["PROJETO INICIAL DA LOA - FIXACAO DESPESA", "CREDITO DISPONIVEL"]]

#".astype(int)." transforma em inteiro
#.fillna(0) transforma valores em branco em "0", para evitar erros
#baseSecundaria = baseSecundaria.fillna(0)

try:
    # .map(). verifica se o valor é numérico (int ou float) antes de formatar.
    # Se não for numérico, o valor original é retornado.
    # 1. Formata o número para string com 2 casas decimais e separador de milhar.
    # 2. Usa .translate() para trocar os separadores para o padrão brasileiro.
    print(primaryKey.map(lambda x: f'{x:,.2f}'.translate(str.maketrans(',.', '.,')) if isinstance(x, (int, float)) else x))

    primaryKey.to_excel("base_primaria_tratada.xlsx", index=False)
    print("Dados salvos")

#"Exception as e" transforma a exceção em "e"
except Exception as e:
    print(f'Ocorreu um erro: {e}')

