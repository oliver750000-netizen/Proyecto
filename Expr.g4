grammar Expr;

// REGLAS DEL PARSER


compilationUnit
    : packageDeclaration? importDeclaration* typeDeclaration* EOF
    ;

packageDeclaration
    : PACK qualifiedName PUNTO_COMA
    ;

importDeclaration
    : IMPO (STAT? PUNTO_COMA | qualifiedName (PUNTO POR)? PUNTO_COMA)
    ;

qualifiedName
    : Identifier (PUNTO Identifier)*
    ;

typeDeclaration
    : modifier* (classDeclaration | interfaceDeclaration | enumDeclaration) 
    | PUNTO_COMA
    ;

modifier
    : PUBL | PROT | PRIV | STAT | ABST | FINA | NATI | SYNC | TRAN | VOLA
    | annotation
    ;

classDeclaration
    : CLAS Identifier typeParameters? (EXTE typeType)? (IMPL typeList)? classBody
    ;

interfaceDeclaration
    : INTE Identifier typeParameters? (EXTE typeList)? interfaceBody
    ;

enumDeclaration
    : ENUM Identifier (IMPL typeList)? enumBody
    ;

classBody
    : LLAV_IZQ classBodyDeclaration* LLAV_DER
    ;

classBodyDeclaration
    : PUNTO_COMA
    | STAT? block
    | modifier* memberDeclaration
    ;

memberDeclaration
    : methodDeclaration
    | fieldDeclaration
    | constructorDeclaration
    | classDeclaration
    | interfaceDeclaration
    | enumDeclaration
    | voidMethodDeclaration
    ;

interfaceBody
    : LLAV_IZQ interfaceBodyDeclaration* LLAV_DER
    ;

interfaceBodyDeclaration
    : modifier* interfaceMemberDeclaration
    | PUNTO_COMA
    ;

interfaceMemberDeclaration
    : constDeclaration
    | methodHeader PUNTO_COMA
    | classDeclaration
    | interfaceDeclaration
    | enumDeclaration
    ;

enumBody
    : LLAV_IZQ enumConstants? (COMA enumConstants?)? PUNTO_COMA? enumBodyDeclarations? LLAV_DER
    ;

enumConstants
    : Identifier arguments? (COMA Identifier arguments?)*
    ;

enumBodyDeclarations
    : PUNTO_COMA classBodyDeclaration*
    ;

methodDeclaration
    : typeType Identifier formalParameters (CORC_IZQ CORC_DER)* (THROWS qualifiedNameList)? methodBody
    ;

voidMethodDeclaration
    : VOID Identifier formalParameters (CORC_IZQ CORC_DER)* (THROWS qualifiedNameList)? methodBody
    ;

methodHeader
    : typeType Identifier formalParameters (CORC_IZQ CORC_DER)* (THROWS qualifiedNameList)?
    | VOID Identifier formalParameters (CORC_IZQ CORC_DER)* (THROWS qualifiedNameList)?
    ;

constructorDeclaration
    : Identifier formalParameters (THROWS qualifiedNameList)? constructorBody
    ;

fieldDeclaration
    : typeType variableDeclarators PUNTO_COMA
    ;

constDeclaration
    : typeType variableDeclarators PUNTO_COMA
    ;

variableDeclarators
    : variableDeclarator (COMA variableDeclarator)*
    ;

variableDeclarator
    : variableDeclaratorId (ASIG variableInitializer)?
    ;

variableDeclaratorId
    : Identifier (CORC_IZQ CORC_DER)*
    ;

variableInitializer
    : expression
    | arrayInitializer
    ;

arrayInitializer
    : LLAV_IZQ (variableInitializer (COMA variableInitializer)* (COMA)?)? LLAV_DER
    ;

formalParameters
    : PARE_IZQ formalParameterList? PARE_DER
    ;

formalParameterList
    : formalParameter (COMA formalParameter)*
    ;

formalParameter
    : modifier* typeType variableDeclaratorId
    ;

typeType
    : classOrInterfaceType
    | primitiveType (CORC_IZQ CORC_DER)*
    ;

classOrInterfaceType
    : Identifier typeArguments? (PUNTO Identifier typeArguments?)*
    ;

primitiveType
    : BYTE | SHOR | INT | LONG | CHAR | FLOAT | DOUB | BOOL
    ;

typeList
    : typeType (COMA typeType)*
    ;

typeParameters
    : MENOR typeParameter (COMA typeParameter)* MAYOR
    ;

