class Bateria:
    def __init__(self,baterias, valores):
        self.bateria = baterias
        self.preço = valores

    def identifica (self):
        print("o valor da bateria é",self.preço, "e a marca é", self.bateria, "de amperagem")

        # class Bateriasds(Bateria) é uma classe mãe, exemplo de como fazer uma classe mãe e imprimir

class Bateriasds(Bateria):
    
    def __init__(self, baterias, valores,amperagens):
        super().__init__(baterias, valores)
        self.amperagens = amperagens

    def identifica (self):
        print("o valor da bateria é",self.preço, "e a marca é", self.bateria, "de amperagem é",self.amperagens)



bateria = Bateriasds('heliar',420, "60ah")
bateria.identifica ()





