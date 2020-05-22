import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter, MaxNLocator
import pickle

class Skyline():

    def __init__(self):
        # Atributs relacionats amb wl matplotlib per a poder dibuixar els rectangles
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
        self.pickleFile = 'plots.obj'



    # Configura la grafica com nosaltres volguem
    def configureAxis(self):
        self.ax = self.figura.add_subplot(111, aspect='equal')
        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))


    # Donat un edifici nou, recalcula les parts del Skyline
    def actualitzarParts(self,edifici):

        pass


    # Afegeix un nou edifici al SKyline
    def afegir(self, xmin, altura, xmax):
        inici = min(xmin,xmax)
        fi = max(xmax,xmin)
        base = fi-inici
        ini = (inici, 0)
        #new = Skyline()
        #Dibuixem el nou edifici
        #new.setPatch(inici,base,altura,self.color)
        self.ax.add_patch(
            patches.Rectangle(ini, base, altura, color=self.color))

        # Actualitzem Xmax, Altura, Xmin i Area totals del Skyline
        #new.setXmaxTotal(max(self.xmaxTotal,xmax))
        #new.setAlturaTotal(max(self.alturaTotal,altura))
        #new.setAreaTotal(base*altura)
        self.xmaxTotal = max(self.xmaxTotal,fi)
        self.alturaTotal = max(self.alturaTotal,altura)
        self.areaTotal += (base * altura)
        if self.xminTotal != -1:
            self.xminTotal = min(self.xminTotal, inici)
            #new.setXminTotal(min(self.xminTotal, xmin))
        else:
            #new.setXminTotal(xmin)
            self.xminTotal = inici

        # Especifiquem els limits del eixos
        self.ax.set_ylim(0, self.alturaTotal + 1)
        self.ax.set_xlim(0, self.xmaxTotal + 1)

        #new.setLimits()

        # Afegim al llistat d'accions el que acabem de fer
        self.llistaAccions.append((inici, altura, fi))
        #new.setLlistaAccions(self.llistaAccions.append((xmin, altura, xmax)))

        self.actualitzarParts((inici,altura,fi))
        #new.setParts(self.llistaParts)
        #new.actualitzarParts((xmin,altura,xmax))


        #Retornem l'altura i area toral del Skyline
        return self


    # Donat un nombre n, desplacem l'Skyline n posicions a la dreta
    def moureDreta(self, n):
        # Resetejarem tots els atributs per a que s'adequin a la modificació
        novaLlistaAccions = []
        ultimesAccions = self.llistaAccions.copy()

        # Borrem la fiura actual per a poder repintar la nova
        self.figura.clf()
        self.figura = plt.figure()
        self.configureAxis()

        # Reiniciem atributs
        self.llistaParts = []
        self.areaTotal = 0

        # Anem re-calculan el Xmin, Altura i Xmax sumantt el offset, i anem dibuixant pas a pas.
        for accio in ultimesAccions:
            novaAccio = (accio[0]+n, accio[1], accio[2] + n)
            novaLlistaAccions.append(novaAccio)

            self.afegir(novaAccio[0], novaAccio[1], novaAccio[2])

        #Reiniciem els atributs
        self.llistaAccions = novaLlistaAccions
        self.xmaxTotal = self.xmaxTotal + n
        self.xminTotal = self.xminTotal + n
        return self


    # Donat un nombre n, desplacem l'Skyline n posicions a l'esquerra
    def moureEsquerra(self, n):
        # Resetejarem tots els atributs per a que s'adequin a la modificació
        novaLlistaAccions = []
        ultimesAccions = self.llistaAccions.copy()

        # Borrem la fiura actual per a poder repintar la nova
        self.figura.clf()
        self.figura = plt.figure()
        self.configureAxis()

        # Reiniciem atributs
        self.llistaParts = []
        self.areaTotal = 0

        # Comprovem que no ens passem al desplaçar a l'esquerra
        if (self.xminTotal - n < 0):
            print('MoureEsquerra: No es pot moure tan a la esquerra, xmin = 0')
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
        return self


    # Donat un nombre de repeticions, replica el Skyline actual n cops
    def replicar (self, n):
        # Accedirem a les accions passades per a replicar-les una a una.
        ultimesAccions = self.llistaAccions.copy()
        fi = self.xmaxTotal
        for i in range (1,n):
            for accio in ultimesAccions:
                # Anem calculan el Xmin, ALtura i Xmax, i anem dibuixant pas a pas.
                altura = accio[1]
                xmin = (fi * i) + (accio[0])
                xmax = (fi * i) + (accio[2])
                #print('Replicar: Accio', accio, xmin, xmax)
                self.afegir(xmin, altura, xmax)


        # Retornem l'altura i area toral del Skyline
        return self


    #Donades unes accions, ens retorna una llista amb el Skyline dividid per parts (Metode auxiliar de intersecció)
    def trobarParts(self,accions):
        alturaT = -1
        xmaxT = -1
        xminT = -1
        xminAnterior = -1
        xmaxAnterior = -1
        alturaAnterior = -1
        l = []
        llista = []

        primer = True
        ultim = True
        for elem in accions:
            if (primer):
                xminT = elem[0]
                xmaxT = elem[2]
                alturaT = elem[1]
                primer = False

            elif(elem[0] == xmaxT and elem[1] == alturaT):
                llista = [xminT,alturaT,elem[2]]
                xmaxT = elem[2]
                ultim = True

            elif(elem[0] == xminAnterior and elem[2] == xmaxAnterior and alturaAnterior != elem[1]):
                llista = [xminAnterior,max(alturaAnterior,elem[1]),xmaxAnterior]
                alturaT = max(alturaAnterior,elem[1])
                ultim = True

            elif (elem[1] != alturaT):
                if (len(llista) > 0):
                    l.append(llista)
                else:
                    l.append([xminAnterior,alturaAnterior,xmaxAnterior])
                alturaT = elem[1]
                llista = []

            else:
                xminT = elem[0]
                xmaxT = elem[2]
                alturaT = elem[1]

            xminAnterior = elem[0]
            xmaxAnterior = elem[2]
            alturaAnterior = elem[1]

        if ultim:
            if (len(llista) > 0):
                l.append(llista)
            else:
                l.append([xminAnterior, alturaAnterior, xmaxAnterior])
        return l


    # Donada una accio i una part d'un Skyline, ens retorna l'edifici que cap en el espai que delimita la part (Metode auxiliar de intersecció)
    def capDins(self,accio,part):
        #Per cabre, cal que l'edifici estigui abans del xmax de la part i que el xmin
        if (part[2] > accio[0] and part[0] <= accio[2] and accio[0]):
            # Si l'accio es més petita que la part, podem pintar l'edifici sencer
            if(part[2] >= accio[2]):
                print ('CapDins Sencer:',accio,part,accio[0], min(part[1],accio[1]), accio[2])
                return (accio[0],min(part[1],accio[1]),accio[2])
            # Si l'accio es més gran que la part, hem de pintar un tros del edifici
            else:
                print ('CapDins tros:',accio,part,part[0], min(part[1],accio[1]), part[2])
                return (max(part[0],accio[0]), min(part[1],accio[1]), part[2])
        # Sino, no cap el edifici
        else:
            return ()


    # Donat un Skyline, calcula l'intersecció entre el parametre implicit i b
    def interseccio(self, sk):

        # Ordenem les accions dels dos skylines
        llistaAccionsNoves = sk.getLlistaAccions()
        llistaAccionsNoves.sort(key=lambda x: x[0])
        self.llistaAccions.sort(key=lambda x: x[0])

        # Dividim el Skyline principal en parts (per a que sigui mes facil)
        print('Interseccio: Accions B', llistaAccionsNoves)
        parts = self.trobarParts(self.llistaAccions)
        print('Interseccio: Parts A', parts)

        # Borrem la fiura actual per a poder repintar la nova
        self.figura.clf()
        self.figura = plt.figure()
        self.configureAxis()

        # Especifiquem que volem pintar la interseccio de color blau
        self.color = 'Blue'
        self.areaTotal = 0

        # Per cada nova accio a afegir, mirarem si cap dins de cada part del skyline principal. Si cap,
        # pintarem l'intersecció
        for accio in llistaAccionsNoves:
            for part in parts:
                edifici = self.capDins(accio,part)
                if (len(edifici) > 0):
                    self.afegir(edifici[0], edifici[1], edifici[2])
        return self


    # Donat un Skyline, calcula l'unió entre el parametre implicit i b
    def unio(self, sk):
        llistaAccionsUnir = sk.getLlistaAccions()
        print('Unio:',llistaAccionsUnir)

        # Reiniciem la llista de parts
        self.llistaParts = []

        for accio in llistaAccionsUnir:
            # print(accio)
            # Anem calculan el Xmin, ALtura i Xmax, i anem dibuixant pas a pas.
            self.afegir(accio[0], accio[1], accio[2])
        return self


    # Calcula l'Skyline reflectit
    def mirall(self):

        # Ens quedem amb el inici del Skyline i posem del reves la llista de accions
        inici = self.xminTotal
        #print('Mirall: accions', self.llistaAccions)

        # Fem una copia per a poder iterar sobre ella, si iteressim sobre l'atribut directament,
        # entariem en bucle infinit ja que cada cop que dibuixem, afegim una entrada a la llista d'accions
        ultimesAccions = self.llistaAccions.copy()
        ultimesAccions.sort(key=lambda x: x[0], reverse=True)
        print('Mirall: accions', ultimesAccions)
        # Borrem la fiura actual per a poder repintar la nova
        self.figura.clf()
        self.figura = plt.figure()
        self.configureAxis()
        self.llistaAccions = []

        # Reiniciem atributs
        self.llistaParts = []
        self.areaTotal = 0

        xminAnterior = ultimesAccions[0][2]

        # Per cada accio (amb la llista girada), anem dibuixant recalculant el inici i el final
        for accio in ultimesAccions:
            base = accio[2] - accio[0]
            altura = accio[1]
            espai = xminAnterior - accio[2] #Espai entre la figura actual i la següent

            #Coloquem la figura al inici més el espai que li pertoca
            xmin = inici + espai
            xmax = xmin + base
            print('Mirall: Nou edifici', xmin, altura, xmax)
            self.afegir(xmin, altura, xmax)
            inici = xmax
            xminAnterior = accio[0]

        return self

    # Consulta el paramtere a l'atribut llistaAccions
    def getLlistaAccions(self):
        return self.llistaAccions


    # Consulta l'atribut llistaParts
    def getLlistaParts(self):
        return self.llistaParts


    # Consulta la figura del Skyline
    def getFigura(self):
        return self.figura


    # Consulta l'area del Skyline
    def getArea(self):
        return self.areaTotal


    # Consulta l'altura del Skyline
    def getAltura(self):
        return self.alturaTotal








    # Retorna el skyline guardat a file en format Pickle
    def getSkyline(self,file):
        with open(file, 'rb') as file:
            fig1 = pickle.load(file)
            return fig1


    # Guarda el skyline a file en format Pickle
    def saveSkyline(self,file):
        with open(file, 'wb') as file:
            pickle.dump(self, file)


    #Guarda en el fitxer file el Skyline en formay imatge
    def mostrar(self,file):
        # Guardem Imatge, amb el segon parametre fem que la grafica es vegi més gran.
        #print('Guardo Image de',self.llistaAccions)
        self.figura.savefig(file, bbox_inches='tight')
        plt.close(self.figura)
        return self


'''
a = Skyline()
#a.afegir(1,2,2)
#a.afegir(2,4,4)
#a.afegir(4,2,8)
a.afegir(1,4,3)
a.afegir(3,8,5)
a.afegir(5,4,9)
a.mirall()
plt.show()
'''