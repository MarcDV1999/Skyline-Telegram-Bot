# Generated from /Users/marcdomenech/Desktop/UPC/Computacio/LP/Practica Pyhton i Compiladors/Compilador/Skyline.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\5\5\37\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\60\n\5\f\5\16\5\63")
        buf.write("\13\5\3\5\2\3\b\6\2\4\6\b\2\2\28\2\23\3\2\2\2\4\25\3\2")
        buf.write("\2\2\6\27\3\2\2\2\b\36\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2")
        buf.write("\3\f\24\3\2\2\2\r\16\5\6\4\2\16\17\7\2\2\3\17\24\3\2\2")
        buf.write("\2\20\21\5\b\5\2\21\22\7\2\2\3\22\24\3\2\2\2\23\n\3\2")
        buf.write("\2\2\23\r\3\2\2\2\23\20\3\2\2\2\24\3\3\2\2\2\25\26\7\n")
        buf.write("\2\2\26\5\3\2\2\2\27\30\7\n\2\2\30\31\7\13\2\2\31\32\5")
        buf.write("\b\5\2\32\7\3\2\2\2\33\34\b\5\1\2\34\37\5\4\3\2\35\37")
        buf.write("\7\3\2\2\36\33\3\2\2\2\36\35\3\2\2\2\37\61\3\2\2\2 !\f")
        buf.write("\t\2\2!\"\7\4\2\2\"\60\5\b\5\n#$\f\b\2\2$%\7\5\2\2%\60")
        buf.write("\5\b\5\t&\'\f\7\2\2\'(\7\6\2\2(\60\5\b\5\b)*\f\6\2\2*")
        buf.write("+\7\7\2\2+\60\5\b\5\7,-\f\5\2\2-.\7\b\2\2.\60\5\b\5\5")
        buf.write("/ \3\2\2\2/#\3\2\2\2/&\3\2\2\2/)\3\2\2\2/,\3\2\2\2\60")
        buf.write("\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\t\3\2\2\2\63")
        buf.write("\61\3\2\2\2\6\23\36/\61")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "<INVALID>", "<INVALID>", "':='" ]

    symbolicNames = [ "<INVALID>", "NUM", "MES", "MENYS", "MULT", "DIV", 
                      "POT", "WS", "WORD", "ASSIGN" ]

    RULE_root = 0
    RULE_consulta = 1
    RULE_assignacio = 2
    RULE_expr = 3

    ruleNames =  [ "root", "consulta", "assignacio", "expr" ]

    EOF = Token.EOF
    NUM=1
    MES=2
    MENYS=3
    MULT=4
    DIV=5
    POT=6
    WS=7
    WORD=8
    ASSIGN=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def consulta(self):
            return self.getTypedRuleContext(SkylineParser.ConsultaContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def assignacio(self):
            return self.getTypedRuleContext(SkylineParser.AssignacioContext,0)


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
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.consulta()
                self.state = 9
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.assignacio()
                self.state = 12
                self.match(SkylineParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.expr(0)
                self.state = 15
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
            self.state = 19
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
            self.state = 21
            self.match(SkylineParser.WORD)
            self.state = 22
            self.match(SkylineParser.ASSIGN)
            self.state = 23
            self.expr(0)
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


        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.WORD]:
                self.state = 26
                self.consulta()
                pass
            elif token in [SkylineParser.NUM]:
                self.state = 27
                self.match(SkylineParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 31
                        self.match(SkylineParser.MES)
                        self.state = 32
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 34
                        self.match(SkylineParser.MENYS)
                        self.state = 35
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 37
                        self.match(SkylineParser.MULT)
                        self.state = 38
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        self.match(SkylineParser.DIV)
                        self.state = 41
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        self.match(SkylineParser.POT)
                        self.state = 44
                        self.expr(3)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._predicates[3] = self.expr_sempred
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
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




