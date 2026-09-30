import pandas as pd

df = pd.read_csv(r"C:\Users\alejandro.nascimento\Downloads\funcionarios.csv")

print(df)

df_funcinarios_ativos_vendas = df [(df["departamento"] == "Vendas") & (df["ativo"] == True)]
print(df_funcinarios_ativos_vendas)

df_funcinarios_ativos_com_lucros =  df [(df["lucro"] > 5000) & (df["ativo"] == True)]
print(df_funcinarios_ativos_com_lucros)

df_funcinarios_inativos = df [(df["ativo"] == False)]
print(df_funcinarios_inativos)


