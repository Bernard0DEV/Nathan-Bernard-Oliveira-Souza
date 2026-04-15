# string = texto
# int = numeros inteiros (1,2,3,4)
# float = numeros de ponto flutuante
# list = lista
# dict = tipo de dicionário
# tupla
# sets = conjuntos
# datetime = data e hora
# bool = verdadeiro ou falso (bolean)
"""
type() - serve para validar tipos, assim verificando se o tipo corresponde ao pedido do codigo
"""

# texto = 'programacao'
# numero = "1"
# print("essa e a variavel texto: ", texto)
# print("essa variavel e do tipo: ", type(texto))

# print(type(type(texto) == type(numero)))

ponto_flutuante = 1.4
inteiro = 7
complexo = 15 + 16j 
# f-string e um texto que recebe variaveis em chaves
# print(f"a soma de {inteiro} mais {ponto_flutuante} É: {inteiro + ponto_flutuante}")
# while True:
#     recebido = input("digite um numero: ")
#     try:
#         recebido = int(recebido)
#     except ValueError:
#         try:
#             recebido = float(recebido)
#         except ValueError:
#             pass

#     print(bool(recebido))
# if type(recebido) == int:
#     print("esse numero e inteiro")
# else: 
#     print("esse numero nao e inteiro")
dicionario = {
    "chave": 6, 
    "chave2": "texto"
}
lista = [1,2,3,4]

chave = dicionario["chave"]
chave2 = dicionario["chave2"]
# print(f"o valor da chave1 é {chave}")
# print(f"o valor da chave2 é {chave2}")
# print(dicionario.keys())
# print(dicionario.values())
print(dicionario)
dicionario["chave2"] = "Nathan"
print(dicionario)