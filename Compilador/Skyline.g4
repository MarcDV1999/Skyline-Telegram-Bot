grammar Skyline;


// Definim la Gramatica, (REGLES)

// Per quan haguem de processar el final del fitxer
root : expr EOF ;

// Definim les expresions de suma, resta ... de nombres naturals
expr : expr MES expr
    | expr MENYS expr
    | expr MULT expr
    | expr DIV expr
    | <assoc=right> expr POT expr // La potencia te associativitat per la dreta (cal especificar-ho)
    | NUM;


// Definim Gramàtica
NUM : [0-9]+ ; // Amb el + indiquem que un NUM pot ser un o mes nombres del 0-9
MES : '+' ;
MENYS : '-';
MULT : '*';
DIV : '/';
POT : '^';
WS : [ \n]+ -> skip ; // indica a l'escàner que el token WS no ha d'arribar al parser.
WORD : ['a'-'z'];