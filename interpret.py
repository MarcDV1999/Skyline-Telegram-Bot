from antlr4 import *

# from ..gen.SkylineLexer import SkylineLexer as SkLexer
# from ..gen.SkylineParser import SkylineParser as SkParser
from cl.gen import SkylineParser as SkParser, SkylineLexer as SkLexer, SkTreeVisitor


class Interpret():
    def __init__(self):
        self.visitor = SkTreeVisitor.SkTreeVisitor()

    def executarInstruccio(self, instruccio):
        input_stream = InputStream(instruccio)
        lexer = SkLexer.SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        parser = SkParser.SkylineParser(token_stream)
        tree = parser.root()

        # A tree tenim el arbre parsejat
        # print('Tree',tree.toStringTree(recog=parser))

        # Creem un visitor, per a poder recorrer el arbre generat anteriorment
        result = self.visitor.visit(tree)
        # print(result)
        return result

    def getTaulaSimbols(self):
        return self.visitor.getTaulaSimbols()

    def setTaulaSimbols(self, dict):
        self.visitor.setTaulaSimbols(dict)

    def saveSkyline(self, id):
        self.visitor.saveSkyline(id)

    def loadSkyline(self, id):
        return self.visitor.loadSkyline(id)
