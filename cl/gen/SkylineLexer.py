# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Skyline Telegram Bot/cl/Skyline.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\6\6-\n\6\r\6\16\6.\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f<\n\f\r\f\16\f=\3\f")
        buf.write("\3\f\3\r\6\rC\n\r\r\r\16\rD\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3")
        buf.write("\2\5\3\2\62;\4\2\f\f\"\"\4\2C\\c|\2Q\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2")
        buf.write("\2\t)\3\2\2\2\13,\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21")
        buf.write("\64\3\2\2\2\23\66\3\2\2\2\258\3\2\2\2\27;\3\2\2\2\31B")
        buf.write("\3\2\2\2\33F\3\2\2\2\35I\3\2\2\2\37K\3\2\2\2!M\3\2\2\2")
        buf.write("#$\7*\2\2$\4\3\2\2\2%&\7+\2\2&\6\3\2\2\2\'(\7}\2\2(\b")
        buf.write("\3\2\2\2)*\7\177\2\2*\n\3\2\2\2+-\t\2\2\2,+\3\2\2\2-.")
        buf.write("\3\2\2\2.,\3\2\2\2./\3\2\2\2/\f\3\2\2\2\60\61\7-\2\2\61")
        buf.write("\16\3\2\2\2\62\63\7/\2\2\63\20\3\2\2\2\64\65\7,\2\2\65")
        buf.write("\22\3\2\2\2\66\67\7\61\2\2\67\24\3\2\2\289\7`\2\29\26")
        buf.write("\3\2\2\2:<\t\3\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2")
        buf.write("\2\2>?\3\2\2\2?@\b\f\2\2@\30\3\2\2\2AC\t\4\2\2BA\3\2\2")
        buf.write("\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\32\3\2\2\2FG\7<\2\2")
        buf.write("GH\7?\2\2H\34\3\2\2\2IJ\7]\2\2J\36\3\2\2\2KL\7_\2\2L ")
        buf.write("\3\2\2\2MN\7.\2\2N\"\3\2\2\2\6\2.=D\3\b\2\2")
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
    POT = 10
    WS = 11
    WORD = 12
    ASSIGN = 13
    INICIL = 14
    FIL = 15
    SEP = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'^'", 
            "':='", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "MENYS", "MULT", "DIV", "POT", "WS", "WORD", "ASSIGN", 
            "INICIL", "FIL", "SEP" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUM", "MES", "MENYS", 
                  "MULT", "DIV", "POT", "WS", "WORD", "ASSIGN", "INICIL", 
                  "FIL", "SEP" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

