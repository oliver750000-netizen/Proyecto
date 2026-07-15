# importa ANTL para funciones
from antlr4 import*
from ExprLexer import ExprLexer


#Lo que obtiene es la entrada, analiza el texto y lo separa
lexer = ExprLexer(InputStream(input("? ")))


tokens = CommonTokenStream(lexer)
tokens.fill()


for token in tokens.tokens:
    print(f"Texto   : {token.text}")
    print("Tipo    : " + ExprLexer.symbolicNames[token.type])
    print(f"Línea   : {token.line}")
    print(f"Columna : {token.column}")
    print("---------------------------")


#RODRIGUEZ BELMAN DIEGO ALBERTO 20031358
#ERICK EDUARDO HERNÁNDEZ ARIZA 20031179
#OLIVER VÁSQUEZ SANTIAGO 22031030
