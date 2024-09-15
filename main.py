import sys
from antlr4 import *
from calculadoraLexer import calculadoraLexer
from calculadoraParser import calculadoraParser
from calculadoraVisitor import calculadoraVisitor


class CalcVisitor(calculadoraVisitor):
    def visitAtomExpr(self, ctx:calculadoraParser.AtomExprContext):
        return float(ctx.getText())

    def visitParenExpr(self, ctx:calculadoraParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx:calculadoraParser.OpExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r



def calc(line) -> float:
    input_stream = InputStream(line)

    # lexing
    lexer = calculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # parsing
    parser = calculadoraParser(stream)
    tree = parser.expr()

    # use customized visitor to traverse AST
    visitor = CalcVisitor()
    return visitor.visit(tree)



if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        print(calc(line))