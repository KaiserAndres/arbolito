class Rama:
    def __init__(self, numero_elementos):
        self.numero_elementos = numero_elementos
        self.siguientes = [Hoja() for i in range(numero_elementos)]

    def crecer(self):
        for i, e in enumerate(self.siguientes):
            if e is Hoja:
                self.siguientes[i] = Rama(self.numero_elementos)
            elif e is Rama:
                e.crecer()

    def __str__(self):
        my_string = "R"
        for sig in self.siguientes:
            my_string += "(" + sig.__str__() + ")"
