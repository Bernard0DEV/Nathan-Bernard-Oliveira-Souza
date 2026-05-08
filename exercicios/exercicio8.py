def e_par(num):
    if num == 0.0:
        return False
    return num % 2 == 0

numero = input("Insira um número: ")
numero_convertido = 0.0

try: 
    numero_convertido = float(numero)
except ValueError as e:
    print(f"O valor inserido não é um número válido. {e} Tente novamente.")
if e_par(numero_convertido):
    print("Acesso permitido")
else:
    print("O número é invalido")


