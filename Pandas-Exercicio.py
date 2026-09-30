import pandas as pd

dicionario = {
    "nome": ["Joaquim", "Pedro", "Thiago"], 
    "Cargo":["Analista", "Assistente", "Estagiário"], 
    "Salário": [5.500, 3.000,1.200]
              }

df = pd.DataFrame (dicionario)

print(df)

#exportando o dataframe para um arquivo CSV
df.to_csv("pandas_excel_exercicio-1.csv", index=False, sep=";") #sep indica que o símbolo ; indica a separação das colunas