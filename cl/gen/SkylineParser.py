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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\5\2#\n\2\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\64\n\5\3\6")
        buf.write("\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bX\n\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\7\bc\n\b\f\b\16\bf\13\b\3\b\2\3\16")
        buf.write("\t\2\4\6\b\n\f\16\2\3\3\2\b\t\2o\2\"\3\2\2\2\4$\3\2\2")
        buf.write("\2\6&\3\2\2\2\b\63\3\2\2\2\n\65\3\2\2\2\f@\3\2\2\2\16")
        buf.write("W\3\2\2\2\20\21\5\6\4\2\21\22\7\2\2\3\22#\3\2\2\2\23\24")
        buf.write("\5\4\3\2\24\25\7\2\2\3\25#\3\2\2\2\26\27\5\n\6\2\27\30")
        buf.write("\7\2\2\3\30#\3\2\2\2\31\32\5\b\5\2\32\33\7\2\2\3\33#\3")
        buf.write("\2\2\2\34\35\5\f\7\2\35\36\7\2\2\3\36#\3\2\2\2\37 \5\16")
        buf.write("\b\2 !\7\2\2\3!#\3\2\2\2\"\20\3\2\2\2\"\23\3\2\2\2\"\26")
        buf.write("\3\2\2\2\"\31\3\2\2\2\"\34\3\2\2\2\"\37\3\2\2\2#\3\3\2")
        buf.write("\2\2$%\7\r\2\2%\5\3\2\2\2&\'\7\r\2\2\'(\7\16\2\2()\5\16")
        buf.write("\b\2)\7\3\2\2\2*+\7\3\2\2+,\5\16\b\2,-\7\21\2\2-.\5\16")
        buf.write("\b\2./\7\21\2\2/\60\5\16\b\2\60\61\7\4\2\2\61\64\3\2\2")
        buf.write("\2\62\64\5\4\3\2\63*\3\2\2\2\63\62\3\2\2\2\64\t\3\2\2")
        buf.write("\2\65\66\7\17\2\2\66;\5\b\5\2\678\7\21\2\28:\5\b\5\29")
        buf.write("\67\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;")
        buf.write("\3\2\2\2>?\7\20\2\2?\13\3\2\2\2@A\7\5\2\2AB\5\16\b\2B")
        buf.write("C\7\21\2\2CD\5\16\b\2DE\7\21\2\2EF\5\16\b\2FG\7\21\2\2")
        buf.write("GH\5\16\b\2HI\7\21\2\2IJ\5\16\b\2JK\7\6\2\2K\r\3\2\2\2")
        buf.write("LM\b\b\1\2MN\7\3\2\2NO\5\16\b\2OP\7\4\2\2PX\3\2\2\2QR")
        buf.write("\7\t\2\2RX\5\16\b\nSX\5\b\5\2TX\5\n\6\2UX\5\f\7\2VX\7")
        buf.write("\7\2\2WL\3\2\2\2WQ\3\2\2\2WS\3\2\2\2WT\3\2\2\2WU\3\2\2")
        buf.write("\2WV\3\2\2\2Xd\3\2\2\2YZ\f\t\2\2Z[\7\n\2\2[c\5\16\b\n")
        buf.write("\\]\f\b\2\2]^\7\13\2\2^c\5\16\b\t_`\f\7\2\2`a\t\2\2\2")
        buf.write("ac\5\16\b\bbY\3\2\2\2b\\\3\2\2\2b_\3\2\2\2cf\3\2\2\2d")
        buf.write("b\3\2\2\2de\3\2\2\2e\17\3\2\2\2fd\3\2\2\2\b\"\63;Wbd")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "<INVALID>", "<INVALID>", 
                     "':='", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "MES", "MENYS", "MULT", "DIV", 
                      "WS", "WORD", "ASSIGN", "INICIL", "FIL", "SEP" ]

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
    WS=10
    WORD=11
    ASSIGN=12
    INICIL=13
    FIL=14
    SEP=15

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

        def consulta(self):
            return self.getTypedRuleContext(SkylineParser.ConsultaContext,0)


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
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
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
                pass
            elif token in [SkylineParser.WORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.consulta()
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 51
            self.match(SkylineParser.INICIL)
            self.state = 52
            self.edifici()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.SEP:
                self.state = 53
                self.match(SkylineParser.SEP)
                self.state = 54
                self.edifici()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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
            self.state = 62
            self.match(SkylineParser.T__2)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(SkylineParser.SEP)
            self.state = 65
            self.expr(0)
            self.state = 66
            self.match(SkylineParser.SEP)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(SkylineParser.SEP)
            self.state = 69
            self.expr(0)
            self.state = 70
            self.match(SkylineParser.SEP)
            self.state = 71
            self.expr(0)
            self.state = 72
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def edificis(self):
            return self.getTypedRuleContext(SkylineParser.EdificisContext,0)


        def edificiAleatori(self):
            return self.getTypedRuleContext(SkylineParser.EdificiAleatoriContext,0)


        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def MULT(self):
            return self.getToken(SkylineParser.MULT, 0)

        def DIV(self):
            return self.getToken(SkylineParser.DIV, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

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
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 75
                self.match(SkylineParser.T__0)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                self.state = 79
                self.match(SkylineParser.MENYS)
                self.state = 80
                self.expr(8)
                pass

            elif la_ == 3:
                self.state = 81
                self.edifici()
                pass

            elif la_ == 4:
                self.state = 82
                self.edificis()
                pass

            elif la_ == 5:
                self.state = 83
                self.edificiAleatori()
                pass

            elif la_ == 6:
                self.state = 84
                self.match(SkylineParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 88
                        self.match(SkylineParser.MULT)
                        self.state = 89
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 91
                        self.match(SkylineParser.DIV)
                        self.state = 92
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 94
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.MES or _la==SkylineParser.MENYS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        self.expr(6)
                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




