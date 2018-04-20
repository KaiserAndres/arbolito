from tad.rama import Rama

if __name__ == '__main__':
    miArbol = Rama(2)
    for i in range(3):
        miArbol.crecer()
    print(miArbol)
