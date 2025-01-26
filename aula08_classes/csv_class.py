import pandas as pd 

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None 

        def carregar_csv(self):
            self.df = pd.read_csv(self.file_path)

        def filtrar_por_idade(self, idade):
            return self.df[self.df['idade'] == idade]
        

arquivo_csv = 'C:\Users\Noel\Documents\studySpace\bootcamp python\aula08_classes\dananda.csv'
idade = 28

arquivo_Csv = CsvProcessor(arquivo_csv)
arquivo_Csv.carregar_csv()
arquivo_Csv.filtrar_por_idade(28)
