# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Skyline Telegram Bot/cl/Skyline.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("K\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\6\6+\n\6\r\6\16\6,\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\6\138\n\13\r\13\16\139\3\13\3\13\3\f\6\f?")
        buf.write("\n\f\r\f\16\f@\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21\3\2\5\3\2\62;\4\2\f\f")
        buf.write("\"\"\4\2C\\c|\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2")
        buf.write("\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13*\3\2\2\2\r.\3")
        buf.write("\2\2\2\17\60\3\2\2\2\21\62\3\2\2\2\23\64\3\2\2\2\25\67")
        buf.write("\3\2\2\2\27>\3\2\2\2\31B\3\2\2\2\33E\3\2\2\2\35G\3\2\2")
        buf.write("\2\37I\3\2\2\2!\"\7*\2\2\"\4\3\2\2\2#$\7+\2\2$\6\3\2\2")
        buf.write("\2%&\7}\2\2&\b\3\2\2\2\'(\7\177\2\2(\n\3\2\2\2)+\t\2\2")
        buf.write("\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\f\3\2\2\2")
        buf.write("./\7-\2\2/\16\3\2\2\2\60\61\7/\2\2\61\20\3\2\2\2\62\63")
        buf.write("\7,\2\2\63\22\3\2\2\2\64\65\7\61\2\2\65\24\3\2\2\2\66")
        buf.write("8\t\3\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2")
        buf.write("\2:;\3\2\2\2;<\b\13\2\2<\26\3\2\2\2=?\t\4\2\2>=\3\2\2")
        buf.write("\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\30\3\2\2\2BC\7<\2\2")
        buf.write("CD\7?\2\2D\32\3\2\2\2EF\7]\2\2F\34\3\2\2\2GH\7_\2\2H\36")
        buf.write("\3\2\2\2IJ\7.\2\2J \3\2\2\2\6\2,9@\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUM = 5
    MES = 6
    MENYS = 7
    MULT = 8
    DIV = 9
    WS = 10
    WORD = 11
    ASSIGN = 12
    INICIL = 13
    FIL = 14
    SEP = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "':='", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "MENYS", "MULT", "DIV", "WS", "WORD", "ASSIGN", 
            "INICIL", "FIL", "SEP" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUM", "MES", "MENYS", 
                  "MULT", "DIV", "WS", "WORD", "ASSIGN", "INICIL", "FIL", 
                  "SEP" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


