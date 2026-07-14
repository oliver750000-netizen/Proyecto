// Generated from c:/Users/power/OneDrive/Documentos/Codigos/Parcial 4/Lexico/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SYSTEM=1, OUT=2, PRINT=3, PRINTLN=4, MAIN=5, STRING=6, OBJECT=7, MATH=8, 
		INTEGER=9, CHARACTER=10, THREAD=11, EXCEPTION=12, THROWABLE=13, STRINGBUILDER=14, 
		STRINGBUFFER=15, RUNTIME=16, PROCESS=17, CLASS=18, ENUM_CLASS=19, ABST=20, 
		ASSE=21, BOOL=22, BREA=23, BYTE=24, CASE=25, CATC=26, CHAR=27, CLAS=28, 
		CONS=29, CONT=30, DEFA=31, DO=32, DOUB=33, ELSE=34, ENUM=35, EXTE=36, 
		FINA=37, FINALY=38, FLOAT=39, FOR=40, GOTO=41, IF=42, IMPL=43, IMPO=44, 
		INST=45, INT=46, INTE=47, LONG=48, NATI=49, NEW=50, PACK=51, PRIV=52, 
		PROT=53, PUBL=54, RETU=55, SHOR=56, STAT=57, STRI=58, SUPE=59, SWIT=60, 
		SYNC=61, THIS=62, THRO=63, THROWS=64, TRAN=65, TRY=66, VOID=67, VOLA=68, 
		WHIL=69, GUIO_BAJ=70, EXPO=71, MODU=72, NON_S=73, OPEN=74, OPENS=75, PERM=76, 
		PROV=77, RECO=78, REQU=79, SEAL=80, TO=81, TRANS=82, USES=83, VAR=84, 
		WITH=85, YIEL=86, TRUE=87, FALSE=88, NULL=89, SCANNER=90, ARRAYLIST=91, 
		LINKEDLIST=92, HASHMAP=93, TREEMAP=94, HASHSET=95, TREESET=96, QUEUE=97, 
		STACK=98, DEQUE=99, VECTOR=100, COLLECTIONS=101, ARRAYS=102, OPTIONAL=103, 
		UUID=104, RANDOM=105, DATE=106, CALENDAR=107, FILE=108, FILEREADER=109, 
		FILEWRITER=110, BUFFEREDREADER=111, BUFFEREDWRITER=112, PRINTWRITER=113, 
		INPUTSTREAM=114, OUTPUTSTREAM=115, IOEXCEPTION=116, CONNECTION=117, STATEMENT=118, 
		PREPAREDSTATEMENT=119, RESULTSET=120, DRIVERMANAGER=121, SQLEXCEPTION=122, 
		APPLICATION=123, STAGE=124, SCENE=125, BUTTON=126, LABEL=127, TEXTFIELD=128, 
		TABLEVIEW=129, IMAGE=130, IMAGEVIEW=131, VBOX=132, HBOX=133, GRIDPANE=134, 
		BORDERPANE=135, ANCHORPANE=136, PRINTF=137, NEXT=138, NEXTINT=139, NEXTDOUBLE=140, 
		NEXTFLOAT=141, NEXTLINE=142, NEXTBOOLEAN=143, PARSEINT=144, PARSEDOUBLE=145, 
		VALUEOF=146, LENGTH=147, CHARAT=148, SUBSTRING=149, EQUALS=150, COMPARETO=151, 
		TOSTRING=152, PI=153, E=154, ERR=155, IN=156, OVERRIDE=157, DEPRECATED=158, 
		SUPPRESSWARNINGS=159, FUNCTIONALINTERFACE=160, SAFEVARARGS=161, ASIG=162, 
		SUMA_ASIG=163, RESTA_ASIG=164, MULTI_ASIG=165, DIVI_ASIG=166, MODU_ASIG=167, 
		AND_ASIG=168, OR_ASIG=169, XOR_ASIG=170, DESPLA_IZQ_ASIG=171, DESPLA_DER_ASIG=172, 
		DESPLA_DER_SIN_SIGNO_ASIG=173, MAS=174, MENOS=175, POR=176, DIVI=177, 
		PORSE=178, INCRE=179, DISMI=180, IGUAL_QUE=181, DIFER_DE=182, MENOR=183, 
		MAYOR=184, MENOR_ASIG=185, MAYOR_ASIG=186, AND=187, OR=188, NOT=189, AND_BIT=190, 
		OR_BIT=191, XOR=192, COMPLE=193, DESPL_IZQ=194, DESPL_DER=195, DESPL_DER_SIN_SIGNO=196, 
		CONDI=197, SEPAR=198, LAMBDA=199, REFERENCIA=200, PARE_IZQ=201, PARE_DER=202, 
		LLAV_IZQ=203, LLAV_DER=204, CORC_IZQ=205, CORC_DER=206, PUNTO_COMA=207, 
		COMA=208, PUNTO=209, VARARGS=210, ANOTACION=211, EXP_REGU=212, NUM=213, 
		NUM_REGU=214, CADENA=215, REPRE_CHAR=216, WS=217;
	public static final int
		RULE_root = 0, RULE_expr = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'System'", "'out'", "'print'", "'println'", "'main'", "'String'", 
			"'Object'", "'Math'", "'Integer'", "'Character'", "'Thread'", "'Exception'", 
			"'Throwable'", "'StringBuilder'", "'StringBuffer'", "'Runtime'", "'Process'", 
			"'Class'", "'Enum'", "'abstract'", "'assert'", "'boolean'", "'break'", 
			"'byte'", "'case'", "'catch'", "'char'", "'class'", "'const'", "'continue'", 
			"'default'", "'do'", "'double'", "'else'", "'enum'", "'extends'", "'final'", 
			"'finalLy'", "'float'", "'for'", "'goto'", "'if'", "'implements'", "'import'", 
			"'instanceof'", "'int'", "'interface'", "'long'", "'native'", "'new'", 
			"'package'", "'private'", "'protected'", "'public'", "'return'", "'short'", 
			"'static'", "'strictfp'", "'super'", "'switch'", "'synchronized'", "'this'", 
			"'throw'", "'throws'", "'transient'", "'try'", "'void'", "'volatile'", 
			"'while'", "'_'", "'exports'", "'module'", "'non-sealed'", "'open'", 
			"'opens'", "'permits'", "'provides'", "'record'", "'requires'", "'sealed'", 
			"'to'", "'transitive'", "'uses'", "'var'", "'with'", "'yield'", "'true'", 
			"'false'", "'null'", "'Scanner'", "'ArrayList'", "'LinkedList'", "'HashMap'", 
			"'TreeMap'", "'HashSet'", "'TreeSet'", "'Queue'", "'Stack'", "'Deque'", 
			"'Vector'", "'Collections'", "'Arrays'", "'Optional'", "'UUID'", "'Random'", 
			"'Date'", "'Calendar'", "'File'", "'FileReader'", "'FileWriter'", "'BufferedReader'", 
			"'BufferedWriter'", "'PrintWriter'", "'InputStream'", "'OutputStream'", 
			"'IOException'", "'Connection'", "'Statement'", "'PreparedStatement'", 
			"'ResultSet'", "'DriverManager'", "'SQLException'", "'Application'", 
			"'Stage'", "'Scene'", "'Button'", "'Label'", "'TextField'", "'TableView'", 
			"'Image'", "'ImageView'", "'VBox'", "'HBox'", "'GridPane'", "'BorderPane'", 
			"'AnchorPane'", "'printf'", "'next'", "'nextInt'", "'nextDouble'", "'nextFloat'", 
			"'nextLine'", "'nextBoolean'", "'parseInt'", "'parseDouble'", "'valueOf'", 
			"'length'", "'charAt'", "'substring'", "'equals'", "'compareTo'", "'toString'", 
			"'PI'", "'E'", "'err'", "'in'", "'@Override'", "'@Deprecated'", "'@SuppressWarnings'", 
			"'@FunctionalInterface'", "'@SafeVarargs'", "'='", "'+='", "'-='", "'*='", 
			"'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'>>>='", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'++'", "'--'", "'=='", "'!='", "'<'", "'>'", 
			"'<='", "'>='", "'&&'", "'||'", "'!'", "'&'", "'|'", "'^'", "'~'", "'<<'", 
			"'>>'", "'>>>'", "'?'", "':'", "'->'", "'::'", "'('", "')'", "'{'", "'}'", 
			"'['", "']'", "';'", "','", "'.'", "'...'", "'@'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SYSTEM", "OUT", "PRINT", "PRINTLN", "MAIN", "STRING", "OBJECT", 
			"MATH", "INTEGER", "CHARACTER", "THREAD", "EXCEPTION", "THROWABLE", "STRINGBUILDER", 
			"STRINGBUFFER", "RUNTIME", "PROCESS", "CLASS", "ENUM_CLASS", "ABST", 
			"ASSE", "BOOL", "BREA", "BYTE", "CASE", "CATC", "CHAR", "CLAS", "CONS", 
			"CONT", "DEFA", "DO", "DOUB", "ELSE", "ENUM", "EXTE", "FINA", "FINALY", 
			"FLOAT", "FOR", "GOTO", "IF", "IMPL", "IMPO", "INST", "INT", "INTE", 
			"LONG", "NATI", "NEW", "PACK", "PRIV", "PROT", "PUBL", "RETU", "SHOR", 
			"STAT", "STRI", "SUPE", "SWIT", "SYNC", "THIS", "THRO", "THROWS", "TRAN", 
			"TRY", "VOID", "VOLA", "WHIL", "GUIO_BAJ", "EXPO", "MODU", "NON_S", "OPEN", 
			"OPENS", "PERM", "PROV", "RECO", "REQU", "SEAL", "TO", "TRANS", "USES", 
			"VAR", "WITH", "YIEL", "TRUE", "FALSE", "NULL", "SCANNER", "ARRAYLIST", 
			"LINKEDLIST", "HASHMAP", "TREEMAP", "HASHSET", "TREESET", "QUEUE", "STACK", 
			"DEQUE", "VECTOR", "COLLECTIONS", "ARRAYS", "OPTIONAL", "UUID", "RANDOM", 
			"DATE", "CALENDAR", "FILE", "FILEREADER", "FILEWRITER", "BUFFEREDREADER", 
			"BUFFEREDWRITER", "PRINTWRITER", "INPUTSTREAM", "OUTPUTSTREAM", "IOEXCEPTION", 
			"CONNECTION", "STATEMENT", "PREPAREDSTATEMENT", "RESULTSET", "DRIVERMANAGER", 
			"SQLEXCEPTION", "APPLICATION", "STAGE", "SCENE", "BUTTON", "LABEL", "TEXTFIELD", 
			"TABLEVIEW", "IMAGE", "IMAGEVIEW", "VBOX", "HBOX", "GRIDPANE", "BORDERPANE", 
			"ANCHORPANE", "PRINTF", "NEXT", "NEXTINT", "NEXTDOUBLE", "NEXTFLOAT", 
			"NEXTLINE", "NEXTBOOLEAN", "PARSEINT", "PARSEDOUBLE", "VALUEOF", "LENGTH", 
			"CHARAT", "SUBSTRING", "EQUALS", "COMPARETO", "TOSTRING", "PI", "E", 
			"ERR", "IN", "OVERRIDE", "DEPRECATED", "SUPPRESSWARNINGS", "FUNCTIONALINTERFACE", 
			"SAFEVARARGS", "ASIG", "SUMA_ASIG", "RESTA_ASIG", "MULTI_ASIG", "DIVI_ASIG", 
			"MODU_ASIG", "AND_ASIG", "OR_ASIG", "XOR_ASIG", "DESPLA_IZQ_ASIG", "DESPLA_DER_ASIG", 
			"DESPLA_DER_SIN_SIGNO_ASIG", "MAS", "MENOS", "POR", "DIVI", "PORSE", 
			"INCRE", "DISMI", "IGUAL_QUE", "DIFER_DE", "MENOR", "MAYOR", "MENOR_ASIG", 
			"MAYOR_ASIG", "AND", "OR", "NOT", "AND_BIT", "OR_BIT", "XOR", "COMPLE", 
			"DESPL_IZQ", "DESPL_DER", "DESPL_DER_SIN_SIGNO", "CONDI", "SEPAR", "LAMBDA", 
			"REFERENCIA", "PARE_IZQ", "PARE_DER", "LLAV_IZQ", "LLAV_DER", "CORC_IZQ", 
			"CORC_DER", "PUNTO_COMA", "COMA", "PUNTO", "VARARGS", "ANOTACION", "EXP_REGU", 
			"NUM", "NUM_REGU", "CADENA", "REPRE_CHAR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(4);
			expr();
			setState(5);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u00d9\n\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0000"+
		"\u0000\u0002\u0000\u0002\u0000\u0000\u0007\u0000\u0004\u0001\u0000\u0000"+
		"\u0000\u0002\u0007\u0001\u0000\u0000\u0000\u0004\u0005\u0003\u0002\u0001"+
		"\u0000\u0005\u0006\u0005\u0000\u0000\u0001\u0006\u0001\u0001\u0000\u0000"+
		"\u0000\u0007\b\u0005\u0000\u0000\u0001\b\u0003\u0001\u0000\u0000\u0000"+
		"\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}