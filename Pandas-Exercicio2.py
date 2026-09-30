import pandas as pd

dicionario = {"nome": ["Geronimo", "Martha", "patroclo", "tiberius", "janaina", "mercedes"],
              "cargo":["gerente", "gerente", "vendedor", "secretario", "vendedora", "vendedor"],
              "salario":[9600.56, 9600.56, 2600.90, 4500.45,2600.90,2600.90]
}

df = pd.DataFrame(dicionario)

print(df)

salario = df [df["salario"] > 3000]

print(salario)

cargo = df [df["cargo"] == "vendedor"]

print(cargo)


print(df[(df["cargo"] == "vendedor") | (df["cargo"] == "vendedora")])

#exportando o dataframe para um arquivo CSV
df.to_csv("pandas_excel_aula-12.csv", index=False, sep=";") #sep indica que o símbolo ; indica a separação das colunas