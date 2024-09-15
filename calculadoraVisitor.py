# Generated from calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraParser.

class calculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraParser#AtomExpr.
    def visitAtomExpr(self, ctx:calculadoraParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#ParenExpr.
    def visitParenExpr(self, ctx:calculadoraParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#OpExpr.
    def visitOpExpr(self, ctx:calculadoraParser.OpExprContext):
        return self.visitChildren(ctx)



del calculadoraParser