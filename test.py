from antlr4 import *

from cl.gen import SkylineParser as SkParser, SkylineLexer as SkLexer, SkTreeVisitor


class Interpret():
    def __init__(self):
        self.visitor = SkTreeVisitor.SkTreeVisitor()

    def executarInstruccio(self, instruccio):
        input_stream = InputStream(instruccio)
        lexer = SkLexer.SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        parser = SkParser.SkylineParser(token_stream)

        # A tree tenim el arbre parsejat
        tree = parser.root()

        # Creem un visitor, per a poder recorrer el arbre generat anteriorment
        result = self.visitor.visit(tree)
        return result

    def getTaulaSimbols(self):
        return self.visitor.getTaulaSimbols()

    def setTaulaSimbols(self, dict):
        self.visitor.setTaulaSimbols(dict)

    def saveSkyline(self, id, username):
        self.visitor.saveSkyline(id, username)

    def loadSkyline(self, id, username):
        return self.visitor.loadSkyline(id, username)
