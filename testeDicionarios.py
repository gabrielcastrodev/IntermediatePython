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

