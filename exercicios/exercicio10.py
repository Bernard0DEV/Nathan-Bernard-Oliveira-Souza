class Praca:
    def __init__(self, pessoas, assento, lanchonete):
        self.pessoas = pessoas
        self.assento = assento
        self.lanchonete = lanchonete

    def condicoes_lanchonete(self) -> str:
        if self.lanchonete == "Lanchou cagou":
            return "A lanchonete está em más condições, escolha outro lugar para comer!"
        elif self.lanchonete == "Lanchou pagou":
            return "A lanchonete está em boas condições, pode comer lá!"
        else:
            return "Condição da lanchonete desconhecida."

praca = Praca("fedendo a inhaca", "Tudo quebrado", "Lanchou cagou")
print(praca.condicoes_lanchonete())s