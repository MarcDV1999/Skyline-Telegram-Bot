# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Practica Pyhton i Compiladors/Compilador/Skyline.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from gen.SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkTreeVisitor(SkylineVisitor):

    taulaSimbols = {}

    # Funció que visita l'arrel del AST
    def visitRoot(self, ctx:SkylineParser.RootContext):
        # Agafem el següent fill i el visitem.
        # En cas de ser una expressio, retorna un valor, per tant el mostrem
        fill = next(ctx.getChildren())
        result = self.visit(fill)
        print(result)


    # Funció que visita l'AST on la seva arrel és una expressió
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        # Agafem tots els fills i mirem si hem arribat a una fulla o no
        fills = [n for n in ctx.getChildren()]

        # Si només tenim un fill, hem arribat a un NUM o una consulta
        if (len(fills) == 1):
            # Si es un num...
            try:
                return int(fills[0].getText())
            # Si es una consulta...
            except:
                return int(self.visit(fills[0]))

        # Sino, vol dir que estem en una expressió, formada per dos parametres i un simbol.
        # Tindrem algo del estil [3,+,4] per exemple
        # En aquest cas retornem el resultat de l'operació desitjada
        else:
            #print('Expressio', fills[0].getText(), fills[2].getText())
            simbol = fills[1]
            #print('Estic en una Expressio:', simbol)
            if (simbol == ctx.MES()):
                return self.visit(fills[0]) + self.visit(fills[2])
            if (simbol == ctx.MENYS()):
                return self.visit(fills[0]) - self.visit(fills[2])
            if (simbol == ctx.MULT()):
                return self.visit(fills[0]) * self.visit(fills[2])
            if (simbol == ctx.DIV()):
                try:
                    return self.visit(fills[0]) / self.visit(fills[2])
                except:
                    print('Error, divisió per zero')
            if (simbol == ctx.POT()):
                return self.visit(fills[0]) ** self.visit(fills[2])

    def visitAssignacio(self, ctx:SkylineParser.AssignacioContext):
        # Ara mateix si posem a : 6 (error), salta un error per segueix afegint al diccionar la variable
        # Agafem tots els fills i extraiem el valor i la variable
        #print('Visitem Assignacio')
        fills = [n for n in ctx.getChildren()]
        # El valor, l'obtindrem de evaluar l'expressió del 3r fill
        variable = fills[0].getText()
        valor = self.visit(fills[2])

        #print('Assignacio', variable,valor)
        #print('variable',variable)
        #print('valor', valor)

        try:
            #Afegim en una taula de simbols la variable i el seu valor
            self.taulaSimbols[variable] = valor
            return valor
        except:
            print('Error')


    def visitConsulta(self, ctx:SkylineParser.ConsultaContext):
        # Agafem el unic fill que té, el nom de la variable a consultar
        fills = [n for n in ctx.getChildren()]
        variable = fills[0].getText()
        #print('Consulta',variable)

        #Mirem si trobem la variable a la nostra taula de simbols, i retornem el seu valor si podem
        if variable in self.taulaSimbols:
            return self.taulaSimbols[variable]
        else:
            return 'La variable {}, no la tinc'.format(variable)




del SkylineParser









