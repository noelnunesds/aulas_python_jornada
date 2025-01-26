import pandas as pd 

df = pd.read_csv('aula08_classes\dananda.csv')

df_filtrado = df[df['idade'] == 28]

print(df_filtrado)