# Importamos herramientas principales de ANTLR
from antlr4 import InputStream, CommonTokenStream, Token

# Importamos ErrorListener para capturar errores lexicos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el lexer y parser generados por ANTLR
from ExprLexer import ExprLexer
from ExprParser import ExprParser


# Clase para guardar errores lexicos
class ErroresLexicos(ErrorListener):
    def __init__(self):
        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Clase para hacer el analisis lexico y sintactico
class AnalizadorLexico:
    def __init__(self):
        self.lexer = None
        self.tokens = None
        self.parser = None
        self.arbol = None
        self.errores = ErroresLexicos()
        self.errores_sintacticos = []
        self.arbol_json = None
        self.debug_info = []  # Para depuración

    def analizar(self, codigo):
        self.debug_info = []
        
        # ANÁLISIS LÉXICO
        entrada = InputStream(codigo)
        self.lexer = ExprLexer(entrada)
        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(self.errores)
        self.tokens = CommonTokenStream(self.lexer)
        self.tokens.fill()
        
        # Verificar tokens generados
        self.debug_info.append(f"Tokens generados: {len(self.tokens.tokens)}")
        
        # ANÁLISIS SINTÁCTICO
        self.tokens.seek(0)
        self.parser = ExprParser(self.tokens)
        self.errores_sintacticos = []
        self.arbol_json = None
        
        try:
            # Intentamos analizar
            self.arbol = self.parser.compilationUnit()
            self.debug_info.append("Árbol generado correctamente")
            
            # Convertir el árbol a formato JSON
            if self.arbol is not None:
                self.arbol_json = self._arbol_a_json(self.arbol)
                self.debug_info.append("Árbol convertido a JSON")
            else:
                self.debug_info.append("El árbol es None")
                
        except Exception as e:
            error_msg = f"Error al analizar: {str(e)}"
            self.errores_sintacticos.append({
                "linea": 1,
                "columna": 1,
                "mensaje": error_msg
            })
            self.debug_info.append(f"Error: {error_msg}")
            self.arbol = None

    def _arbol_a_json(self, nodo):
        """Convierte el árbol de ANTLR a formato JSON"""
        if nodo is None:
            return None
        
        try:
            # Si es un nodo hoja (token)
            if nodo.getChildCount() == 0:
                texto = nodo.getText()
                return {
                    "tipo": type(nodo).__name__,
                    "texto": texto
                }
            
            # Si es un nodo interno
            hijos = []
            for i in range(nodo.getChildCount()):
                hijo = nodo.getChild(i)
                hijo_json = self._arbol_a_json(hijo)
                if hijo_json is not None:
                    hijos.append(hijo_json)
            
            return {
                "tipo": type(nodo).__name__,
                "hijos": hijos
            }
        except Exception as e:
            self.debug_info.append(f"Error en _arbol_a_json: {str(e)}")
            return None

    def obtener_tokens(self):
        resultado = []
        for token in self.tokens.tokens:
            if token.type == Token.EOF:
                continue
            try:
                nombre_token = self.lexer.symbolicNames[token.type]
                resultado.append({
                    "lexema": token.text,
                    "token": nombre_token,
                    "tipo": token.type,
                    "linea": token.line,
                    "columna": token.column
                })
            except:
                resultado.append({
                    "lexema": token.text,
                    "token": "DESCONOCIDO",
                    "tipo": token.type,
                    "linea": token.line,
                    "columna": token.column
                })
        return resultado

    def obtener_errores(self):
        return self.errores.lista

    def sintaxis_correcta(self):
        if self.parser is None:
            return False
        return self.parser.getNumberOfSyntaxErrors() == 0

    def obtener_errores_sintacticos(self):
        if self.parser is None:
            return 0
        return self.parser.getNumberOfSyntaxErrors()

    def obtener_arbol_sintactico(self):
        if self.arbol is None:
            return "No se pudo generar el árbol sintáctico"
        try:
            return self.arbol.toStringTree(recog=self.parser)
        except Exception as e:
            return f"Error al generar el árbol: {str(e)}"

    def obtener_arbol_json(self):
        return self.arbol_json

    def obtener_debug_info(self):
        return self.debug_info

    def obtener_analisis_completo(self):
        return {
            "tokens": self.obtener_tokens(),
            "errores_lexicos": self.obtener_errores(),
            "sintaxis_correcta": self.sintaxis_correcta(),
            "errores_sintacticos": self.obtener_errores_sintacticos(),
            "arbol_sintactico": self.obtener_arbol_sintactico(),
            "arbol_json": self.obtener_arbol_json(),
            "debug_info": self.obtener_debug_info()
        }