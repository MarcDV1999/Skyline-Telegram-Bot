import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
import pickle


class Skyline():

    # Deixem de mostrar les figures per pantalla, només volem guardar-les en una imatge
    plt.switch_backend('Agg')

    # Constructor
    def __init__(self):
        # Atributs relacionats amb el matplotlib per a poder dibuixar els rectangles
        self.figura = plt.figure()
        self.configureAxis()

        # Atributs del Skyline
        self.alturaTotal = 0
        self.xminTotal = -1
        self.xmaxTotal = 0
        self.areaTotal = 0
        self.color = 'red'

        # Llista on anirem guardant tots els passos que anem fent per a generar el Skyline
        self.llistaAccions = []
        self.llistaParts = []

    # Redefinim el operador de suma
    def __add__(self, other):
        tipus = type(other)
        if(tipus is Skyline):
            return self.unio(other)
        elif(tipus is int):
            return self.moureDreta(other)
        else:
            return None

    # Redefinim el operador de resta
    def __sub__(self, other):
        tipus = type(other)
        if (tipus is int):
            return self.moureEsquerra(other)
        else:
            return None

    # Redefinim el operador de multiplicacio
    def __mul__(self, other):
        tipus = type(other)
        if (tipus is Skyline):
            return self.interseccio(other)
        elif (tipus is int):
            return self.replicar(other)
        else:
            return None

    # Redefinim el operador de negacio
    def __neg__(self):
        return self.mirall()

    # Configura la grafica com nosaltres volguem
    def configureAxis(self):
        self.ax = self.figura.add_subplot(111, aspect='equal')
        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Afegeix un nou edifici al SKyline
    def afegir(self, xmin, altura, xmax):
        inici = min(xmin, xmax)
        fi = max(xmax, xmin)
        base = fi-inici
        ini = (inici, 0)

        # Només fem modificacions si xmin es diferent a xmax
        if (xmin != xmax):
            # Dibuixem el nou edifici
            self.ax.add_patch(
                patches.Rectangle(ini, base, altura, color=self.color))

            # Actualitzem Xmax, Altura, Xmin i Area totals del Skyline
            self.xmaxTotal = max(self.xmaxTotal, fi)
            self.alturaTotal = max(self.alturaTotal, altura)
            self.areaTotal += (base * altura)
            if self.xminTotal != -1:
                self.xminTotal = min(self.xminTotal, inici)
            else:
                self.xminTotal = inici

            # Especifiquem els limits del eixos
            self.ax.set_ylim(0, self.alturaTotal + 1)
            self.ax.set_xlim(0, self.xmaxTotal + 1)

            # Afegim al llistat d'accions el que acabem de fer
            self.llistaAccions.append((inici, altura, fi))

        # Retornem el Skyline
        return self

    # Donat un nombre n, desplacem l'Skyline n posicions a la dreta
    def moureDreta(self, n):
        newSk = Skyline()
        # Resetejarem tots els atributs per a que s'adequin a la modificació
        novaLlistaAccions = []
        ultimesAccions = self.llistaAccions.copy()

        # Anem re-calculan el Xmin, Altura i Xmax sumantt el offset, i anem dibuixant pas a pas.
        for accio in ultimesAccions:
            novaAccio = (accio[0] + n, accio[1], accio[2] + n)
            novaLlistaAccions.append(novaAccio)
            # Anem afegint les accions
            newSk.afegir(novaAccio[0], novaAccio[1], novaAccio[2])

        return newSk

    # Donat un nombre n, desplacem l'Skyline n posicions a l'esquerra
    def moureEsquerra(self, n):
        newSk = Skyline()
        # Resetejarem tots els atributs per a que s'adequin a la modificació
        novaLlistaAccions = []
        ultimesAccions = self.llistaAccions.copy()

        # Comprovem que no ens passem al desplaçar a l'esquerra
        if (self.xminTotal - n < 0):
            n = n - (n - self.xminTotal)

        # Anem re-calculan el Xmin, Altura i Xmax sumantt el offset, i anem dibuixant pas a pas.
        for accio in ultimesAccions:
            novaAccio = (accio[0] - n, accio[1], accio[2] - n)
            novaLlistaAccions.append(novaAccio)

            newSk.afegir(novaAccio[0], novaAccio[1], novaAccio[2])

        return newSk

    # Donat un nombre de repeticions, replica el Skyline actual n cops
    def replicar(self, n):
        newSk = Skyline()
        # Accedirem a les accions passades per a replicar-les una a una.
        ultimesAccions = self.llistaAccions.copy()
        fi = self.xmaxTotal
        for i in range(0, n):
            for accio in ultimesAccions:
                # Anem calculan el Xmin, Altura i Xmax, i anem dibuixant pas a pas.
                altura = accio[1]
                xmin = (fi * i) + (accio[0])
                xmax = (fi * i) + (accio[2])
                newSk.afegir(xmin, altura, xmax)

        return newSk

    # Donades unes accions, ens retorna una llista amb el Skyline dividid per parts (Metode auxiliar de intersecció)
    def trobarParts(self, accions):

        # Ordenem les accions per ordre d'inici
        accions.sort(key=lambda x: x[0])
        alturaT = xmaxT = xminT = xminAnterior = xmaxAnterior = alturaAnterior = -1
        primer = ultim = True

        llistaParts = []
        part = []

        # Per cada acció, mirarem si forma part de la part anterior o no.
        # D'aquesta manera anirem reconstruint les diverses parts del Skyline
        for accio in accions:
            if (primer):
                xminT = accio[0]
                xmaxT = accio[2]
                alturaT = accio[1]
                primer = False

            elif(accio[0] == xmaxT and accio[1] == alturaT):
                part = [xminT, alturaT, accio[2]]
                xmaxT = accio[2]
                ultim = True

            elif(accio[0] == xminAnterior and accio[2] == xmaxAnterior and alturaAnterior != accio[1]):
                part = [xminAnterior, max(alturaAnterior, accio[1]), xmaxAnterior]
                alturaT = max(alturaAnterior, accio[1])
                ultim = True

            elif (accio[1] != alturaT):
                if (len(part) > 0):
                    llistaParts.append(part)
                else:
                    llistaParts.append([xminAnterior, alturaAnterior, xmaxAnterior])
                alturaT = accio[1]
                part = []

            else:
                xminT = accio[0]
                xmaxT = accio[2]
                alturaT = accio[1]

            xminAnterior = accio[0]
            xmaxAnterior = accio[2]
            alturaAnterior = accio[1]

        if ultim:
            if (len(part) > 0):
                llistaParts.append(part)
            else:
                llistaParts.append([xminAnterior, alturaAnterior, xmaxAnterior])
        return llistaParts

    # Donada una accio i una part d'un Skyline, ens retorna l'edifici que cap en el espai que delimita la part (Metode auxiliar de intersecció)
    def capDins(self, accio, part):
        # Per cabre, cal que l'edifici estigui abans del xmax de la part i que el xmin
        if (part[2] > accio[0] and part[0] <= accio[2] and accio[0]):
            # Si l'accio es més petita que la part, podem pintar l'edifici sencer
            if(part[2] >= accio[2]):
                return (accio[0], min(part[1], accio[1]), accio[2])
            # Si l'accio es més gran que la part, hem de pintar un tros del edifici
            else:
                return (max(part[0], accio[0]), min(part[1], accio[1]), part[2])
        # Sino, no cap el edifici en la part especificada
        else:
            return None

    # Donat un Skyline, calcula l'intersecció entre el parametre implicit i b
    def interseccio(self, other):

        newSk = Skyline()

        # Ordenem les accions dels dos skylines per xmin
        llistaAccionsNoves = other.getLlistaAccions()
        llistaAccionsNoves.sort(key=lambda x: x[0])
        self.llistaAccions.sort(key=lambda x: x[0])

        # Dividim el Skyline principal en parts (per a que sigui mes facil)
        parts = self.trobarParts(self.llistaAccions)
        part2 = self.trobarParts(llistaAccionsNoves)

        # Per cada nova accio a afegir, mirarem si cap dins de cada part del skyline principal. Si cap,
        # pintarem l'intersecció
        for accio in part2:
            for part in parts:
                edifici = self.capDins(accio, part)
                if (edifici is not None):
                    newSk.afegir(edifici[0], edifici[1], edifici[2])
        return newSk

    # Donat un Skyline, calcula l'unió entre el parametre implicit i b
    def unio(self, other):
        newSk = Skyline()
        llistaAccionsUnir = other.getLlistaAccions()
        for accio in llistaAccionsUnir:
            # Anem calculan el Xmin, ALtura i Xmax, i anem dibuixant pas a pas.
            newSk.afegir(accio[0], accio[1], accio[2])

        for accio in self.llistaAccions:
            # Anem calculan el Xmin, ALtura i Xmax, i anem dibuixant pas a pas.
            newSk.afegir(accio[0], accio[1], accio[2])

        # Reiniciem la llista de parts i recalculem l'area
        newSk.llistaParts = self.trobarParts(self.llistaAccions)

        # Per cada part, recalculem l'area
        for part in self.llistaParts:
            base = part[2] - part[0]
            altura = part[1]
            newSk.areaTotal += (base * altura)

        return newSk

    # Calcula l'Skyline reflectit
    def mirall(self):

        newSk = Skyline()
        # Ens quedem amb el inici del Skyline i posem del reves la llista de accions
        inici = self.xminTotal

        # Fem una copia per a poder iterar sobre ella, si iteressim sobre l'atribut directament,
        # entariem en bucle infinit ja que cada cop que dibuixem, afegim una entrada a la llista d'accions
        ultimesAccions = self.llistaAccions.copy()
        ultimesAccions.sort(key=lambda x: x[0], reverse=True)

        xminAnterior = ultimesAccions[0][2]

        # Per cada accio (amb la llista girada), anem dibuixant recalculant el inici i el final
        for accio in ultimesAccions:
            base = accio[2] - accio[0]
            altura = accio[1]
            espai = xminAnterior - accio[2]  # Espai entre la figura actual i la següent

            # Coloquem la figura al inici més el espai que li pertoca
            xmin = inici + espai
            xmax = xmin + base
            newSk.afegir(xmin, altura, xmax)
            inici = xmax
            xminAnterior = accio[0]

        return newSk

    # Consulta el paramtere a l'atribut llistaAccions
    def getLlistaAccions(self):
        return self.llistaAccions

    # Consulta l'atribut llistaParts
    def getLlistaParts(self):
        return self.llistaParts

    # Consulta l'area del Skyline
    def getArea(self):
        return self.areaTotal

    # Consulta l'altura del Skyline
    def getAltura(self):
        return self.alturaTotal

    # Retorna el skyline guardat a file en format Pickle
    def getSkyline(self, file):
        with open(file, 'rb') as file:
            newSk = pickle.load(file)
            return newSk

    # Guarda el skyline a file en format Pickle
    def saveSkyline(self, file):
        with open(file, 'wb') as file:
            pickle.dump(self, file)

    # Guarda en el fitxer file el Skyline en formay imatge
    def mostrar(self, file):
        # Guardem Imatge, amb el segon parametre fem que la grafica es vegi més gran.
        self.figura.savefig(file, bbox_inches='tight')
        plt.close(self.figura)
        return self


'''
a = Skyline()
b = Skyline()
#a.afegir(1,2,2)
#a.afegir(2,4,4)
#a.afegir(4,2,8)
a.afegir(1,4,3)


b.afegir(8,6,15)
c = a+b

a.afegir(1,4,30)


plt.show()

'''
