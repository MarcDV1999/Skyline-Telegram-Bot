# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Skyline Telegram Bot/cl/Skyline.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#consulta.
    def visitConsulta(self, ctx:SkylineParser.ConsultaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assignacio.
    def visitAssignacio(self, ctx:SkylineParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edificis.
    def visitEdificis(self, ctx:SkylineParser.EdificisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edificiAleatori.
    def visitEdificiAleatori(self, ctx:SkylineParser.EdificiAleatoriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)



del SkylineParser