import pandas as pd
import os 
import glob 

# Função de extract que le e consolida os json
pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

print(df_list)

#pd.read_json(path_or_buf=)

# Uma função que transforma

#load