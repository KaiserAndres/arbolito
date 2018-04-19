from hoja import Hoja


class Rama:
    def __init__(self, numero_elementos):
        self.numero_elementos = numero_elementos
        self.siguientes = [Hoja() for i in range(numero_elementos)]

    def crecer(self):
        for i in range(self.numero_elementos):
            self.siguientes[i] = Rama(self.numero_elementos)

    def __str__(self):
        my_string = "R"
        for sig in self.siguientes:
            if sig is Hoja:
                my_string += "H"
            elif sig is Rama:
                my_string += "(" + sig.__str__() + ")"
