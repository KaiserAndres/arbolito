
class Rama:
    def __init__(self, numero_elementos):
        '''
        :param numero_elementos: Cantidad de ramas que tendra cuando crezca.
        '''
        self.numero_elementos = numero_elementos
        self.siguientes = []

    def crecer(self):
        '''
        Crear nuevas ramas segun el número de elementos.
        Si las ramas ya existen, pasa la llamada a ellas para que estas crezcan.
        '''
        if self.siguientes:
            for sig in self.siguientes:
                sig.crecer()
        else:
            for i in range(self.numero_elementos):
                self.siguientes.append(Rama(self.numero_elementos))

    def __str__(self):
        '''
        :return: Una representación en texto de la estructura del árbol.
        '''
        my_string = "R("
        if self.siguientes:
            for i, sig in enumerate(self.siguientes):
                my_string += sig.__str__()
                if i != self.numero_elementos - 1:
                    my_string += ', '
        else:
            for i in range(self.numero_elementos):
                my_string += 'H'
                if i != self.numero_elementos - 1:
                    my_string += ', '
        my_string += ')'
        return my_string
