# term.py - Para pruebas en terminal con ambos análisis
from antlr4 import InputStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser


def analizar_codigo(codigo):
    """Analiza código y muestra resultados"""
    print("\n" + "=" * 60)
    print("🔍 ANALIZANDO CÓDIGO")
    print("=" * 60)
    print("📝 Código:")
    print("-" * 40)
    print(codigo)
    print("-" * 40)
    
    # ============================================
    # ANÁLISIS LÉXICO
    # ============================================
    print("\n📝 ANÁLISIS LÉXICO:")
    print("-" * 40)
    
    lexer = ExprLexer(InputStream(codigo))
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    
    for token in tokens.tokens:
        if token.type != -1:  # Ignorar EOF
            print(f"  {token.text:15} → {ExprLexer.symbolicNames[token.type]}")
    
    print(f"\n  Total tokens: {len([t for t in tokens.tokens if t.type != -1])}")
    
    # ============================================
    # ANÁLISIS SINTÁCTICO
    # ============================================
    print("\n🌳 ANÁLISIS SINTÁCTICO:")
    print("-" * 40)
    
    # Reiniciar para el parser
    tokens.seek(0)
    parser = ExprParser(tokens)
    
    try:
        arbol = parser.root()
        errores = parser.getNumberOfSyntaxErrors()
        
        if errores == 0:
            print("✅ Sintaxis correcta")
            print("\nÁrbol sintáctico:")
            print(arbol.toStringTree(recog=parser))
        else:
            print(f"❌ {errores} errores de sintaxis")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print("\n" + "=" * 60)


# ============================================
# MENÚ PRINCIPAL
# ============================================
if __name__ == "__main__":
    print("🔍 ANALIZADOR LÉXICO Y SINTÁCTICO")
    print("=" * 60)
    print("1. Analizar código de ejemplo")
    print("2. Ingresar código manualmente")
    print("3. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        codigo_ejemplo = '''
public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
    }
}
'''
        analizar_codigo(codigo_ejemplo)
        
    elif opcion == "2":
        codigo = input("\nIngresa el código Java:\n")
        analizar_codigo(codigo)
        
    else:
        print("👋 ¡Hasta luego!")


#RODRIGUEZ BELMAN DIEGO ALBERTO 20031358
#ERICK EDUARDO HERNÁNDEZ ARIZA 20031179
#OLIVER VÁSQUEZ SANTIAGO 22031030
