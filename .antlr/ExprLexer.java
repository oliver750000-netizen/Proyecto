// Generated from c:/Users/HP/OneDrive/Documentos/proyecto/mi-proyecto/ejercicio15/Streamlint/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SUDO=1, TCPDUMP=2, CURL=3, DIG=4, GREP=5, UFW=6, NMAP=7, SS=8, JOURNALCTL=9, 
		OPCION_SV=10, OPCION_SN=11, OPCION_TULN=12, OPCION_I=13, OPCION_CORTA=14, 
		OPCION_LARGA=15, NUM=16, IDF=17, IP=18, CIDR=19, RUTA=20, PUNTO=21, IGUAL=22, 
		WS=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SUDO", "TCPDUMP", "CURL", "DIG", "GREP", "UFW", "NMAP", "SS", "JOURNALCTL", 
			"OPCION_SV", "OPCION_SN", "OPCION_TULN", "OPCION_I", "OPCION_CORTA", 
			"OPCION_LARGA", "NUM", "IDF", "IP", "CIDR", "RUTA", "PUNTO", "IGUAL", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'sudo'", "'tcpdump'", "'curl'", "'dig'", "'grep'", "'ufw'", "'nmap'", 
			"'ss'", "'journalctl'", "'-sV'", "'-sn'", "'-tuln'", "'-I'", null, null, 
			null, null, null, null, null, "'.'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SUDO", "TCPDUMP", "CURL", "DIG", "GREP", "UFW", "NMAP", "SS", 
			"JOURNALCTL", "OPCION_SV", "OPCION_SN", "OPCION_TULN", "OPCION_I", "OPCION_CORTA", 
			"OPCION_LARGA", "NUM", "IDF", "IP", "CIDR", "RUTA", "PUNTO", "IGUAL", 
			"WS"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 17:
			IP_action((RuleContext)_localctx, actionIndex);
			break;
		case 18:
			CIDR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void IP_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			1,3
			break;
		case 1:
			1,3
			break;
		case 2:
			1,3
			break;
		case 3:
			1,3
			break;
		}
	}
	private void CIDR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			1,3
			break;
		case 5:
			1,3
			break;
		case 6:
			1,3
			break;
		case 7:
			1,3
			break;
		case 8:
			1,2
			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000\u0017\u00b5\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0004\u000ez\b\u000e\u000b"+
		"\u000e\f\u000e{\u0001\u000f\u0004\u000f\u007f\b\u000f\u000b\u000f\f\u000f"+
		"\u0080\u0001\u0010\u0001\u0010\u0005\u0010\u0085\b\u0010\n\u0010\f\u0010"+
		"\u0088\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0004\u0013\u00a7\b\u0013\u000b\u0013\f\u0013\u00a8\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0004\u0016\u00b0\b\u0016\u000b"+
		"\u0016\f\u0016\u00b1\u0001\u0016\u0001\u0016\u0000\u0000\u0017\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017\u0001\u0000"+
		"\u0006\u0002\u0000AZaz\u0001\u000009\u0003\u0000AZ__az\u0004\u000009A"+
		"Z__az\u0004\u0000.9AZ__az\u0003\u0000\t\n\r\r  \u00b9\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000"+
		"\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'"+
		"\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000"+
		"\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0001/\u0001\u0000\u0000\u0000"+
		"\u00034\u0001\u0000\u0000\u0000\u0005<\u0001\u0000\u0000\u0000\u0007A"+
		"\u0001\u0000\u0000\u0000\tE\u0001\u0000\u0000\u0000\u000bJ\u0001\u0000"+
		"\u0000\u0000\rN\u0001\u0000\u0000\u0000\u000fS\u0001\u0000\u0000\u0000"+
		"\u0011V\u0001\u0000\u0000\u0000\u0013a\u0001\u0000\u0000\u0000\u0015e"+
		"\u0001\u0000\u0000\u0000\u0017i\u0001\u0000\u0000\u0000\u0019o\u0001\u0000"+
		"\u0000\u0000\u001br\u0001\u0000\u0000\u0000\u001du\u0001\u0000\u0000\u0000"+
		"\u001f~\u0001\u0000\u0000\u0000!\u0082\u0001\u0000\u0000\u0000#\u0089"+
		"\u0001\u0000\u0000\u0000%\u0095\u0001\u0000\u0000\u0000\'\u00a4\u0001"+
		"\u0000\u0000\u0000)\u00aa\u0001\u0000\u0000\u0000+\u00ac\u0001\u0000\u0000"+
		"\u0000-\u00af\u0001\u0000\u0000\u0000/0\u0005s\u0000\u000001\u0005u\u0000"+
		"\u000012\u0005d\u0000\u000023\u0005o\u0000\u00003\u0002\u0001\u0000\u0000"+
		"\u000045\u0005t\u0000\u000056\u0005c\u0000\u000067\u0005p\u0000\u0000"+
		"78\u0005d\u0000\u000089\u0005u\u0000\u00009:\u0005m\u0000\u0000:;\u0005"+
		"p\u0000\u0000;\u0004\u0001\u0000\u0000\u0000<=\u0005c\u0000\u0000=>\u0005"+
		"u\u0000\u0000>?\u0005r\u0000\u0000?@\u0005l\u0000\u0000@\u0006\u0001\u0000"+
		"\u0000\u0000AB\u0005d\u0000\u0000BC\u0005i\u0000\u0000CD\u0005g\u0000"+
		"\u0000D\b\u0001\u0000\u0000\u0000EF\u0005g\u0000\u0000FG\u0005r\u0000"+
		"\u0000GH\u0005e\u0000\u0000HI\u0005p\u0000\u0000I\n\u0001\u0000\u0000"+
		"\u0000JK\u0005u\u0000\u0000KL\u0005f\u0000\u0000LM\u0005w\u0000\u0000"+
		"M\f\u0001\u0000\u0000\u0000NO\u0005n\u0000\u0000OP\u0005m\u0000\u0000"+
		"PQ\u0005a\u0000\u0000QR\u0005p\u0000\u0000R\u000e\u0001\u0000\u0000\u0000"+
		"ST\u0005s\u0000\u0000TU\u0005s\u0000\u0000U\u0010\u0001\u0000\u0000\u0000"+
		"VW\u0005j\u0000\u0000WX\u0005o\u0000\u0000XY\u0005u\u0000\u0000YZ\u0005"+
		"r\u0000\u0000Z[\u0005n\u0000\u0000[\\\u0005a\u0000\u0000\\]\u0005l\u0000"+
		"\u0000]^\u0005c\u0000\u0000^_\u0005t\u0000\u0000_`\u0005l\u0000\u0000"+
		"`\u0012\u0001\u0000\u0000\u0000ab\u0005-\u0000\u0000bc\u0005s\u0000\u0000"+
		"cd\u0005V\u0000\u0000d\u0014\u0001\u0000\u0000\u0000ef\u0005-\u0000\u0000"+
		"fg\u0005s\u0000\u0000gh\u0005n\u0000\u0000h\u0016\u0001\u0000\u0000\u0000"+
		"ij\u0005-\u0000\u0000jk\u0005t\u0000\u0000kl\u0005u\u0000\u0000lm\u0005"+
		"l\u0000\u0000mn\u0005n\u0000\u0000n\u0018\u0001\u0000\u0000\u0000op\u0005"+
		"-\u0000\u0000pq\u0005I\u0000\u0000q\u001a\u0001\u0000\u0000\u0000rs\u0005"+
		"-\u0000\u0000st\u0007\u0000\u0000\u0000t\u001c\u0001\u0000\u0000\u0000"+
		"uv\u0005-\u0000\u0000vw\u0005-\u0000\u0000wy\u0001\u0000\u0000\u0000x"+
		"z\u0007\u0000\u0000\u0000yx\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000"+
		"\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|\u001e\u0001"+
		"\u0000\u0000\u0000}\u007f\u0007\u0001\u0000\u0000~}\u0001\u0000\u0000"+
		"\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0001\u0000\u0000\u0000\u0081 \u0001\u0000\u0000\u0000\u0082"+
		"\u0086\u0007\u0002\u0000\u0000\u0083\u0085\u0007\u0003\u0000\u0000\u0084"+
		"\u0083\u0001\u0000\u0000\u0000\u0085\u0088\u0001\u0000\u0000\u0000\u0086"+
		"\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000\u0087"+
		"\"\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0007\u0001\u0000\u0000\u008a\u008b\u0006\u0011\u0000\u0000\u008b\u008c"+
		"\u0005.\u0000\u0000\u008c\u008d\u0007\u0001\u0000\u0000\u008d\u008e\u0006"+
		"\u0011\u0001\u0000\u008e\u008f\u0005.\u0000\u0000\u008f\u0090\u0007\u0001"+
		"\u0000\u0000\u0090\u0091\u0006\u0011\u0002\u0000\u0091\u0092\u0005.\u0000"+
		"\u0000\u0092\u0093\u0007\u0001\u0000\u0000\u0093\u0094\u0006\u0011\u0003"+
		"\u0000\u0094$\u0001\u0000\u0000\u0000\u0095\u0096\u0007\u0001\u0000\u0000"+
		"\u0096\u0097\u0006\u0012\u0004\u0000\u0097\u0098\u0005.\u0000\u0000\u0098"+
		"\u0099\u0007\u0001\u0000\u0000\u0099\u009a\u0006\u0012\u0005\u0000\u009a"+
		"\u009b\u0005.\u0000\u0000\u009b\u009c\u0007\u0001\u0000\u0000\u009c\u009d"+
		"\u0006\u0012\u0006\u0000\u009d\u009e\u0005.\u0000\u0000\u009e\u009f\u0007"+
		"\u0001\u0000\u0000\u009f\u00a0\u0006\u0012\u0007\u0000\u00a0\u00a1\u0005"+
		"/\u0000\u0000\u00a1\u00a2\u0007\u0001\u0000\u0000\u00a2\u00a3\u0006\u0012"+
		"\b\u0000\u00a3&\u0001\u0000\u0000\u0000\u00a4\u00a6\u0005/\u0000\u0000"+
		"\u00a5\u00a7\u0007\u0004\u0000\u0000\u00a6\u00a5\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9(\u0001\u0000\u0000\u0000\u00aa"+
		"\u00ab\u0005.\u0000\u0000\u00ab*\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005"+
		"=\u0000\u0000\u00ad,\u0001\u0000\u0000\u0000\u00ae\u00b0\u0007\u0005\u0000"+
		"\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00b0\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b4\u0006\u0016\t\u0000"+
		"\u00b4.\u0001\u0000\u0000\u0000\u0006\u0000{\u0080\u0086\u00a8\u00b1\n"+
		"\u0001\u0011\u0000\u0001\u0011\u0001\u0001\u0011\u0002\u0001\u0011\u0003"+
		"\u0001\u0012\u0004\u0001\u0012\u0005\u0001\u0012\u0006\u0001\u0012\u0007"+
		"\u0001\u0012\b\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}