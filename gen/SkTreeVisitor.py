# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Practica Pyhton i Compiladors/Compilador/Skyline.g4 by ANTLR 4.8
from antlr4 import *
import random
from Skyline import Skyline

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from gen.SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkTreeVisitor(SkylineVisitor):
    a = Skyline()
    b = Skyline()
    a.afegir(1,2,3)
    b.afegir(3,2,10)
    taulaSimbols = {'a':a,'b':b}
    file = 'image.png'

    # Funció que visita l'arrel del AST
    def visitRoot(self, ctx:SkylineParser.RootContext):
        # Agafem el següent fill i el visitem.
        # En cas de ser una expressio, retorna un valor, per tant el mostrem
        fill = next(ctx.getChildren())
        #print('fill',fill)
        result = self.visit(fill)
        print('result:',type(result))
        if (type(result) is Skyline):
            print('Voy a mostrar')
            result.mostrar(self.file)
        print('---------------------',result.getArea(),'---------------------')
        return result.getArea(),result.getAltura()


    # Funció que visita l'AST on la seva arrel és una expressió
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        # Agafem tots els fills i mirem si hem arribat a una fulla o no
        fills = [n for n in ctx.getChildren()]

        # Si només tenim un fill, hem arribat a un NUM o una consulta
        if (len(fills) == 1):
            # Si es un num...
            try:
                print('Expressio: Valor', fills[0].getText())
                return int(fills[0].getText())
            # Si es una consulta...
            except:
                print('Expresio: Consulta',self.visit(fills[0]))
                return self.visit(fills[0])

        # Sino, vol dir que estem en una expressió, formada per dos parametres i un simbol.
        # Tindrem algo del estil [3,+,4] per exemple
        # En aquest cas retornem el resultat de l'operació desitjada
        elif(len(fills) == 3):
            print('Expressio',len(fills))
            f1 = self.visit(fills[0])
            f2 = self.visit(fills[2])
            simbol = fills[1]

            # Si la expressió és entre 2 Skylines
            if(type(f1) is Skyline and type(f2) is Skyline):
                print('Expressio: Skyline + Skyline', f1, f2)
                if (simbol == ctx.MES()):
                    return f1.unio(f2)
                if (simbol == ctx.MULT()):
                    return f1.interseccio(f2)
            # Si la expressió és entre Skyline i N
            elif(type(f1) is Skyline and type(f2) is int):
                print('Expressio: Skyline + Num', f1, f2)
                if (simbol == ctx.MULT()):
                    return f1.replicar(int(f2))
                if (simbol == ctx.MES()):
                    return f1.moureDreta(int(f2))
                if (simbol == ctx.MENYS()):
                    return f1.moureEsquerra(int(f2))

            # Si la expressió és entre N i Skyline
            elif (type(f2) is Skyline):
                print('Expressio: Num + Skyline', f1, f2)
                #f2.saveSkyline()
                #fAux = f1.getSkyline()
                if (simbol == ctx.MULT()):
                    return f2.replicar(f1)
                if (simbol == ctx.MES()):
                    return f2.moureDreta(f1)
                if (simbol == ctx.MENYS()):
                    return f2.moureEsquerra(f1)

        elif(len(fills) == 2):
            simbol = fills[0]
            edifici = self.visit(fills[1])
            if(simbol == ctx.MENYS() and type(edifici) is Skyline):
                return edifici.mirall()
            elif(simbol == ctx.MENYS() and type(edifici) is tuple):
                newSk = Skyline()
                newSk.afegir(edifici[0],edifici[1],edifici[2])
                return newSk.mirall()



    def visitAssignacio(self, ctx:SkylineParser.AssignacioContext):
        # Ara mateix si posem a : 6 (error), salta un error per segueix afegint al diccionar la variable
        # Agafem tots els fills i extraiem el valor i la variable
        #print('Visitem Assignacio')
        fills = [n for n in ctx.getChildren()]
        # El valor, l'obtindrem de evaluar l'expressió del 3r fill
        variable = fills[0].getText()
        print('Assignacio: valor->',fills[2].getText())
        valor = self.visit(fills[2])

        print('Assignacio: Guardarem a ->',variable)
        print('Assignacio: valor', str(valor))

        try:
            #Si el valor es un Skyline, l'afegim a la taula, el guardem, i el mostrem
            if(type(valor) is Skyline):
                self.taulaSimbols[variable] = valor
                self.taulaSimbols[variable].saveSkyline('FIG-{}.obj'.format(variable))
                self.taulaSimbols[variable] = valor.mostrar(self.file)
                return valor
            #Si es una tupla, primer hem de crear el Skyline
            elif(type(valor) is tuple):
                newSk = Skyline()
                newSk.afegir(valor[0],valor[1],valor[2])
                newSk.mostrar('fig-{}.png'.format(variable))
                newSk.saveSkyline('fig-{}.obj'.format(variable))
                return newSk

        except:
            print('Assignacio Error: Estem assignant el num',valor,'a la variable',variable)
            return None


    def visitConsulta(self, ctx:SkylineParser.ConsultaContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        variable = fills[0].getText()
        #print('Consulta',variable)

        #Mirem si trobem la variable a la nostra taula de simbols, i retornem el seu valor si podem
        if variable in self.taulaSimbols:
            sk = self.taulaSimbols[variable]
            sk = sk.getSkyline('FIG-{}.obj'.format(variable))
            sk.mostrar(self.file)
            return sk

        else:
            print('Consulta: La variable {}, no la tinc'.format(variable))


    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        #for f in fills:
            #print(f.getText())
        xmin = self.visit(fills[1])
        altura = self.visit(fills[3])
        xmax = self.visit(fills[5])

        #xmin = int(fills[1].getText())
        #altura = int(fills[3].getText())
        #xmax = int(fills[5].getText())

        #print('xmin', xmin)
        #print('altura', altura)
        #print('xmax', xmax)
        return xmin, altura, xmax


    def visitEdificis(self, ctx:SkylineParser.EdificisContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        llista = []

        for f in fills:
            tipus = type(f).__name__
            #Només guardarem a la llista tots aquells tokens que siguin del tipus Edifici.
            # No volem ni els [ ni res per l'estil
            if ( tipus == 'EdificiContext'):
                llista.append(f.getText())
        return llista


    def visitEdificiAleatori(self, ctx:SkylineParser.EdificiAleatoriContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        # for f in fills:
        # print(f.getText())
        n = self.visit(fills[1])
        h = self.visit(fills[3])
        w = self.visit(fills[5])
        xmin = self.visit(fills[7])
        xmax = self.visit(fills[9])

        random.seed()
        h = random.randint(0,h)
        w = random.randint(1,w)
        mitad = int((xmin + xmax)/2)
        xmin = random.randint(xmin, mitad)
        xmax = random.randint(mitad, xmax)


        return (n, h, w, xmin, xmax)


del SkylineParser









