
class Rama:
    def __init__(self, numero_elementos):
        self.numero_elementos = numero_elementos
        self.siguientes = []

    def crecer(self):
        for _ in range(self.numero_elementos):
            self.siguientes.append(Rama(self.numero_elementos))

    def __str__(self):
        my_string = "R("
        if self.siguientes:
            for sig in self.siguientes:
                my_string += sig.__str__()
        else:
            for _ in range(self.numero_elementos):
                my_string += 'H'
        my_string += ')'
        return my_string
