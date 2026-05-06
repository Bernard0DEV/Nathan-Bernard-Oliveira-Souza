"""
Operadores:
    - São símbolos que realizam operações em variáveis e valores.
    - Exemplos de operadores:
        - Aritméticos: +, -, *, /, // (divisão inteira), % (módulo), ** (exponenciação)
        - Relacionais: (==, !=, >, <, >=, <=) -> Sempre vai retornar um valor booleano (True ou False)
        - Lógicos: and, or, not

"""

variavel_1 = int(input("Digite o primeiro número: "))
variavel_2 = int(input("Digite o segundo número: "))
variavel_3 = int(input("Digite o terceiro número: "))
variavel_4 = int(input("Digite o quarto número: ")) 

if variavel_1 >= variavel_2 and variavel_3 == variavel_4:
    print("O primeiro valor é maior que o segundo valor e o terceiro e quarto valor são iguais")
    input("Aperte enter...\n")

if variavel_2 <= variavel_3 or variavel_1 != variavel_4: 
    print("O segundo valor é menor que o terceiro valor ou o primeiro valor é diferente do quarto valor")
    input("Aperte enter...\n")

if variavel_2 != variavel_4 and variavel_1 <= variavel_3: 
    print("O segundo valor é diferente do quarto valor e o primeiro valor é menor igual ao terceiro valor")
    input("Aperte enter...\n")

if variavel_3 == variavel_1 or variavel_2 > variavel_1: 
    print("O terceiro valor é igual ao primeiro valor ou o segundo valor é menor que o primeiro valor")
    input("Aperte enter...\n")
