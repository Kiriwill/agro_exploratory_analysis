import pandas as pd

# Arquivo original (tabela 1)
pd.read_excel('Historico_2000_2017_revisado_2018.xls')

# Retira comentários e define indices corretos
historic = pd.read_excel('Historico_2000_2017_revisado_2018.xls', header=[1,2], index_col=0, skiprows=range(37,49))

# Retira colunas "unnamed"  
emptyze_collum = {k:'' for k in historic.columns if type(k) == str and 'Unnamed' in k}
historic.rename(emptyze_collum, axis="columns", inplace=True)

# Cria tabelas com dados de estados (imagem 3)
index_estados = [i for i in historic.index if i not in ['NORTE','SUDESTE','SUL','NORDESTE','CENTRO-OESTE', 
                                                        'SEM DEFINIÇÃO', 'Total']]

estados = historic.loc[index_estados,:]
