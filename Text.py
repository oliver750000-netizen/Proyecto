# importa ANTL para funciones
from antlr4 import*
from ExprLexer import ExprLexer
import sys


#Lo que obtiene es la entrada, analiza el texto y lo separa
input_stream = FileStream(sys.argv[1], encoding='utf-8')



lexer = ExprLexer(input_stream)


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
