// concrete syntax
grammar calculadora;

// non-terminals expressed as context-free grammar (BNF)
expr:	left=expr op=('*'|'/') right=expr  # OpExpr
    |	left=expr op=('+'|'-') right=expr  # OpExpr
    |	atom=INT                          # AtomExpr
    |	'(' expr ')'                       # ParenExpr
    ;

// tokens expressed as regular expressions
INT :   [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;
WS  :   [ \t]+ -> skip ;