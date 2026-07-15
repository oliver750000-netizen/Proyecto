# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,217,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,5,0,0,1,8,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'System'", "'out'", "'print'", "'println'", 
                     "'main'", "'String'", "'Object'", "'Math'", "'Integer'", 
                     "'Character'", "'Thread'", "'Exception'", "'Throwable'", 
                     "'StringBuilder'", "'StringBuffer'", "'Runtime'", "'Process'", 
                     "'Class'", "'Enum'", "'abstract'", "'assert'", "'boolean'", 
                     "'break'", "'byte'", "'case'", "'catch'", "'char'", 
                     "'class'", "'const'", "'continue'", "'default'", "'do'", 
                     "'double'", "'else'", "'enum'", "'extends'", "'final'", 
                     "'finalLy'", "'float'", "'for'", "'goto'", "'if'", 
                     "'implements'", "'import'", "'instanceof'", "'int'", 
                     "'interface'", "'long'", "'native'", "'new'", "'package'", 
                     "'private'", "'protected'", "'public'", "'return'", 
                     "'short'", "'static'", "'strictfp'", "'super'", "'switch'", 
                     "'synchronized'", "'this'", "'throw'", "'throws'", 
                     "'transient'", "'try'", "'void'", "'volatile'", "'while'", 
                     "'_'", "'exports'", "'module'", "'non-sealed'", "'open'", 
                     "'opens'", "'permits'", "'provides'", "'record'", "'requires'", 
                     "'sealed'", "'to'", "'transitive'", "'uses'", "'var'", 
                     "'with'", "'yield'", "'true'", "'false'", "'null'", 
                     "'Scanner'", "'ArrayList'", "'LinkedList'", "'HashMap'", 
                     "'TreeMap'", "'HashSet'", "'TreeSet'", "'Queue'", "'Stack'", 
                     "'Deque'", "'Vector'", "'Collections'", "'Arrays'", 
                     "'Optional'", "'UUID'", "'Random'", "'Date'", "'Calendar'", 
                     "'File'", "'FileReader'", "'FileWriter'", "'BufferedReader'", 
                     "'BufferedWriter'", "'PrintWriter'", "'InputStream'", 
                     "'OutputStream'", "'IOException'", "'Connection'", 
                     "'Statement'", "'PreparedStatement'", "'ResultSet'", 
                     "'DriverManager'", "'SQLException'", "'Application'", 
                     "'Stage'", "'Scene'", "'Button'", "'Label'", "'TextField'", 
                     "'TableView'", "'Image'", "'ImageView'", "'VBox'", 
                     "'HBox'", "'GridPane'", "'BorderPane'", "'AnchorPane'", 
                     "'printf'", "'next'", "'nextInt'", "'nextDouble'", 
                     "'nextFloat'", "'nextLine'", "'nextBoolean'", "'parseInt'", 
                     "'parseDouble'", "'valueOf'", "'length'", "'charAt'", 
                     "'substring'", "'equals'", "'compareTo'", "'toString'", 
                     "'PI'", "'E'", "'err'", "'in'", "'@Override'", "'@Deprecated'", 
                     "'@SuppressWarnings'", "'@FunctionalInterface'", "'@SafeVarargs'", 
                     "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", 
                     "'|='", "'^='", "'<<='", "'>>='", "'>>>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'++'", "'--'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
                     "'!'", "'&'", "'|'", "'^'", "'~'", "'<<'", "'>>'", 
                     "'>>>'", "'?'", "':'", "'->'", "'::'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'...'", 
                     "'@'" ]

    symbolicNames = [ "<INVALID>", "SYSTEM", "OUT", "PRINT", "PRINTLN", 
                      "MAIN", "STRING", "OBJECT", "MATH", "INTEGER", "CHARACTER", 
                      "THREAD", "EXCEPTION", "THROWABLE", "STRINGBUILDER", 
                      "STRINGBUFFER", "RUNTIME", "PROCESS", "CLASS", "ENUM_CLASS", 
                      "ABST", "ASSE", "BOOL", "BREA", "BYTE", "CASE", "CATC", 
                      "CHAR", "CLAS", "CONS", "CONT", "DEFA", "DO", "DOUB", 
                      "ELSE", "ENUM", "EXTE", "FINA", "FINALY", "FLOAT", 
                      "FOR", "GOTO", "IF", "IMPL", "IMPO", "INST", "INT", 
                      "INTE", "LONG", "NATI", "NEW", "PACK", "PRIV", "PROT", 
                      "PUBL", "RETU", "SHOR", "STAT", "STRI", "SUPE", "SWIT", 
                      "SYNC", "THIS", "THRO", "THROWS", "TRAN", "TRY", "VOID", 
                      "VOLA", "WHIL", "GUIO_BAJ", "EXPO", "MODU", "NON_S", 
                      "OPEN", "OPENS", "PERM", "PROV", "RECO", "REQU", "SEAL", 
                      "TO", "TRANS", "USES", "VAR", "WITH", "YIEL", "TRUE", 
                      "FALSE", "NULL", "SCANNER", "ARRAYLIST", "LINKEDLIST", 
                      "HASHMAP", "TREEMAP", "HASHSET", "TREESET", "QUEUE", 
                      "STACK", "DEQUE", "VECTOR", "COLLECTIONS", "ARRAYS", 
                      "OPTIONAL", "UUID", "RANDOM", "DATE", "CALENDAR", 
                      "FILE", "FILEREADER", "FILEWRITER", "BUFFEREDREADER", 
                      "BUFFEREDWRITER", "PRINTWRITER", "INPUTSTREAM", "OUTPUTSTREAM", 
                      "IOEXCEPTION", "CONNECTION", "STATEMENT", "PREPAREDSTATEMENT", 
                      "RESULTSET", "DRIVERMANAGER", "SQLEXCEPTION", "APPLICATION", 
                      "STAGE", "SCENE", "BUTTON", "LABEL", "TEXTFIELD", 
                      "TABLEVIEW", "IMAGE", "IMAGEVIEW", "VBOX", "HBOX", 
                      "GRIDPANE", "BORDERPANE", "ANCHORPANE", "PRINTF", 
                      "NEXT", "NEXTINT", "NEXTDOUBLE", "NEXTFLOAT", "NEXTLINE", 
                      "NEXTBOOLEAN", "PARSEINT", "PARSEDOUBLE", "VALUEOF", 
                      "LENGTH", "CHARAT", "SUBSTRING", "EQUALS", "COMPARETO", 
                      "TOSTRING", "PI", "E", "ERR", "IN", "OVERRIDE", "DEPRECATED", 
                      "SUPPRESSWARNINGS", "FUNCTIONALINTERFACE", "SAFEVARARGS", 
                      "ASIG", "SUMA_ASIG", "RESTA_ASIG", "MULTI_ASIG", "DIVI_ASIG", 
                      "MODU_ASIG", "AND_ASIG", "OR_ASIG", "XOR_ASIG", "DESPLA_IZQ_ASIG", 
                      "DESPLA_DER_ASIG", "DESPLA_DER_SIN_SIGNO_ASIG", "MAS", 
                      "MENOS", "POR", "DIVI", "PORSE", "INCRE", "DISMI", 
                      "IGUAL_QUE", "DIFER_DE", "MENOR", "MAYOR", "MENOR_ASIG", 
                      "MAYOR_ASIG", "AND", "OR", "NOT", "AND_BIT", "OR_BIT", 
                      "XOR", "COMPLE", "DESPL_IZQ", "DESPL_DER", "DESPL_DER_SIN_SIGNO", 
                      "CONDI", "SEPAR", "LAMBDA", "REFERENCIA", "PARE_IZQ", 
                      "PARE_DER", "LLAV_IZQ", "LLAV_DER", "CORC_IZQ", "CORC_DER", 
                      "PUNTO_COMA", "COMA", "PUNTO", "VARARGS", "ANOTACION", 
                      "EXP_REGU", "NUM", "NUM_REGU", "CADENA", "REPRE_CHAR", 
                      "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    SYSTEM=1
    OUT=2
    PRINT=3
    PRINTLN=4
    MAIN=5
    STRING=6
    OBJECT=7
    MATH=8
    INTEGER=9
    CHARACTER=10
    THREAD=11
    EXCEPTION=12
    THROWABLE=13
    STRINGBUILDER=14
    STRINGBUFFER=15
    RUNTIME=16
    PROCESS=17
    CLASS=18
    ENUM_CLASS=19
    ABST=20
    ASSE=21
    BOOL=22
    BREA=23
    BYTE=24
    CASE=25
    CATC=26
    CHAR=27
    CLAS=28
    CONS=29
    CONT=30
    DEFA=31
    DO=32
    DOUB=33
    ELSE=34
    ENUM=35
    EXTE=36
    FINA=37
    FINALY=38
    FLOAT=39
    FOR=40
    GOTO=41
    IF=42
    IMPL=43
    IMPO=44
    INST=45
    INT=46
    INTE=47
    LONG=48
    NATI=49
    NEW=50
    PACK=51
    PRIV=52
    PROT=53
    PUBL=54
    RETU=55
    SHOR=56
    STAT=57
    STRI=58
    SUPE=59
    SWIT=60
    SYNC=61
    THIS=62
    THRO=63
    THROWS=64
    TRAN=65
    TRY=66
    VOID=67
    VOLA=68
    WHIL=69
    GUIO_BAJ=70
    EXPO=71
    MODU=72
    NON_S=73
    OPEN=74
    OPENS=75
    PERM=76
    PROV=77
    RECO=78
    REQU=79
    SEAL=80
    TO=81
    TRANS=82
    USES=83
    VAR=84
    WITH=85
    YIEL=86
    TRUE=87
    FALSE=88
    NULL=89
    SCANNER=90
    ARRAYLIST=91
    LINKEDLIST=92
    HASHMAP=93
    TREEMAP=94
    HASHSET=95
    TREESET=96
    QUEUE=97
    STACK=98
    DEQUE=99
    VECTOR=100
    COLLECTIONS=101
    ARRAYS=102
    OPTIONAL=103
    UUID=104
    RANDOM=105
    DATE=106
    CALENDAR=107
    FILE=108
    FILEREADER=109
    FILEWRITER=110
    BUFFEREDREADER=111
    BUFFEREDWRITER=112
    PRINTWRITER=113
    INPUTSTREAM=114
    OUTPUTSTREAM=115
    IOEXCEPTION=116
    CONNECTION=117
    STATEMENT=118
    PREPAREDSTATEMENT=119
    RESULTSET=120
    DRIVERMANAGER=121
    SQLEXCEPTION=122
    APPLICATION=123
    STAGE=124
    SCENE=125
    BUTTON=126
    LABEL=127
    TEXTFIELD=128
    TABLEVIEW=129
    IMAGE=130
    IMAGEVIEW=131
    VBOX=132
    HBOX=133
    GRIDPANE=134
    BORDERPANE=135
    ANCHORPANE=136
    PRINTF=137
    NEXT=138
    NEXTINT=139
    NEXTDOUBLE=140
    NEXTFLOAT=141
    NEXTLINE=142
    NEXTBOOLEAN=143
    PARSEINT=144
    PARSEDOUBLE=145
    VALUEOF=146
    LENGTH=147
    CHARAT=148
    SUBSTRING=149
    EQUALS=150
    COMPARETO=151
    TOSTRING=152
    PI=153
    E=154
    ERR=155
    IN=156
    OVERRIDE=157
    DEPRECATED=158
    SUPPRESSWARNINGS=159
    FUNCTIONALINTERFACE=160
    SAFEVARARGS=161
    ASIG=162
    SUMA_ASIG=163
    RESTA_ASIG=164
    MULTI_ASIG=165
    DIVI_ASIG=166
    MODU_ASIG=167
    AND_ASIG=168
    OR_ASIG=169
    XOR_ASIG=170
    DESPLA_IZQ_ASIG=171
    DESPLA_DER_ASIG=172
    DESPLA_DER_SIN_SIGNO_ASIG=173
    MAS=174
    MENOS=175
    POR=176
    DIVI=177
    PORSE=178
    INCRE=179
    DISMI=180
    IGUAL_QUE=181
    DIFER_DE=182
    MENOR=183
    MAYOR=184
    MENOR_ASIG=185
    MAYOR_ASIG=186
    AND=187
    OR=188
    NOT=189
    AND_BIT=190
    OR_BIT=191
    XOR=192
    COMPLE=193
    DESPL_IZQ=194
    DESPL_DER=195
    DESPL_DER_SIN_SIGNO=196
    CONDI=197
    SEPAR=198
    LAMBDA=199
    REFERENCIA=200
    PARE_IZQ=201
    PARE_DER=202
    LLAV_IZQ=203
    LLAV_DER=204
    CORC_IZQ=205
    CORC_DER=206
    PUNTO_COMA=207
    COMA=208
    PUNTO=209
    VARARGS=210
    ANOTACION=211
    EXP_REGU=212
    NUM=213
    NUM_REGU=214
    CADENA=215
    REPRE_CHAR=216
    WS=217

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





