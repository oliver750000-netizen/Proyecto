# build.ps1 - Versión Automática
# Este script busca el JAR automáticamente

# Buscar JAR en la carpeta del ejercicio (subir un nivel)
$JAR = Get-ChildItem -Path "..\antlr-*.jar" -ErrorAction SilentlyContinue | Select-Object -First 1

# Si no lo encuentra, buscar en todo el proyecto
if (-not $JAR) {
    $JAR = Get-ChildItem -Path "..\..\*" -Filter "antlr-*.jar" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
}

# Si no lo encuentra, preguntar al usuario
if (-not $JAR) {
    $ruta = Read-Host "❌ No encontré antlr-*.jar. Escribe la ruta completa del JAR"
    $JAR = Get-Item $ruta -ErrorAction SilentlyContinue
    if (-not $JAR) {
        Write-Host "❌ Ruta inválida. Saliendo..." -ForegroundColor Red
        exit 1
    }
}

Write-Host "✅ Usando JAR: $($JAR.FullName)" -ForegroundColor Green

# Limpiar
Remove-Item ExprLexer.java, ExprParser.java, ExprBaseListener.java, ExprListener.java, Expr.tokens, ExprLexer.py, ExprParser.py, ExprListener.py, ExprVisitor.py, *.class -ErrorAction SilentlyContinue

# Generar Java
java -jar $JAR.FullName Expr.g4

# Compilar Java
javac -cp $JAR.FullName Expr*.java

# Generar Python
java -jar $JAR.FullName -Dlanguage=Python3 Expr.g4

# Ejecutar Streamlit
streamlit run app.py