import pandas as pd

#criar um dicionario (dados) para um Dataframe
dicionario={"nome": ["João","Maria", "Pedro"], "idade": [12,10,11], "nota":[7.0, 5.6, 9.0]}

#importar o dicionario (dados) para um Dataframe
df= pd.DataFrame(dicionario)

print(df)
