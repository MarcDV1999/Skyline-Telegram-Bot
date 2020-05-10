# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Practica Pyhton i Compiladors/Compilador/Skyline.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\27\n\2\r\2\16\2\30")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b&\n\b")
        buf.write("\r\b\16\b\'\3\b\3\b\3\t\6\t-\n\t\r\t\16\t.\3\n\3\n\3\n")
        buf.write("\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\5")
        buf.write("\3\2\62;\4\2\f\f\"\"\4\2C\\c|\2\65\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\26\3\2\2\2\5")
        buf.write("\32\3\2\2\2\7\34\3\2\2\2\t\36\3\2\2\2\13 \3\2\2\2\r\"")
        buf.write("\3\2\2\2\17%\3\2\2\2\21,\3\2\2\2\23\60\3\2\2\2\25\27\t")
        buf.write("\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\4\3\2\2\2\32\33\7-\2\2\33\6\3\2\2\2\34\35")
        buf.write("\7/\2\2\35\b\3\2\2\2\36\37\7,\2\2\37\n\3\2\2\2 !\7\61")
        buf.write("\2\2!\f\3\2\2\2\"#\7`\2\2#\16\3\2\2\2$&\t\3\2\2%$\3\2")
        buf.write("\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\b\b")
        buf.write("\2\2*\20\3\2\2\2+-\t\4\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2")
        buf.write("\2./\3\2\2\2/\22\3\2\2\2\60\61\7<\2\2\61\62\7?\2\2\62")
        buf.write("\24\3\2\2\2\6\2\30\'.\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    MES = 2
    MENYS = 3
    MULT = 4
    DIV = 5
    POT = 6
    WS = 7
    WORD = 8
    ASSIGN = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'^'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "MENYS", "MULT", "DIV", "POT", "WS", "WORD", "ASSIGN" ]

    ruleNames = [ "NUM", "MES", "MENYS", "MULT", "DIV", "POT", "WS", "WORD", 
                  "ASSIGN" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


