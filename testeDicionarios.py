# Módulo 02
# Testes com dicionários

paises = ['brasil', 'frança', 'alemanha']
capitais = ['brasilia', 'paris', 'berlim']

meu_dicionario = {
        'brasil':'brasilia', 'frança':'paris', 'alemanha':'berlim'
 }

print(meu_dicionario)
print(meu_dicionario['brasil'])

meu_dicionario['brasil'] = 'rio de janeiro' # alterar os dados da chave 'Brasil'
print(meu_dicionario['brasil'])

meu_dicionario['italia'] = 'rome' # Adicionando um novo valor ao dicionário
print(meu_dicionario)
print()

dicionario2 = { # dicionario com várias listas e categorias
    'brasil' : {'capital' : 'brasilia', 'populacao' : 89.13 },
    'alemanha' : { 'capital' : 'berlim', 'populacao' : 45.13 },
    'italia' : { 'capital' : 'rome', 'populacao' : 12.12 }
 }

print(dicionario2)
print()
print(dicionario2['brasil']) # imprimindo apenas os valores da lista 'brasil' dentro do dicionário
print(dicionario2['alemanha']) # imprimindo apenas alemanha

lista_add = { 'capital': 'warsaw', 'populacao' : 5.75 } # adicionando uma nova categoria e subcategoria
dicionario2['polonia'] = lista_add # adicionando as subcategorias e criando a categoria que vai receber os valores


print(dicionario2['polonia'])
print()

