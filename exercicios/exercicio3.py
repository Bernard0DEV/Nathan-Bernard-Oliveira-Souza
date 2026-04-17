PALAVRA_COMPLETA = "JSNERY"
PALAVRA_INCOMPLETA = "JS__RY"
SILABA_FALTANTE = "NE"

silabas_usadas = []

print(f"A palavra é: {PALAVRA_INCOMPLETA}")
while True:
    silabas_inserida = input("Qual é a sílaba?").upper()

    if silabas_inserida == SILABA_FALTANTE:
        print("Você acertou a sílaba!")
        break
    elif silabas_inserida in silabas_usadas: 
        print("Essa sílaba está incorreta e já foi tentada!")
    else:
        silabas_usadas.append(silabas_inserida)
        print(f"Sílaba incorreta: {silabas_usadas}")