import sys
from antlr4 import *

from gen import SkylineLexer as SkLexer
from gen import SkylineParser as SkParser

input_stream = InputStream(input('? '))
lexer = SkLexer.SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkParser.SkylineParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))