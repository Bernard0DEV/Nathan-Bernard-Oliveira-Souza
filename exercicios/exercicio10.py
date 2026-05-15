class Praca:
    def __init__(self, pessoas, assento, lanchonete):
        self.pessoas = pessoas
        self.assento = assento
        self.lanchonete = lanchonete

    def condicoes_lanchonete(self) -> str:
       self.lanchonete = lanchonete
       if self.lanchonete == "Lanchou cagou":
            return "A lanchonete está em más condições, escolha outro lugar para comer!"   
        elif self.lanchonete == "Lanchou pagou":
            return "A lanchonete está em boas condições, pode comer lá!"
        else:
            return "A lanchonete está em condições regulares, escolha outro lugar para comer ou coma lá por sua conta e risco!"

praca = Praca("fedendo a inhaca", "Tudo quebrado", "Lanchou cagou")
print(praca.condicoes_lanchonete())