typeParameter
    : Identifier (EXTE typeBound)?
    ;

typeBound
    : typeType (AND typeType)*
    ;

typeArguments
    : MENOR typeArgument (COMA typeArgument)* MAYOR
    ;

typeArgument
    : typeType
    | CONDI
    | CONDI EXTE typeType
    | CONDI SUPE typeType
    ;

qualifiedNameList
    : qualifiedName (COMA qualifiedName)*
    ;

methodBody
    : block
    | PUNTO_COMA
    ;

constructorBody
    : block
    ;

block
    : LLAV_IZQ blockStatement* LLAV_DER
    ;

blockStatement
    : modifier* localVariableDeclaration PUNTO_COMA
    | statement
    ;

localVariableDeclaration
    : typeType variableDeclarators
    ;

statement
    : block
    | IF pareExpression statement (ELSE statement)?
    | FOR pareExpression? PUNTO_COMA expression? PUNTO_COMA expression? statement
    | forStatement
    | WHIL pareExpression statement
    | DO statement WHIL pareExpression PUNTO_COMA
    | TRY block (CATC pareExpression block)+ (FINALY block)?
    | TRY resourceSpecification block (CATC pareExpression block)+ (FINALY block)?
    | TRY resourceSpecification block (FINALY block)?
    | SWIT pareExpression switchBlock
    | SYNC pareExpression block
    | RETU expression? PUNTO_COMA
    | THRO expression PUNTO_COMA
    | BREA Identifier? PUNTO_COMA
    | CONT Identifier? PUNTO_COMA
    | ASSE expression (SEPAR expression)? PUNTO_COMA
    | PUNTO_COMA
    | statementExpression PUNTO_COMA
    | Identifier SEPAR statement
    ;

statementExpression
    : expression
    ;

forStatement
    : FOR PARE_IZQ enhancedForControl PARE_DER statement
    ;

enhancedForControl
    : modifier* typeType variableDeclaratorId SEPAR expression
    ;

switchBlock
    : LLAV_IZQ switchBlockStatementGroup* switchLabel* LLAV_DER
    ;

switchBlockStatementGroup
    : switchLabel+ blockStatement+
    ;

switchLabel
    : CASE expression SEPAR
    | DEFA SEPAR
    ;

resourceSpecification
    : PARE_IZQ resources (PUNTO_COMA resources?)? PARE_DER
    ;

resources
    : resource (PUNTO_COMA resource)*
    ;

resource
    : modifier* classOrInterfaceType variableDeclaratorId ASIG expression
    | Identifier
    ;

pareExpression
    : PARE_IZQ expression PARE_DER
    ;

expression
    : primary
    | expression PUNTO Identifier
    | expression PUNTO methodCall
    | expression PUNTO THIS
    | expression PUNTO NEW Identifier arguments
    | expression CORC_IZQ expression CORC_DER
    | expression PARE_IZQ PARE_DER
    | expression PARE_IZQ expressionList? PARE_DER
    | NEW classOrInterfaceType arguments (CORC_IZQ expression CORC_DER)* (CORC_IZQ CORC_DER)*
    | NEW classOrInterfaceType CORC_IZQ expression CORC_DER (CORC_IZQ expression CORC_DER)*
    | NEW primitiveType CORC_IZQ expression CORC_DER (CORC_IZQ expression CORC_DER)*
    | expression INCRE
    | expression DISMI
    | MAS expression
    | MENOS expression
    | INCRE expression
    | DISMI expression
    | COMPLE expression
    | NOT expression
    | expression POR expression
    | expression DIVI expression
    | expression PORSE expression
    | expression MAS expression
    | expression MENOS expression
    | expression DESPL_IZQ expression
    | expression DESPL_DER expression
    | expression DESPL_DER_SIN_SIGNO expression
    | expression MENOR expression
    | expression MAYOR expression
    | expression MENOR_ASIG expression
    | expression MAYOR_ASIG expression
    | expression INST expression
    | expression IGUAL_QUE expression
    | expression DIFER_DE expression
    | expression AND_BIT expression
    | expression XOR expression
    | expression OR_BIT expression
    | expression AND expression
    | expression OR expression
    | expression CONDI expression SEPAR expression
    | expression ASIG expression
    | expression SUMA_ASIG expression
    | expression RESTA_ASIG expression
    | expression MULTI_ASIG expression
    | expression DIVI_ASIG expression
    | expression MODU_ASIG expression
    | expression AND_ASIG expression
    | expression OR_ASIG expression
    | expression XOR_ASIG expression
    | expression DESPLA_IZQ_ASIG expression
    | expression DESPLA_DER_ASIG expression
    | expression DESPLA_DER_SIN_SIGNO_ASIG expression
    | lambdaExpression
    ;

