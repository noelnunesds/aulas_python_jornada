import pandas as pd 

class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Método extrair_dados deve ser implementado nas classes filhas")

    def executar_etl(self):
        dados_extraidos = self.extrair_dados()

class ETLExcel(ETLProcess):
    def __init__(self, fonte_dados):
        super().__init__(fonte_dados)
    
    def extrair_dados(self):
        print('all')
        return super().extrair_dados()
