# Generated from calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete listener for a parse tree produced by calculadoraParser.
class calculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by calculadoraParser#AtomExpr.
    def enterAtomExpr(self, ctx:calculadoraParser.AtomExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#AtomExpr.
    def exitAtomExpr(self, ctx:calculadoraParser.AtomExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#ParenExpr.
    def enterParenExpr(self, ctx:calculadoraParser.ParenExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#ParenExpr.
    def exitParenExpr(self, ctx:calculadoraParser.ParenExprContext):
        pass


    # Enter a parse tree produced by calculadoraParser#OpExpr.
    def enterOpExpr(self, ctx:calculadoraParser.OpExprContext):
        pass

    # Exit a parse tree produced by calculadoraParser#OpExpr.
    def exitOpExpr(self, ctx:calculadoraParser.OpExprContext):
        pass



del calculadoraParser