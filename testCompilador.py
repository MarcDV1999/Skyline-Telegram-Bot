import sys
from antlr4 import *

# from ..gen.SkylineLexer import SkylineLexer as SkLexer
# from ..gen.SkylineParser import SkylineParser as SkParser
from gen import SkylineParser as SkParser
from gen import SkylineLexer as SkLexer
from gen import SkTreeVisitor

class Interpret():


    def executarInstruccio(self,instruccio):
        input_stream = InputStream(instruccio)
        lexer = SkLexer.SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkParser.SkylineParser(token_stream)
        tree = parser.root()

        # A tree tenim el arbre parsejat
        # print('Tree',tree.toStringTree(recog=parser))

        # Creem un visitor, per a poder recorrer el arbre generat anteriorment
        visitor = SkTreeVisitor.SkTreeVisitor()
        result = visitor.visit(tree)
        #print(result)
        return result