methodCall
    : Identifier arguments
    ;

primary
    : PARE_IZQ expression PARE_DER
    | THIS
    | SUPE
    | literal
    | Identifier
    | classOrInterfaceType SUPE
    | classOrInterfaceType THIS
    | typeType PUNTO CLAS
    | VOID PUNTO CLAS
    ;

arguments
    : PARE_IZQ expressionList? PARE_DER
    ;

expressionList
    : expression (COMA expression)*
    ;

lambdaExpression
    : lambdaParameters LAMBDA expression
    | lambdaParameters LAMBDA block
    ;

lambdaParameters
    : Identifier
    | PARE_IZQ formalParameterList? PARE_DER
    | PARE_IZQ Identifier (COMA Identifier)* PARE_DER
    ;

annotation
    : ANOTACION Identifier (PARE_IZQ (elementValuePairs | elementValue)? PARE_DER)?
    ;

elementValuePairs
    : elementValuePair (COMA elementValuePair)*
    ;

elementValuePair
    : Identifier ASIG elementValue
    ;

elementValue
    : expression
    | annotation
    | elementValueArrayInitializer
    ;

elementValueArrayInitializer
    : LLAV_IZQ (elementValue (COMA elementValue)* (COMA)?)? LLAV_DER
    ;

literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | CHARACTER_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE
    | NULL
    ;

// TOKENS LEXICOS 
//Palabras reservadas y palabras clave contextuales
SYSTEM: 'System';
OUT: 'out';
PRINT: 'print';
PRINTLN: 'println';
MAIN: 'main';
STRING: 'String';
OBJECT: 'Object';
MATH: 'Math';
INTEGER: 'Integer';
CHARACTER: 'Character';
THREAD: 'Thread';
EXCEPTION: 'Exception';
THROWABLE: 'Throwable';
STRINGBUILDER: 'StringBuilder';
STRINGBUFFER: 'StringBuffer';
RUNTIME: 'Runtime';
PROCESS: 'Process';
CLASS: 'Class';
ENUM_CLASS: 'Enum';
ABST: 'abstract';
ASSE: 'assert';
BOOL: 'boolean';
BREA: 'break';
BYTE: 'byte';
CASE: 'case';
CATC: 'catch';
CHAR: 'char';
CLAS: 'class';
CONS: 'const';
CONT: 'continue';
DEFA: 'default';
DO: 'do';
DOUB: 'double';
ELSE: 'else';
ENUM: 'enum';
EXTE: 'extends';
FINA: 'final';
FINALY: 'finally';
FLOAT: 'float';
FOR: 'for';
GOTO: 'goto';
IF: 'if';
IMPL: 'implements';
IMPO: 'import';
INST: 'instanceof';
INT: 'int';
INTE: 'interface';
LONG: 'long';
NATI: 'native';
NEW: 'new';
PACK: 'package';
PRIV: 'private';
PROT: 'protected';
PUBL: 'public';
RETU: 'return';
SHOR: 'short';
STAT: 'static';
STRI: 'strictfp';
SUPE: 'super';
SWIT: 'switch';
SYNC: 'synchronized';
THIS: 'this';
THRO: 'throw';
THROWS: 'throws';
TRAN: 'transient';
TRY: 'try';
VOID: 'void';
VOLA: 'volatile';
WHIL: 'while';
GUIO_BAJ: '_';
EXPO: 'exports';
MODU: 'module';
NON_S: 'non-sealed';
OPEN: 'open';
OPENS: 'opens';
PERM: 'permits';
PROV: 'provides';
RECO: 'record';
REQU: 'requires';
SEAL: 'sealed';
TO: 'to';
TRANS: 'transitive';
USES: 'uses';
VAR: 'var';
WITH: 'with';
YIEL: 'yield';
TRUE: 'true';
FALSE: 'false';
NULL: 'null';

