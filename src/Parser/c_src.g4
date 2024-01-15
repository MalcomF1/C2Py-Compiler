grammar c_src;

// antlr4 -Dlanguage=Python3 c_src.g4 -visitor

prog : (include)* (initSentence | defSentence)*;

//-------------语法规则----------------------------------------------
include : '#include' '<' libName '>';

// 初始化
initSentence : (normalInit | arrayInit | structInit);

defSentence : (funcDef | structDef);

//结构体
structDef : structItem '{' structParams '}' ';';

structParams : (sParam)+;

//结构体中参数
sParam : (typeName | structItem) (varName | arrayName) (',' (varName | arrayName))* ';';

//函数
funcDef : (typeName | voidType | structItem) varName '(' params ')' '{' funcBody '}';

//函数参数
params : param (',' param)* | ;
param : typeName varName;

//函数体
funcBody : mainBody returnSentence;

//语句块/函数块
mainBody : (block | func ';')*;

//语句块
block : initSentence | assignSentence | forBlock | whileBlock | ifBlocks | returnSentence;

//初始化语句
normalInit : (typeName) varName ('=' expression)? (',' varName ('=' expression)?)* ';';
arrayInit : typeName varName '[' intType ']'';';
structInit : structItem (varName | arrayName) ';';

//赋值语句
// assignSentence : ((arrayItem | varName | structMember) '=')+ expression ';';
assignSentence : ((arrayItem | varName | structMember) '=') expression ';';

//for 语句
forBlock : 'for' '(' firstBlock ';' condition ';' secondBlock ')' ('{' mainBody '}' | ';');
firstBlock : varName '=' expression (',' firstBlock)? | ;
secondBlock : varName '=' expression (',' secondBlock)? | ;

//if 语句
ifBlocks : ifBlock (elifBlock)* (elseBlock)?;
ifBlock : 'if' '(' condition ')' '{' mainBody '}';
elifBlock : 'else' 'if' '(' condition ')' '{' mainBody '}';
elseBlock : 'else' '{' mainBody '}';

condition : expression;

//while 语句
whileBlock : 'while' '(' condition ')' '{' mainBody '}';

//return 语句
// returnSentence : 'return' (intType | varName)? ';';
returnSentence : 'return' (expression)? ';';

expression
    : '(' expression ')'               #parens
    | op='!' expression                   #Neg
    | expression op=('*' | '/' | '%') expression   #MulDiv
    | expression op=('+' | '-') expression   #AddSub
    | expression op=('==' | '!=' | '<' | '<=' | '>' | '>=') expression #Judge
    | expression Logical expression             # AND
    | (op='-')? intType             #int
    | (op='-')? doubleType          #double
    | charType                       #char
    | stringType                     #string
    | arrayItem                  #arrayitem
    | structMember               #structmember
    | varName                         #identifier
    | func                       #function
    ;


structItem : 'struct' varName;

arrayName : varName '[' intType ']';

structMember : (varName | arrayItem) '.' (varName | arrayItem);

voidType : 'void';

typeName
    : 'string'
    | 'int'
    | 'char'
    | 'double'
    ;

arrayItem : varName '[' expression ']';



//函数
func : (scanfFunc | getsFunc | atoiFunc | printfFunc | strlenFunc | selfDefinedFunc) ;

//scanf
// scanfFunc : 'scanf' '(' stringType (',' '&' ? (varName | arrayItem | structMember))* ')';
scanfFunc : 'scanf' '(' stringType (',' '&' ? (varName | arrayItem | structMember)) ')';

//gets
getsFunc : 'gets' '(' varName ')';

//atoi
atoiFunc : 'atoi' '(' expression ')';

//printf
printfFunc : 'printf' '(' (stringType | varName) (',' expression)* ')';

//Selfdefined
//selfDefinedFunc : varName '(' ((argument | varName) (',' (argument | varName))*)? ')';
selfDefinedFunc : varName '(' ((expression) (',' (expression))*)? ')';

//strlen
strlenFunc : 'strlen' '(' varName ')';


//argument : intType | doubleType | charType | stringType;

//varName
varName : VAR;

//intType
intType : INT;

//doubleType
doubleType : DOUBLE;

//charType
charType : CHAR;

//stringType
stringType : STRING;

//libName
libName : LIB;

//-------------词法规则----------------------------------------------
VAR : [a-zA-Z_][0-9A-Za-z_]*;

INT : [0-9]+;

DOUBLE : [0-9]+'.'[0-9]+;

CHAR : '\'' . '\'' ;

STRING : '"' .*? '"';

LIB : [a-zA-Z]+ '.h' ?;

Logical : '&&' | '||';


Operator : '/' | '!=' | '*' | '>' | '>=' | '==' | '<' | '+' | '-' | '<=' | '!' ;

LineComment : '//' .*? '\r'? '\n' -> skip;

BlockComment : '/*' .*? '*/' -> skip;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

