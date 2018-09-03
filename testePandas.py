# Módulo 02
# Pandas dataFrames
import pandas as pd

# Cria os vetores para serem criados os dicionários
names = [ 'Brasil', 'Jamaica', 'Holanda', 'Alemanha' ]
renda_per = [ '857', '632', '218', '985' ]
lado_volante = [ True, True, False, False ]

# Criação do dicionário
dicionario = {
        
        'pais': names,
        'renda' : renda_per, 
        'lado' : lado_volante 
 }

print(dicionario)

# criação do DataFrame com pandas
data_frame_carros = pd.DataFrame(dicionario)
print()

print("Normal")
print(data_frame_carros)
print()

# Alterando a primeira coluna com o count
primeiras_linhas = ['BRA','JAM', 'HOL', 'ALE']
data_frame_carros.index = primeiras_linhas
print("Index Alterado")
print(data_frame_carros)
print()

data_frame_carros.columns = ['Pais', 'Renda_Pais', 'Lado_volante']
print(data_frame_carros)
print()

# Selecionando elementos em um df com loc e iLoc
print(data_frame_carros.loc[['BRA'], ['Renda_Pais', 'Lado_volante']])
print()
print(data_frame_carros.iloc[[0]])
