grammar Skyline;


// Definim la Gramatica, (REGLES)

// Per quan haguem de processar el final del fitxer
root : assignacio EOF
    | consulta EOF
    | edificis EOF
    | edifici EOF
    | edificiAleatori EOF
    | expr EOF;


// Definim la semantica que tindra una consulta
consulta : WORD;


// Definim la semantica que tindra una assignacio
assignacio : WORD ASSIGN expr;

// Definim la semantica que tindra un edifici
edifici :  '(' expr ',' expr ',' expr ')' | consulta;

// Definim la semantica que tindra un edifici
edificis : INICIL edifici (SEP edifici)* FIL;


// Definim la semantica que tindra un edifici ALeatori
edificiAleatori :  '{' expr ',' expr ',' expr ',' expr ',' expr '}';



// Definim les expresions de suma, resta ... de nombres naturals

expr :  '(' expr ')' // Mes prioritat
    | MENYS expr
    | expr MULT expr
    | expr DIV expr
    | expr (MES | MENYS) expr
    | edifici
    | edificis
    | edificiAleatori
    | NUM;





// Definim Gramàtica
NUM : [0-9]+ ; // Amb el + indiquem que un NUM pot ser un o mes nombres del 0-9
MES : '+' ;
MENYS : '-';
MULT : '*';
DIV : '/';
WS : [ \n]+ -> skip ; // indica a l'escàner que el token WS no ha d'arribar al parser.
WORD : ('a'..'z' | 'A'..'Z')+;
ASSIGN : ':=';

INICIL : '[';
FIL : ']';
SEP : ',';
