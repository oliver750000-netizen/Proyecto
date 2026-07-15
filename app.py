import streamlit as st
from archivo import Archivo
from analizador_lexico import AnalizadorLexico


class App:

    def __init__(self):
        st.set_page_config(page_title="Analizador Léxico y Sintáctico", layout="wide")
        self.analizador = AnalizadorLexico()

    def ejecutar(self):
        st.title("🔍 Analizador Léxico y Sintáctico con ANTLR")
        st.markdown("""
        <div style="background: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <p style="margin: 0;">
                📤 Sube un archivo con código Java para analizar su estructura 
                <strong>léxica</strong> (tokens) y <strong>sintáctica</strong> (árbol de análisis).
            </p>
            <p style="margin: 5px 0 0 0; font-size: 14px; color: #666;">
                Extensiones soportadas: .txt, .java, .jav, .jsp
            </p>
        </div>
        """, unsafe_allow_html=True)

        # ============================================
        # SIDEBAR - EJEMPLOS (MANTENER IGUAL)
        # ============================================
        with st.sidebar:
            st.header("📋 Ejemplos de Código")
            st.markdown("Haz clic para cargar un ejemplo:")

            ejemplos = {
                "Hola Mundo": '''
public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
    }
}
''',
                "Variables y Operadores": '''
public class Operadores {
    public static void main(String[] args) {
        int x = 10;
        int y = 5;
        int suma = x + y;
        int resta = x - y;
        int multi = x * y;
        int div = x / y;
        boolean mayor = x > y;
        boolean igual = x == y;
    }
}
''',
                "Estructuras de Control": '''
public class Control {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                System.out.println("Par: " + i);
            }
        }
        
        String[] nombres = {"Ana", "Carlos"};
        for (String nombre : nombres) {
            System.out.println(nombre);
        }
    }
}
''',
                "Con Errores": '''
public class ConErrores {
    public static void main(String[] args) {
        int x = 
        System.out.println("Error de sintaxis");
    }
}
'''
            }

            for nombre, codigo in ejemplos.items():
                if st.button(f"📄 {nombre}", key=f"ejemplo_{nombre}", use_container_width=True):
                    import io
                    archivo_simulado = io.BytesIO(codigo.encode('utf-8'))
                    archivo_simulado.name = f"ejemplo_{nombre}.java"
                    st.session_state['archivo_ejemplo'] = archivo_simulado
                    st.rerun()

            st.divider()
            st.markdown("**ℹ️ Información:**")
            st.caption("📊 El análisis muestra los tokens y el árbol sintáctico del código.")

        # ============================================
        # SUBIR ARCHIVO (MANTENER IGUAL)
        # ============================================
        if 'archivo_ejemplo' in st.session_state:
            archivo_subido = st.session_state['archivo_ejemplo']
            st.success(f"✅ Ejemplo cargado: {archivo_subido.name}")
            
            if st.button("🗑️ Limpiar ejemplo"):
                del st.session_state['archivo_ejemplo']
                st.rerun()
        else:
            archivo_subido = st.file_uploader(
                "📤 Sube tu archivo",
                type=["txt", "java", "jav", "jsp"],
                help="Formatos soportados: .txt, .java, .jav, .jsp"
            )

        if archivo_subido is None:
            st.info("ℹ️ Sube un archivo o selecciona un ejemplo del sidebar")
            return

        # ============================================
        # PROCESAR ARCHIVO (MANTENER IGUAL)
        # ============================================
        archivo = Archivo(archivo_subido)

        if not archivo.es_extension_soportada():
            st.error(f"❌ Extensión no soportada: {archivo.obtener_extension()}")
            st.info(f"Extensiones permitidas: {', '.join(['.' + ext for ext in archivo.EXTENSIONES_SOPORTADAS])}")
            return

        codigo = archivo.leer()
        info = archivo.obtener_info()

        with st.expander("📁 Información del archivo", expanded=False):
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Nombre", info["nombre"])
            col2.metric("Extensión", info["extension"])
            col3.metric("Tipo", info["tipo"])
            col4.metric("Líneas", len(codigo.split('\n')))

        st.subheader("📝 Código fuente")
        st.code(codigo, language="java")

        # ============================================
        # BOTÓN ANALIZAR (MANTENER IGUAL)
        # ============================================
        col_btn1, col_btn2 = st.columns([1, 5])
        with col_btn1:
            if st.button("🔍 Analizar", type="primary", use_container_width=True):
                st.session_state.analizar = True

        if not st.session_state.get('analizar', False):
            st.info("Presiona 'Analizar' para iniciar el análisis")
            return

        # ============================================
        # EJECUTAR ANÁLISIS (AQUÍ ESTÁ EL CAMBIO)
        # ============================================
        with st.spinner("🔍 Analizando código..."):
            self.analizador.analizar(codigo)  # Esto ya hace ambos análisis

        # ============================================
        # MOSTRAR RESULTADOS (AQUÍ ESTÁN LOS CAMBIOS)
        # ============================================
        st.markdown("---")
        st.header("📊 Resultados del Análisis")

        # ============================================
        # ESTADÍSTICAS (AGREGADO: errores sintácticos)
        # ============================================
        tokens = self.analizador.obtener_tokens()
        errores_lexicos = self.analizador.obtener_errores()
        sintaxis_correcta = self.analizador.sintaxis_correcta()  # NUEVO
        errores_sintacticos = self.analizador.obtener_errores_sintacticos()  # NUEVO
        arbol = self.analizador.obtener_arbol_sintactico()  # NUEVO

        col1, col2, col3, col4 = st.columns(4)  # AHORA 4 COLUMNAS
        col1.metric("📝 Tokens", len(tokens))
        col2.metric("❌ Errores Léxicos", len(errores_lexicos))
        col3.metric("🔍 Errores Sintácticos", errores_sintacticos)  # NUEVO
        col4.metric("✅ Estado", "Válido" if sintaxis_correcta else "Inválido")  # NUEVO

        # ============================================
        # PESTAÑAS (AHORA CON SINTÁCTICO)
        # ============================================
        tab1, tab2, tab3, tab4 = st.tabs([
            "📝 Tokens", 
            "🌳 Árbol Sintáctico",  # NUEVA
            "⚠️ Errores",
            "📋 Reporte"
        ])

        # ============================================
        # TAB 1: TOKENS (IGUAL)
        # ============================================
        with tab1:
            st.subheader("📝 Lista de Tokens")

            if len(tokens) == 0:
                st.warning("No se encontraron tokens en el código")
            else:
                import pandas as pd
                df_tokens = pd.DataFrame(tokens)
                st.dataframe(df_tokens, use_container_width=True, height=400)

                st.caption("🔤 Vista visual de tokens:")
                tokens_html = " ".join([
                    f'<span style="background: #e2e8f0; padding: 4px 10px; border-radius: 5px; margin: 3px; display: inline-block; font-family: monospace; font-size: 12px;">'
                    f'<span style="color: #4a5568; font-weight: 600;">{t["token"]}</span> '
                    f'<span style="color: #e53e3e;">{repr(t["lexema"])}</span>'
                    f'</span>'
                    for t in tokens[:50]
                ])
                st.markdown(f'<div style="background: #f7fafc; padding: 15px; border-radius: 8px;">{tokens_html}</div>', unsafe_allow_html=True)

                if len(tokens) > 50:
                    st.caption(f"... y {len(tokens) - 50} tokens más")

        # ============================================
        # TAB 2: ÁRBOL SINTÁCTICO (NUEVA)
        # ============================================
        with tab2:
            st.subheader("🌳 Árbol Sintáctico")

            if sintaxis_correcta:
                st.success("✅ El código es sintácticamente correcto")
            else:
                st.error(f"❌ El código tiene {errores_sintacticos} errores de sintaxis")

            st.markdown("**Estructura del análisis:**")
            st.code(arbol, language="text", line_numbers=True)

        # ============================================
        # TAB 3: ERRORES (IGUAL PERO CON SINTÁCTICOS)
        # ============================================
        with tab3:
            st.subheader("⚠️ Errores Encontrados")

            # Errores léxicos
            if errores_lexicos:
                st.markdown("**Errores Léxicos:**")
                import pandas as pd
                df_errores = pd.DataFrame(errores_lexicos)
                st.dataframe(df_errores, use_container_width=True)
            else:
                st.success("✅ No hay errores léxicos")

            # Errores sintácticos (NUEVO)
            if errores_sintacticos > 0:
                st.markdown("**Errores Sintácticos:**")
                st.warning(f"Se encontraron {errores_sintacticos} errores de sintaxis")
                st.caption("Revisa el árbol sintáctico en la pestaña anterior para más detalles")
            else:
                st.success("✅ No hay errores sintácticos")

        # ============================================
        # TAB 4: REPORTE (IGUAL PERO CON SINTÁCTICO)
        # ============================================
        with tab4:
            st.subheader("📋 Reporte Completo del Análisis")

            st.markdown("### 📊 Resumen Ejecutivo")

            col_r1, col_r2, col_r3 = st.columns(3)
            with col_r1:
                st.metric("Tokens", len(tokens))
            with col_r2:
                tipos_unicos = len(set(t['token'] for t in tokens))
                st.metric("Tipos de Tokens", tipos_unicos)
            with col_r3:
                st.metric("Errores Totales", len(errores_lexicos) + errores_sintacticos)

            st.markdown("### 📝 Detalles Completos")
            reporte = {
                "archivo": info,
                "analisis": {
                    "total_tokens": len(tokens),
                    "tipos_unicos": tipos_unicos,
                    "errores_lexicos": len(errores_lexicos),
                    "errores_sintacticos": errores_sintacticos,
                    "sintaxis_correcta": sintaxis_correcta
                },
                "primeros_tokens": tokens[:10] if len(tokens) > 10 else tokens
            }
            st.json(reporte)

            import json
            reporte_json = json.dumps(reporte, indent=2, ensure_ascii=False)
            st.download_button(
                label="📥 Descargar Reporte (JSON)",
                data=reporte_json,
                file_name=f"reporte_{info['nombre_base']}.json",
                mime="application/json",
                use_container_width=True
            )

        # ============================================
        # BOTÓN RESET (IGUAL)
        # ============================================
        st.markdown("---")
        if st.button("🔄 Nuevo Análisis", use_container_width=True):
            st.session_state.analizar = False
            if 'archivo_ejemplo' in st.session_state:
                del st.session_state['archivo_ejemplo']
            st.rerun()


if __name__ == "__main__":
    app = App()
    app.ejecutar()