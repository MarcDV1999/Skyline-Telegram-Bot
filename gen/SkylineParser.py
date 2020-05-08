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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("!\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\34")
        buf.write("\n\3\f\3\16\3\37\13\3\3\3\2\3\4\4\2\4\2\2\2#\2\6\3\2\2")
        buf.write("\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n")
        buf.write("\b\3\1\2\n\13\7\3\2\2\13\35\3\2\2\2\f\r\f\b\2\2\r\16\7")
        buf.write("\4\2\2\16\34\5\4\3\t\17\20\f\7\2\2\20\21\7\5\2\2\21\34")
        buf.write("\5\4\3\b\22\23\f\6\2\2\23\24\7\6\2\2\24\34\5\4\3\7\25")
        buf.write("\26\f\5\2\2\26\27\7\7\2\2\27\34\5\4\3\6\30\31\f\4\2\2")
        buf.write("\31\32\7\b\2\2\32\34\5\4\3\4\33\f\3\2\2\2\33\17\3\2\2")
        buf.write("\2\33\22\3\2\2\2\33\25\3\2\2\2\33\30\3\2\2\2\34\37\3\2")
        buf.write("\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37\35\3")
        buf.write("\2\2\2\4\33\35")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'^'" ]

    symbolicNames = [ "<INVALID>", "NUM", "MES", "MENYS", "MULT", "DIV", 
                      "POT", "WS", "WORD" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    NUM=1
    MES=2
    MENYS=3
    MULT=4
    DIV=5
    POT=6
    WS=7
    WORD=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(SkylineParser.EOF)
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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(SkylineParser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 10
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 11
                        self.match(SkylineParser.MES)
                        self.state = 12
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 13
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 14
                        self.match(SkylineParser.MENYS)
                        self.state = 15
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 17
                        self.match(SkylineParser.MULT)
                        self.state = 18
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 20
                        self.match(SkylineParser.DIV)
                        self.state = 21
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 23
                        self.match(SkylineParser.POT)
                        self.state = 24
                        self.expr(2)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




