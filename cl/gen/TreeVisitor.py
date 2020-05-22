# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Practica Pyhton i Compiladors/cl/Skyline.g4 by ANTLR 4.8
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from cl.gen.SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class TreeVisitor(SkylineVisitor):

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

        # Si només tenim un fill, hem arribat a una fulla per tant retornem el seu valor
        if (len(fills) == 1):
            print('Arribo a un numero:',fills[0])
            return int(fills[0].getText())

        # Sino, vol dir que estem en una expressió, formada per dos parametres i un simbol.
        # Tindrem algo del estil [3,+,4] per exemple
        # En aquest cas retornem el resultat de l'operació desitjada
        else:
            simbol = fills[1]
            print('Estic en una Expressio:', simbol)
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



del SkylineParser