//IMPORTS
SCANNER: 'Scanner';
ARRAYLIST: 'ArrayList';
LINKEDLIST: 'LinkedList';
HASHMAP: 'HashMap';
TREEMAP: 'TreeMap';
HASHSET: 'HashSet';
TREESET: 'TreeSet';
QUEUE: 'Queue';
STACK: 'Stack';
DEQUE: 'Deque';
VECTOR: 'Vector';
COLLECTIONS: 'Collections';
ARRAYS: 'Arrays';
OPTIONAL: 'Optional';
UUID: 'UUID';
RANDOM: 'Random';
DATE: 'Date';
CALENDAR: 'Calendar';
FILE: 'File';
FILEREADER: 'FileReader';
FILEWRITER: 'FileWriter';
BUFFEREDREADER: 'BufferedReader';
BUFFEREDWRITER: 'BufferedWriter';
PRINTWRITER: 'PrintWriter';
INPUTSTREAM: 'InputStream';
OUTPUTSTREAM: 'OutputStream';
IOEXCEPTION: 'IOException';
CONNECTION: 'Connection';
STATEMENT: 'Statement';
PREPAREDSTATEMENT: 'PreparedStatement';
RESULTSET: 'ResultSet';
DRIVERMANAGER: 'DriverManager';
SQLEXCEPTION: 'SQLException';
APPLICATION: 'Application';
STAGE: 'Stage';
SCENE: 'Scene';
BUTTON: 'Button';
LABEL: 'Label';
TEXTFIELD: 'TextField';
TABLEVIEW: 'TableView';
IMAGE: 'Image';
IMAGEVIEW: 'ImageView';
VBOX: 'VBox';
HBOX: 'HBox';
GRIDPANE: 'GridPane';
BORDERPANE: 'BorderPane';
ANCHORPANE: 'AnchorPane';
PRINTF: 'printf';
NEXT: 'next';
NEXTINT: 'nextInt';
NEXTDOUBLE: 'nextDouble';
NEXTFLOAT: 'nextFloat';
NEXTLINE: 'nextLine';
NEXTBOOLEAN: 'nextBoolean';
PARSEINT: 'parseInt';
PARSEDOUBLE: 'parseDouble';
VALUEOF: 'valueOf';
LENGTH: 'length';
CHARAT: 'charAt';
SUBSTRING: 'substring';
EQUALS: 'equals';
COMPARETO: 'compareTo';
TOSTRING: 'toString';
PI: 'PI';
E: 'E';
ERR: 'err';
IN: 'in';
OVERRIDE: '@Override';
DEPRECATED: '@Deprecated';
SUPPRESSWARNINGS: '@SuppressWarnings';
FUNCTIONALINTERFACE: '@FunctionalInterface';
SAFEVARARGS: '@SafeVarargs';

//OPERADORES
ASIG: '=';
SUMA_ASIG: '+=';
RESTA_ASIG: '-=';
MULTI_ASIG: '*=';
DIVI_ASIG: '/=';
MODU_ASIG: '%=';
AND_ASIG: '&=';
OR_ASIG: '|=';
XOR_ASIG: '^=';
DESPLA_IZQ_ASIG: '<<=';
DESPLA_DER_ASIG: '>>=';
DESPLA_DER_SIN_SIGNO_ASIG: '>>>=';
MAS: '+';
MENOS: '-';
POR: '*';
DIVI: '/';
PORSE: '%';
INCRE: '++';
DISMI: '--';
IGUAL_QUE: '==';
DIFER_DE: '!=';
MENOR: '<';
MAYOR: '>';
MENOR_ASIG: '<=';
MAYOR_ASIG: '>=';
AND: '&&';
OR: '||';
NOT: '!';
AND_BIT: '&';
OR_BIT: '|';
XOR: '^';
COMPLE: '~';
DESPL_IZQ: '<<';
DESPL_DER: '>>';
DESPL_DER_SIN_SIGNO: '>>>';
CONDI: '?';
SEPAR: ':';
LAMBDA: '->';
REFERENCIA: '::';

//SEPARADORES
PARE_IZQ: '(';
PARE_DER: ')';
LLAV_IZQ: '{';
LLAV_DER: '}';
CORC_IZQ: '[';
CORC_DER: ']';
PUNTO_COMA: ';';
COMA: ',';
PUNTO: '.';
VARARGS: '...';
ANOTACION: '@';

//TOKENS LÉXICOS
Identifier
    : [a-zA-Z_$][a-zA-Z0-9_$]*
    ;

INTEGER_LITERAL
    : [0-9]+
    ;

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]+ [fFdD]?
    ;

CHARACTER_LITERAL
    : '\'' ( '\\' . | ~['\\\r\n] ) '\''
    ;

STRING_LITERAL
    : '"' ( '\\' . | ~["\\] )* '"'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;