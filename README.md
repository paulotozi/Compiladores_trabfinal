# Trabalho Final 
Trabalho Final da disciplina Compiladores e Interpretadores
lecionada pelo professor Valério Batista no Quadrimestre 2024.2, 
o código neste repositório foi escrito com a ferramenta Antlr e com
a linguagem Python.

## Instruções
No arquivo calculadora.g4 está contida a gramática do projeto,
no terminal do VsCode ou qualquer outra ferramenta de edição de código
 escrever <ins>antlr4 -Dlanguage=Python3 -visitor calculadora.g4</ins> ,
gerando assim os arquivos .interp, .tokens, Lexer, Listener, Parser e Visitor.
No arquivo main.py está contido o código em Python que estará utilizando
a gramática gerada pelo Antlr, utilize main.py para inicializar a calculadora.