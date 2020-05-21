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
        if (type(result) is Skyline):
            print('Voy a mostrar')
            result.mostrar(self.file)
            print('---------------------',result.getArea(),'---------------------')
            return result.getArea(),result.getAltura()
        else:
            return result


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
            if(type(f1) is Skyline):
                if(type(f2) is Skyline):
                    if (simbol == ctx.MES()):
                        return f1.unio(f2)
                    if (simbol == ctx.MULT()):
                        return f1.interseccio(f2)
                elif(type(f2) is int):
                    if (simbol == ctx.MULT()):
                        return f1.replicar(f2)
                    if (simbol == ctx.MES()):
                        return f1.moureDreta(f2)
                    if (simbol == ctx.MENYS()):
                        return f1.moureEsquerra(f2)


            # Si la expressió és entre Skyline i N
            elif(type(f1) is int):
                if(type(f2) is Skyline):
                    if (simbol == ctx.MULT()):
                        return f2.replicar(int(f1))
                    if (simbol == ctx.MES()):
                        return f2.moureDreta(int(f1))
                    if (simbol == ctx.MENYS()):
                        return f2.moureEsquerra(int(f1))
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
                        except:
                            print('Error, divisió per zero')
                    if (simbol == ctx.POT()):
                        return f1 ** f2


        elif(len(fills) == 2):
            simbol = fills[0]
            edifici = self.visit(fills[1])
            if(simbol == ctx.MENYS() and type(edifici) is Skyline):
                return edifici.mirall()




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

            elif (type(valor) is int):
                self.taulaSimbols[variable] = valor
                return valor

        except:
            print('Assignacio Error: Estem assignant el num',valor,'a la variable',variable)
            return None


    def visitConsulta(self, ctx:SkylineParser.ConsultaContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        variable = fills[0].getText()
        #print('Consulta',variable)

        #Mirem si trobem la variable a la nostra taula de simbols, i retornem el seu valor si podem
        if variable in self.taulaSimbols and type(self.taulaSimbols[variable]) is Skyline:
            sk = self.taulaSimbols[variable]
            sk = sk.getSkyline('FIG-{}.obj'.format(variable))
            sk.mostrar(self.file)
            return sk
        elif variable in self.taulaSimbols:
            return self.taulaSimbols[variable]

        else:
            print('Consulta: La variable {}, no la tinc'.format(variable))


    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]

        xmin = self.visit(fills[1])
        altura = self.visit(fills[3])
        xmax = self.visit(fills[5])

        #Creem un nou Skyline i el retornem amb les dades corresponents
        newSk = Skyline()
        newSk.afegir(xmin,altura,xmax)

        return newSk


    def visitEdificis(self, ctx:SkylineParser.EdificisContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        #Creem un nou Skyline (sera el que retornarem)
        newSk = Skyline()

        for f in fills:
            tipus = type(f).__name__
            #Anem afegint al newSk els diversos edificis
            if ( tipus == 'EdificiContext'):
                valor = f.getText()
                newSk.afegir(int(valor[1]),int(valor[3]),int(valor[5]))
        return newSk


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

        # Calculem aleatoriament el primer edifici
        random.seed()
        newH = random.randint(0,h)
        newW = random.randint(1,w)
        newXmin = random.randint(xmin, xmax-newW)
        newXmax = newXmin + w

        newSk = Skyline()
        newSk.afegir(newXmin,newH,newXmax)

        for edifici in range(2,n):
            #Anem calculant aleatoriament la resta d'edificis
            random.seed()
            newH = random.randint(1, h)
            newW = random.randint(1, w)
            newXmin = random.randint(xmin, xmax-newW)
            newXmax = newXmin + newW
            newSk.afegir(newXmin,newH,newXmax)
        return newSk


del SkylineParser









