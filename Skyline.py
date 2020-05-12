import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter, MaxNLocator

class Skyline():

    def __init__(self):
        # Atributs relacionats amb wl matplotlib per a poder dibuixar els rectangles
        self.figura = plt.figure()
        self.ax = self.figura.add_subplot(111, aspect='equal')
        self.configureAxis()

        # Atributs del Skyline
        self.alturaTotal = 0
        self.xminTotal = -1
        self.xmaxTotal = 0
        self.areaTotal = 0
        self.color = 'red'

        # Llista on anirem guardant tots els passos que anem fent per a generar el Skyline
        self.llistaAccions = []


    # Configura la grafica com nosaltres volguem
    def configureAxis(self):
        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))


    # Afegeix un nou edifici al SKyline
    def afegir(self, xmin, altura, xmax):
        base = xmax - xmin
        inici = (xmin, 0)

        #Dibuixem el nou edifici
        self.ax.add_patch(
            patches.Rectangle(inici, base, altura, color=self.color))

        # Actualitzem Xmax, Altura, Xmin i Area totals del Skyline
        self.xmaxTotal = max(self.xmaxTotal,xmax)
        self.alturaTotal = max(self.alturaTotal,altura)
        self.areaTotal += (base * altura)
        if self.xminTotal != -1:
            self.xminTotal = min(self.xminTotal, xmin)
        else:
            self.xminTotal = xmin

        # Especifiquem els limits del eixos
        plt.ylim(0, self.alturaTotal + 1)
        plt.xlim(0, self.xmaxTotal + 1)

        # Afegim al llistat d'accions el que acabem de fer
        self.llistaAccions.append((xmin, altura, xmax))

        #Retornem l'altura i area toral del Skyline
        return self.alturaTotal, self.areaTotal


    # Donat un nombre n, desplacem l'Skyline n posicions a la dreta
    def moureDreta(self, n):
        # Resetejarem tots els atributs per a que s'adequin a la modificació
        novaLlistaAccions = []
        ultimesAccions = self.llistaAccions.copy()

        # Borrem la fiura actual per a poder repintar la nova
        plt.cla()
        self.configureAxis()

        # Anem re-calculan el Xmin, Altura i Xmax sumantt el offset, i anem dibuixant pas a pas.
        for accio in ultimesAccions:
            novaAccio = (accio[0]+n, accio[1], accio[2] + n)
            novaLlistaAccions.append(novaAccio)

            self.afegir(novaAccio[0], novaAccio[1], novaAccio[2])

        #Reiniciem els atributs
        self.llistaAccions = novaLlistaAccions
        self.xmaxTotal = self.xmaxTotal + n
        self.xminTotal = self.xminTotal + n

    # Donat un nombre n, desplacem l'Skyline n posicions a l'esquerra
    def moureEsquerra(self, n):
        # Resetejarem tots els atributs per a que s'adequin a la modificació
        novaLlistaAccions = []
        ultimesAccions = self.llistaAccions.copy()

        # Borrem la fiura actual per a poder repintar la nova
        plt.cla()
        self.configureAxis()

        # Comprovem que no ens passem al desplaçar a l'esquerra
        if (self.xminTotal - n < 0):
            print('No es pot moure tan a la esquerra, xmin = 0')
            n = n - (n - self.xminTotal)

        # Anem re-calculan el Xmin, Altura i Xmax sumantt el offset, i anem dibuixant pas a pas.
        for accio in ultimesAccions:
            novaAccio = (accio[0] - n, accio[1], accio[2] - n)
            novaLlistaAccions.append(novaAccio)

            self.afegir(novaAccio[0], novaAccio[1], novaAccio[2])

        # Reiniciem els atributs
        self.llistaAccions = novaLlistaAccions
        self.xmaxTotal = self.xmaxTotal - n
        self.xminTotal = self.xminTotal - n


    # Donat un nombre de repeticions, replica el Skyline actual n cops
    def replicar (self, n):
        # Accedirem a les accions passades per a replicar-les una a una.
        ultimesAccions = self.llistaAccions.copy()
        for _ in range (1,n):
            for accio in ultimesAccions:
                print(accio)
                # Anem calculan el Xmin, ALtura i Xmax, i anem dibuixant pas a pas.
                base = accio[2] - accio[0]
                altura = accio[1]
                xmin = self.xmaxTotal
                xmax = self.xmaxTotal + base
                self.afegir(xmin, altura, xmax)


        # Retornem l'altura i area toral del Skyline
        return self.alturaTotal, self.areaTotal


    # Donat un Skyline, calcula l'intersecció entre el parametre implicit i b
    def interseccio(self, b):
        return False


    # Donat un Skyline, calcula l'unió entre el parametre implicit i b
    def unio(self, b):
        return False


    # Calcula l'Skyline reflectit
    def mirall(self):
        return False


    # Assigna el paramtere a l'atribut xminTotal
    def setXminTotal(self,xmin):
        self.xminTotal = xmin

    # Assigna el paramtere a l'atribut xmaxTotal
    def setXmaxTotal(self,xmax):
        self.xmaxTotal = xmax

    # Assigna el paramtere a l'atribut llistaAccions
    def setLlistaAccions(self,llistaAccions):
        self.llistaAccions = llistaAccions


a = Skyline()
a.afegir(1,2,3)
a.afegir(3,4,6)
a.replicar(3)
#a.afegir(16,6,19)
#a.replicar(3)
#a.moureDreta(2)
a.moureEsquerra(2)

plt.show()