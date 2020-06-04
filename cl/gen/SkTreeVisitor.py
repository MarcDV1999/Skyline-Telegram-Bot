import random
from skyline import Skyline

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from cl.gen.SkylineParser import SkylineParser
    from cl.gen.SkylineVisitor import SkylineVisitor


# This class defines a complete generic visitor for a parse tree produced by SkylineParser.
class SkTreeVisitor(SkylineVisitor):

    def __init__(self):
        self.taulaSimbols = {}
        self.auxiliarsRoot = 'Imatges/'
        self.SkyDBRoot = 'Skylines_DB/'
        self.file = self.auxiliarsRoot + 'FigActual.png'

    # Funció que visita l'arrel del AST
    def visitRoot(self, ctx: SkylineParser.RootContext):
        # Agafem el següent fill i el visitem.
        fill = next(ctx.getChildren())
        result = self.visit(fill)

        # En cas de ser un Skyline retornem la seva area i altura
        if (type(result) is Skyline):
            result.mostrar(self.file)
            return result.getArea(), result.getAltura()
        # Sino retornem l'expressió
        else:
            return result

    # Funció que visita l'AST on la seva arrel és una expressió
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        # Agafem tots els fills i mirem si hem arribat a una fulla o no
        fills = [n for n in ctx.getChildren()]

        # Si només tenim un fill, hem arribat a un NUM o una consulta
        if (len(fills) == 1):
            # Si es un num...
            try:
                # print('Expressio: Valor', fills[0].getText())
                return int(fills[0].getText())
            # Si es una consulta...
            except Exception as _:
                # print('Expresio: Consulta', self.visit(fills[0]))
                return self.visit(fills[0])

        # Sino, vol dir que estem en una expressió, formada per dos parametres i un simbol.
        # Tindrem algo del estil [3,+,4] per exemple
        elif(len(fills) == 3):
            print('Expressio', len(fills))
            f1 = self.visit(fills[0])
            f2 = self.visit(fills[2])
            simbol = fills[1]

            # Si l'expressió és un ( expr ), em quedo amb lo de dins només i passem dels parentesis
            if (f1 is None and f2 is None):
                return self.visit(fills[1])

            # Si la expressió és entre 2 Skylines
            if(type(f1) is Skyline):
                if (simbol == ctx.MES()):
                    return f1 + f2
                if (simbol == ctx.MULT()):
                    return f1 * f2
                if (simbol == ctx.MENYS()):
                    return f1 - f2

            # Si la expressió és entre Skyline i N
            elif(type(f1) is int):
                if(type(f2) is Skyline):
                    if (simbol == ctx.MULT()):
                        return f2 * f1
                    if (simbol == ctx.MES()):
                        return f2+f1
                    if (simbol == ctx.MENYS()):
                        return f2-f1
                if (type(f2) is int):
                    if (simbol == ctx.MES()):
                        return f1 + f2
                    if (simbol == ctx.MENYS()):
                        return f1 - f2
                    if (simbol == ctx.MULT()):
                        return f1 * f2
                    if (simbol == ctx.DIV()):
                        try:
                            return f1 / f2
                        except Exception as _:
                            print('Error, divisió per zero')
                    if (simbol == ctx.POT()):
                        return f1 ** f2

        # Sino, vol dir que estem en una expressió, formada per un simbol i un parametre.
        # És el cas del mirall
        elif(len(fills) == 2):
            simbol = fills[0]
            edifici = self.visit(fills[1])

            if(simbol == ctx.MENYS()):
                return -edifici

    # Funció que visita l'AST on la seva arrel és una assignació
    def visitAssignacio(self, ctx: SkylineParser.AssignacioContext):
        # Agafem tots els fills i extraiem el valor i la variable
        fills = [n for n in ctx.getChildren()]
        variable = fills[0].getText()
        valor = self.visit(fills[2])

        try:
            # Si el valor es un Skyline, l'afegim a la taula.
            if(type(valor) is Skyline):
                self.taulaSimbols[variable] = valor
                return valor

        except Exception as _:
            print('Assignacio Error: Estem assignant el num', valor, 'a la variable', variable)
            return None

    # Funció que visita l'AST on la seva arrel és una consulta
    def visitConsulta(self, ctx: SkylineParser.ConsultaContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        variable = fills[0].getText()

        # Mirem si trobem la variable a la nostra taula de simbols, i retornem el seu valor si podem
        if variable in self.taulaSimbols:
            return self.taulaSimbols[variable]
        else:
            print('Consulta: La variable {}, no la tinc'.format(variable))
            return None

    # Funció que visita l'AST on la seva arrel és una edifici
    def visitEdifici(self, ctx: SkylineParser.EdificiContext):
        # Agafem els seus fills i ens quedem amb xmin, altura, xmax
        fills = [n for n in ctx.getChildren()]

        xmin = self.visit(fills[1])
        altura = self.visit(fills[3])
        xmax = self.visit(fills[5])

        # Creem un nou Skyline i el retornem amb les dades corresponents
        newSk = Skyline()
        newSk.afegir(xmin, altura, xmax)

        return newSk

    # Funció que visita l'AST on la seva arrel és un conjunt d'edificis
    def visitEdificis(self, ctx: SkylineParser.EdificisContext):
        # Agafem dels seus fills els diferents edificis
        fills = [n for n in ctx.getChildren()]
        # Creem un nou Skyline (sera el que retornarem)
        newSk = Skyline()

        for f in fills:
            # Anem afegint al newSk els diversos edificis
            sk = self.visit(f)
            if (type(sk) is Skyline):
                print('valor', newSk)
                newSk = newSk + sk
        return newSk

    # Funció que visita l'AST on la seva arrel és un edifici aleatori
    def visitEdificiAleatori(self, ctx: SkylineParser.EdificiAleatoriContext):
        # Agafem dels seus fills i ens qedem amb els parametres que ens interessen
        fills = [n for n in ctx.getChildren()]
        n = self.visit(fills[1])
        h = self.visit(fills[3])
        w = self.visit(fills[5])
        xmin = self.visit(fills[7])
        xmax = self.visit(fills[9])

        newSk = Skyline()

        # Anem creant tants edificis com ens demanin
        for edifici in range(0, n):
            # Calculem aleatoriament cada edifici
            random.seed()
            newH = random.randint(1, h)
            newW = random.randint(1, w)
            newXmin = random.randint(xmin, xmax - newW)
            newXmax = newXmin + newW
            newSk.afegir(newXmin, newH, newXmax)
        return newSk

    # Funció que retorna l'atribut taula de simbols
    def getTaulaSimbols(self):
        return self.taulaSimbols

    # Funció que assigna dict a l'atribut taulaSimbols
    def setTaulaSimbols(self, dict):
        self.taulaSimbols = dict

    # Funció que guarda el Skyline amb id id, en el arxiu id.sky
    def saveSkyline(self, id, username):
        try:
            sk = self.taulaSimbols[id]
            nameToSave = id+username
            sk.saveSkyline('{}{}.sky'.format(self.SkyDBRoot, nameToSave))
            sk.mostrar(self.file)
        except Exception as _:
            print('No tinc aquest Skyline')

    # Funció que carrega el Skyline amb id id, del arxiu id.sky
    def loadSkyline(self, id, username):
        try:
            sk = Skyline()
            nameToLoad = id+username
            sk = sk.getSkyline('{}{}.sky'.format(self.SkyDBRoot, nameToLoad))
            self.taulaSimbols[id] = sk
            sk.mostrar(self.file)
            return sk

        except Exception as _:
            print('No tinc aquest Skyline guardat')
            return None

    # Funció que donat un Skyline, en retorna un copia
    # def duplicarSkyline(self, sk):
    #    sk.saveSkyline('{}SkylineActual.pickle'.format(self.auxiliarsRoot))
    #   sk = sk.getSkyline('{}SkylineActual.pickle'.format(self.auxiliarsRoot))
    #    return sk


del SkylineParser
