from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class ValidadorSemantico(ExprVisitor):
    def __init__(self):
        self.errores = []
        self.ambito_actual = "global"
        self.variables_ambito = {"global": {}}
        self.metodos_declarados = set()
        self.clases_declaradas = set()
        
    def visitCompilationUnit(self, ctx):
        """Visita la unidad de compilación"""
        # Primero, recolectar todas las declaraciones
        self._recolectar_declaraciones(ctx)
        # Luego validar el código
        return super().visitCompilationUnit(ctx)
    
    def _recolectar_declaraciones(self, ctx):
        """Recolecta todas las declaraciones de clases y métodos"""
        for child in ctx.children:
            if hasattr(child, 'getRuleIndex'):
                try:
                    if ExprParser.ruleNames[child.getRuleIndex()] == 'classDeclaration':
                        self._recolectar_clase(child)
                except:
                    pass
    
    def _recolectar_clase(self, ctx):
        """Recolecta información de una clase"""
        try:
            nombre_clase = ctx.Identifier().getText()
            self.clases_declaradas.add(nombre_clase)
            
            # Recolectar métodos de la clase
            if ctx.classBody():
                for decl in ctx.classBody().classBodyDeclaration():
                    if decl.memberDeclaration():
                        member = decl.memberDeclaration()
                        # Métodos con retorno
                        if member.methodDeclaration():
                            metodo = member.methodDeclaration()
                            nombre = metodo.Identifier().getText()
                            self.metodos_declarados.add(nombre)
                        # Métodos void
                        elif member.voidMethodDeclaration():
                            metodo = member.voidMethodDeclaration()
                            nombre = metodo.Identifier().getText()
                            self.metodos_declarados.add(nombre)
        except:
            pass
    
    def visitClassDeclaration(self, ctx):
        """Visita una declaración de clase"""
        try:
            nombre_clase = ctx.Identifier().getText()
            self.ambito_actual = nombre_clase
            self.variables_ambito[nombre_clase] = {}
            
            # Visitar el cuerpo de la clase
            if ctx.classBody():
                for decl in ctx.classBody().classBodyDeclaration():
                    if decl.memberDeclaration():
                        member = decl.memberDeclaration()
                        # Visitar declaraciones de campos
                        if member.fieldDeclaration():
                            self.visitFieldDeclaration(member.fieldDeclaration())
                        # Visitar métodos
                        elif member.methodDeclaration():
                            self.visitMethodDeclaration(member.methodDeclaration())
                        elif member.voidMethodDeclaration():
                            self.visitVoidMethodDeclaration(member.voidMethodDeclaration())
        except:
            pass
        
        return None
    
    def visitFieldDeclaration(self, ctx):
        """Visita una declaración de campo (variable de clase)"""
        try:
            tipo = ctx.typeType().getText()
            declaradores = ctx.variableDeclarators()
            
            for declarador in declaradores.variableDeclarator():
                nombre = declarador.variableDeclaratorId().Identifier().getText()
                self.variables_ambito[self.ambito_actual][nombre] = tipo
        except:
            pass
        
        return None
    
    def visitMethodDeclaration(self, ctx):
        """Visita una declaración de método con retorno"""
        try:
            nombre = ctx.Identifier().getText()
            
            # Crear nuevo ámbito para el método
            ambito_anterior = self.ambito_actual
            self.ambito_actual = f"{ambito_anterior}.{nombre}"
            self.variables_ambito[self.ambito_actual] = {}
            
            # Agregar parámetros como variables locales
            if ctx.formalParameters() and ctx.formalParameters().formalParameterList():
                for param in ctx.formalParameters().formalParameterList().formalParameter():
                    try:
                        tipo = param.typeType().getText()
                        nombre_param = param.variableDeclaratorId().Identifier().getText()
                        self.variables_ambito[self.ambito_actual][nombre_param] = tipo
                    except:
                        pass
            
            # Visitar el cuerpo del método
            if ctx.methodBody():
                self.visitMethodBody(ctx.methodBody())
            
            self.ambito_actual = ambito_anterior
        except:
            pass
        
        return None
    
    def visitVoidMethodDeclaration(self, ctx):
        """Visita una declaración de método void"""
        try:
            nombre = ctx.Identifier().getText()
            
            # Crear nuevo ámbito para el método
            ambito_anterior = self.ambito_actual
            self.ambito_actual = f"{ambito_anterior}.{nombre}"
            self.variables_ambito[self.ambito_actual] = {}
            
            # Agregar parámetros como variables locales
            if ctx.formalParameters() and ctx.formalParameters().formalParameterList():
                for param in ctx.formalParameters().formalParameterList().formalParameter():
                    try:
                        tipo = param.typeType().getText()
                        nombre_param = param.variableDeclaratorId().Identifier().getText()
                        self.variables_ambito[self.ambito_actual][nombre_param] = tipo
                    except:
                        pass
            
            # Visitar el cuerpo del método
            if ctx.methodBody():
                self.visitMethodBody(ctx.methodBody())
            
            self.ambito_actual = ambito_anterior
        except:
            pass
        
        return None
    
    def visitMethodBody(self, ctx):
        """Visita el cuerpo de un método"""
        if ctx.block():
            self.visitBlock(ctx.block())
        return None
    
    def visitBlock(self, ctx):
        """Visita un bloque de código"""
        try:
            for statement in ctx.blockStatement():
                if statement.localVariableDeclaration():
                    self.visitLocalVariableDeclaration(statement.localVariableDeclaration())
                elif statement.statement():
                    self.visit(statement.statement())
        except:
            pass
        return None
    
    def visitLocalVariableDeclaration(self, ctx):
        """Visita una declaración de variable local"""
        try:
            tipo = ctx.typeType().getText()
            for declarador in ctx.variableDeclarators().variableDeclarator():
                nombre = declarador.variableDeclaratorId().Identifier().getText()
                self.variables_ambito[self.ambito_actual][nombre] = tipo
                
                # Verificar inicialización
                if declarador.variableInitializer():
                    self.visit(declarador.variableInitializer())
        except:
            pass
        return None
    
    def visitExpression(self, ctx):
        """Visita una expresión y verifica tipos"""
        try:
            # Verificar asignaciones
            if ctx.ASIG():
                # Asignación: izquierda = derecha
                if len(ctx.expression()) >= 2:
                    izquierda = ctx.expression(0)
                    
                    # Verificar que la variable de la izquierda esté declarada
                    if hasattr(izquierda, 'Identifier') and izquierda.Identifier():
                        nombre_var = izquierda.Identifier().getText()
                        if not self._variable_declarada(nombre_var):
                            linea = ctx.start.line
                            self.errores.append({
                                'linea': linea,
                                'mensaje': f"Variable '{nombre_var}' no declarada",
                                'gravedad': 'error'
                            })
            
            # Verificar uso de variables
            if hasattr(ctx, 'Identifier') and ctx.Identifier():
                nombre = ctx.Identifier().getText()
                # Si no es una palabra clave, verificar que esté declarada
                if nombre not in ['true', 'false', 'null', 'this', 'super']:
                    if not self._variable_declarada(nombre) and nombre not in self.metodos_declarados and nombre not in self.clases_declaradas:
                        if nombre not in ['System', 'out', 'println', 'print', 'String', 'Integer', 'Math']:
                            linea = ctx.start.line
                            self.errores.append({
                                'linea': linea,
                                'mensaje': f"Variable o método '{nombre}' no declarado",
                                'gravedad': 'error'
                            })
            
            # Verificar llamadas a métodos
            if hasattr(ctx, 'methodCall') and ctx.methodCall():
                nombre_metodo = ctx.methodCall().Identifier().getText()
                if nombre_metodo not in self.metodos_declarados and nombre_metodo not in ['println', 'print', 'length', 'charAt', 'substring', 'equals', 'toString']:
                    linea = ctx.start.line
                    self.errores.append({
                        'linea': linea,
                        'mensaje': f"Método '{nombre_metodo}' no declarado",
                        'gravedad': 'error'
                    })
        except:
            pass
        
        # Visitar hijos
        try:
            for child in ctx.getChildren():
                if child is not ctx:
                    self.visit(child)
        except:
            pass
        
        return None
    
    def visitStatement(self, ctx):
        """Visita una sentencia"""
        # Visitar hijos
        try:
            for child in ctx.getChildren():
                if child is not ctx:
                    self.visit(child)
        except:
            pass
        
        return None
    
    def _variable_declarada(self, nombre):
        """Verifica si una variable está declarada en el ámbito actual o superiores"""
        # Buscar en el ámbito actual
        if nombre in self.variables_ambito.get(self.ambito_actual, {}):
            return True
        
        # Buscar en ámbito global (clase)
        if '.' in self.ambito_actual:
            clase = self.ambito_actual.split('.')[0]
            if nombre in self.variables_ambito.get(clase, {}):
                return True
        
        # Buscar en ámbito global raíz
        if nombre in self.variables_ambito.get("global", {}):
            return True
        
        return False
    
    def obtener_errores(self):
        """Devuelve la lista de errores semánticos"""
        return self.errores
    
    def es_valido(self):
        """Indica si el código es semánticamente válido"""
        return len(self.errores) == 0