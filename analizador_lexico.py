# Importamos herramientas principales de ANTLR
from antlr4 import InputStream, CommonTokenStream, Token

# Importamos ErrorListener para capturar errores lexicos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el lexer y parser generados por ANTLR
from ExprLexer import ExprLexer
from ExprParser import ExprParser


# Clase para guardar errores lexicos
class ErroresLexicos(ErrorListener):

    # Constructor
    def __init__(self):

        # Lista donde guardaremos los errores
        self.lista = []

    # Metodo que ANTLR ejecuta cuando encuentra error lexico
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # Guardamos el error en la lista
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Clase para hacer el analisis lexico y sintactico
class AnalizadorLexico:

    # Constructor
    def __init__(self):

        # Variable para guardar el lexer
        self.lexer = None

        # Variable para guardar los tokens
        self.tokens = None

        # Variable para guardar el parser
        self.parser = None

        # Variable para guardar el arbol sintactico
        self.arbol = None

        # Objeto para guardar errores lexicos
        self.errores = ErroresLexicos()

        # Lista para guardar errores sintacticos
        self.errores_sintacticos = []

    # Metodo para analizar codigo
    def analizar(self, codigo):

        # ============================================
        # ANÁLISIS LÉXICO
        # ============================================
        # Convertimos el texto en entrada para ANTLR
        entrada = InputStream(codigo)

        # Creamos el lexer
        self.lexer = ExprLexer(entrada)

        # Quitamos los errores normales de ANTLR
        self.lexer.removeErrorListeners()

        # Agregamos nuestro capturador de errores
        self.lexer.addErrorListener(self.errores)

        # Creamos el flujo de tokens
        self.tokens = CommonTokenStream(self.lexer)

        # Leemos todos los tokens
        self.tokens.fill()

        # ============================================
        # ANÁLISIS SINTÁCTICO
        # ============================================
        # Reiniciamos el stream de tokens para el parser
        self.tokens.seek(0)
        
        # Creamos el parser
        self.parser = ExprParser(self.tokens)
        
        # Limpiamos errores anteriores
        self.errores_sintacticos = []
        
        try:
            # Intentamos analizar
            self.arbol = self.parser.root()
            
            # Guardamos los errores sintácticos
            if self.parser.getNumberOfSyntaxErrors() > 0:
                # ANTLR ya imprime los errores, pero los capturamos
                pass
                
        except Exception as e:
            self.errores_sintacticos.append({
                "linea": 1,
                "columna": 1,
                "mensaje": f"Error al analizar: {str(e)}"
            })
            self.arbol = None

    # Metodo para obtener tokens como lista
    def obtener_tokens(self):

        # Creamos una lista vacia
        resultado = []

        # Recorremos todos los tokens
        for token in self.tokens.tokens:

            # Saltamos EOF porque es el fin del archivo
            if token.type == Token.EOF:

                # Continuamos con el siguiente token
                continue

            # Obtenemos el nombre del token
            nombre_token = self.lexer.symbolicNames[token.type]

            # Agregamos el token a la lista
            resultado.append({
                "lexema": token.text,
                "token": nombre_token,
                "tipo": token.type,
                "linea": token.line,
                "columna": token.column
            })

        # Retornamos la lista de tokens
        return resultado

    # Metodo para obtener errores lexicos
    def obtener_errores(self):

        # Retornamos la lista de errores
        return self.errores.lista

    # ============================================
    # NUEVOS MÉTODOS PARA ANÁLISIS SINTÁCTICO
    # ============================================

    # Metodo para verificar si la sintaxis es correcta
    def sintaxis_correcta(self):
        """Retorna True si no hay errores de sintaxis"""
        if self.parser is None:
            return False
        return self.parser.getNumberOfSyntaxErrors() == 0

    # Metodo para obtener el número de errores sintácticos
    def obtener_errores_sintacticos(self):
        """Retorna la lista de errores sintácticos"""
        # ANTLR imprime errores en consola, pero podemos capturarlos
        # Por ahora retornamos el conteo
        if self.parser is None:
            return 0
        return self.parser.getNumberOfSyntaxErrors()

    # Metodo para obtener el arbol sintactico como texto
    def obtener_arbol_sintactico(self):
        """Retorna el árbol sintáctico como string"""
        if self.arbol is None:
            return "No se pudo generar el árbol sintáctico"
        try:
            return self.arbol.toStringTree(recog=self.parser)
        except Exception as e:
            return f"Error al generar el árbol: {str(e)}"

    # Metodo para obtener el estado completo del análisis
    def obtener_analisis_completo(self):
        """Retorna un diccionario con todos los resultados"""
        return {
            "tokens": self.obtener_tokens(),
            "errores_lexicos": self.obtener_errores(),
            "sintaxis_correcta": self.sintaxis_correcta(),
            "errores_sintacticos": self.obtener_errores_sintacticos(),
            "arbol_sintactico": self.obtener_arbol_sintactico()
        }