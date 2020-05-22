# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Skyline Telegram Bot/cl/Skyline.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\5\2#\n\2\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6")
        buf.write("\67\n\6\f\6\16\6:\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bV\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\7\bd\n\b\f\b\16\bg\13\b\3\b\2\3")
        buf.write("\16\t\2\4\6\b\n\f\16\2\3\3\2\b\t\2q\2\"\3\2\2\2\4$\3\2")
        buf.write("\2\2\6&\3\2\2\2\b*\3\2\2\2\n\62\3\2\2\2\f=\3\2\2\2\16")
        buf.write("U\3\2\2\2\20\21\5\6\4\2\21\22\7\2\2\3\22#\3\2\2\2\23\24")
        buf.write("\5\4\3\2\24\25\7\2\2\3\25#\3\2\2\2\26\27\5\n\6\2\27\30")
        buf.write("\7\2\2\3\30#\3\2\2\2\31\32\5\b\5\2\32\33\7\2\2\3\33#\3")
        buf.write("\2\2\2\34\35\5\f\7\2\35\36\7\2\2\3\36#\3\2\2\2\37 \5\16")
        buf.write("\b\2 !\7\2\2\3!#\3\2\2\2\"\20\3\2\2\2\"\23\3\2\2\2\"\26")
        buf.write("\3\2\2\2\"\31\3\2\2\2\"\34\3\2\2\2\"\37\3\2\2\2#\3\3\2")
        buf.write("\2\2$%\7\16\2\2%\5\3\2\2\2&\'\7\16\2\2\'(\7\17\2\2()\5")
        buf.write("\16\b\2)\7\3\2\2\2*+\7\3\2\2+,\5\16\b\2,-\7\22\2\2-.\5")
        buf.write("\16\b\2./\7\22\2\2/\60\5\16\b\2\60\61\7\4\2\2\61\t\3\2")
        buf.write("\2\2\62\63\7\20\2\2\638\5\b\5\2\64\65\7\22\2\2\65\67\5")
        buf.write("\b\5\2\66\64\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\2")
        buf.write("9;\3\2\2\2:8\3\2\2\2;<\7\21\2\2<\13\3\2\2\2=>\7\5\2\2")
        buf.write(">?\5\16\b\2?@\7\22\2\2@A\5\16\b\2AB\7\22\2\2BC\5\16\b")
        buf.write("\2CD\7\22\2\2DE\5\16\b\2EF\7\22\2\2FG\5\16\b\2GH\7\6\2")
        buf.write("\2H\r\3\2\2\2IJ\b\b\1\2JV\5\4\3\2KL\7\t\2\2LV\5\16\b\b")
        buf.write("MN\7\3\2\2NO\5\16\b\2OP\7\4\2\2PV\3\2\2\2QV\5\b\5\2RV")
        buf.write("\5\n\6\2SV\5\f\7\2TV\7\7\2\2UI\3\2\2\2UK\3\2\2\2UM\3\2")
        buf.write("\2\2UQ\3\2\2\2UR\3\2\2\2US\3\2\2\2UT\3\2\2\2Ve\3\2\2\2")
        buf.write("WX\f\r\2\2XY\t\2\2\2Yd\5\16\b\16Z[\f\f\2\2[\\\7\n\2\2")
        buf.write("\\d\5\16\b\r]^\f\13\2\2^_\7\13\2\2_d\5\16\b\f`a\f\n\2")
        buf.write("\2ab\7\f\2\2bd\5\16\b\ncW\3\2\2\2cZ\3\2\2\2c]\3\2\2\2")
        buf.write("c`\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\17\3\2\2\2g")
        buf.write("e\3\2\2\2\7\"8Uce")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "<INVALID>", "<INVALID>", 
                     "':='", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "MES", "MENYS", "MULT", "DIV", 
                      "POT", "WS", "WORD", "ASSIGN", "INICIL", "FIL", "SEP" ]

    RULE_root = 0
    RULE_consulta = 1
    RULE_assignacio = 2
    RULE_edifici = 3
    RULE_edificis = 4
    RULE_edificiAleatori = 5
    RULE_expr = 6

    ruleNames =  [ "root", "consulta", "assignacio", "edifici", "edificis", 
                   "edificiAleatori", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    MES=6
    MENYS=7
    MULT=8
    DIV=9
    POT=10
    WS=11
    WORD=12
    ASSIGN=13
    INICIL=14
    FIL=15
    SEP=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignacio(self):
            return self.getTypedRuleContext(SkylineParser.AssignacioContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def consulta(self):
            return self.getTypedRuleContext(SkylineParser.ConsultaContext,0)


        def edificis(self):
            return self.getTypedRuleContext(SkylineParser.EdificisContext,0)


        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def edificiAleatori(self):
            return self.getTypedRuleContext(SkylineParser.EdificiAleatoriContext,0)


        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.assignacio()
                self.state = 15
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.consulta()
                self.state = 18
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.edificis()
                self.state = 21
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.edifici()
                self.state = 24
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.edificiAleatori()
                self.state = 27
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(SkylineParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsultaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_consulta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsulta" ):
                return visitor.visitConsulta(self)
            else:
                return visitor.visitChildren(self)




    def consulta(self):

        localctx = SkylineParser.ConsultaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_consulta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(SkylineParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def ASSIGN(self):
            return self.getToken(SkylineParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assignacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)




    def assignacio(self):

        localctx = SkylineParser.AssignacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SkylineParser.WORD)
            self.state = 37
            self.match(SkylineParser.ASSIGN)
            self.state = 38
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdificiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_edifici

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdifici" ):
                return visitor.visitEdifici(self)
            else:
                return visitor.visitChildren(self)




    def edifici(self):

        localctx = SkylineParser.EdificiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(SkylineParser.T__0)
            self.state = 41
            self.expr(0)
            self.state = 42
            self.match(SkylineParser.SEP)
            self.state = 43
            self.expr(0)
            self.state = 44
            self.match(SkylineParser.SEP)
            self.state = 45
            self.expr(0)
            self.state = 46
            self.match(SkylineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdificisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIL(self):
            return self.getToken(SkylineParser.INICIL, 0)

        def edifici(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.EdificiContext)
            else:
                return self.getTypedRuleContext(SkylineParser.EdificiContext,i)


        def FIL(self):
            return self.getToken(SkylineParser.FIL, 0)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_edificis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificis" ):
                return visitor.visitEdificis(self)
            else:
                return visitor.visitChildren(self)




    def edificis(self):

        localctx = SkylineParser.EdificisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_edificis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SkylineParser.INICIL)
            self.state = 49
            self.edifici()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.SEP:
                self.state = 50
                self.match(SkylineParser.SEP)
                self.state = 51
                self.edifici()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(SkylineParser.FIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdificiAleatoriContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_edificiAleatori

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificiAleatori" ):
                return visitor.visitEdificiAleatori(self)
            else:
                return visitor.visitChildren(self)




    def edificiAleatori(self):

        localctx = SkylineParser.EdificiAleatoriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_edificiAleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SkylineParser.T__2)
            self.state = 60
            self.expr(0)
            self.state = 61
            self.match(SkylineParser.SEP)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(SkylineParser.SEP)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(SkylineParser.SEP)
            self.state = 66
            self.expr(0)
            self.state = 67
            self.match(SkylineParser.SEP)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(SkylineParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def consulta(self):
            return self.getTypedRuleContext(SkylineParser.ConsultaContext,0)


        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def edificis(self):
            return self.getTypedRuleContext(SkylineParser.EdificisContext,0)


        def edificiAleatori(self):
            return self.getTypedRuleContext(SkylineParser.EdificiAleatoriContext,0)


        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def DIV(self):
            return self.getToken(SkylineParser.DIV, 0)

        def POT(self):
            return self.getToken(SkylineParser.POT, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 72
                self.consulta()
                pass

            elif la_ == 2:
                self.state = 73
                self.match(SkylineParser.MENYS)
                self.state = 74
                self.expr(6)
                pass

            elif la_ == 3:
                self.state = 75
                self.match(SkylineParser.T__0)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 4:
                self.state = 79
                self.edifici()
                pass

            elif la_ == 5:
                self.state = 80
                self.edificis()
                pass

            elif la_ == 6:
                self.state = 81
                self.edificiAleatori()
                pass

            elif la_ == 7:
                self.state = 82
                self.match(SkylineParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.MES or _la==SkylineParser.MENYS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 89
                        self.match(SkylineParser.MULT)
                        self.state = 90
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 92
                        self.match(SkylineParser.DIV)
                        self.state = 93
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 95
                        self.match(SkylineParser.POT)
                        self.state = 96
                        self.expr(8)
                        pass

             
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




