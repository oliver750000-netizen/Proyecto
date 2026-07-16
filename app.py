import streamlit as st
from analizador_lexico import AnalizadorLexico
from archivo import Archivo
import io
import json
import pandas as pd

st.set_page_config(
    page_title="Analizador Léxico y Sintáctico",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

class App:
    def __init__(self):
        self.analizador = None
        
    def ejecutar(self):
        st.markdown("""
            <style>
                .main {
                    background-color: #0e1117;
                }
                .stApp {
                    background-color: #0e1117;
                }
                h1, h2, h3, h4, h5, h6 {
                    color: #ffffff !important;
                }
                p, li, span, div {
                    color: #e0e0e0 !important;
                }
                .card {
                    background: #1a1d23;
                    border-radius: 12px;
                    padding: 1.5rem;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.4);
                    border: 1px solid #2d3138;
                    margin-bottom: 1.5rem;
                }
                .card-title {
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 1.1rem;
                    font-weight: 600;
                    color: #ffffff !important;
                    margin-bottom: 0.75rem;
                    padding-bottom: 0.5rem;
                    border-bottom: 2px solid #2d3138;
                }
                .metric-container {
                    background: #1a1d23;
                    border-radius: 10px;
                    padding: 1.25rem;
                    text-align: center;
                    border: 1px solid #2d3138;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
                    transition: all 0.2s ease;
                }
                .metric-container:hover {
                    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
                    transform: translateY(-2px);
                    border-color: #4a90e2;
                }
                .metric-value {
                    font-size: 2rem;
                    font-weight: 700;
                    color: #ffffff !important;
                }
                .metric-label {
                    font-size: 0.85rem;
                    color: #aaaaaa !important;
                    font-weight: 500;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                }
                .stButton > button {
                    background: #4a90e2;
                    color: white !important;
                    font-weight: 600;
                    border: none;
                    border-radius: 8px;
                    padding: 0.6rem 1.5rem;
                    transition: all 0.2s ease;
                    width: 100%;
                }
                .stButton > button:hover {
                    background: #357abd;
                    box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
                    transform: translateY(-1px);
                }
                .divider {
                    border: none;
                    height: 1px;
                    background: linear-gradient(to right, transparent, #2d3138, transparent);
                    margin: 2rem 0;
                }
                .footer {
                    text-align: center;
                    color: #666666 !important;
                    font-size: 0.85rem;
                    padding: 2rem 0 1rem 0;
                    border-top: 1px solid #2d3138;
                    margin-top: 2rem;
                }
                .footer p {
                    color: #666666 !important;
                }
                .stTabs [data-baseweb="tab-list"] {
                    gap: 2rem;
                    background: #1a1d23;
                    padding: 0.5rem 1rem;
                    border-radius: 10px;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
                }
                .stTabs [data-baseweb="tab"] {
                    font-weight: 500;
                    color: #aaaaaa !important;
                }
                .stTabs [data-baseweb="tab"][aria-selected="true"] {
                    color: #4a90e2 !important;
                    font-weight: 600;
                }
                .dataframe {
                    color: #e0e0e0 !important;
                }
                .dataframe thead tr th {
                    background-color: #1a1d23 !important;
                    color: #ffffff !important;
                }
                .dataframe tbody tr td {
                    background-color: #0e1117 !important;
                    color: #e0e0e0 !important;
                }
                .stFileUploader > div {
                    background-color: #1a1d23;
                    border: 1px dashed #2d3138;
                    border-radius: 8px;
                }
                .stFileUploader > div:hover {
                    border-color: #4a90e2;
                }
                .stTextArea textarea {
                    background-color: #1a1d23 !important;
                    color: #e0e0e0 !important;
                    border: 1px solid #2d3138 !important;
                    border-radius: 8px !important;
                }
                .stAlert {
                    background-color: #1a1d23 !important;
                    border: 1px solid #2d3138 !important;
                }
                .stAlert div {
                    color: #e0e0e0 !important;
                }
                [data-testid="metric-container"] {
                    background-color: #1a1d23 !important;
                    border: 1px solid #2d3138 !important;
                    border-radius: 10px !important;
                    padding: 1rem !important;
                }
                [data-testid="metric-container"] label {
                    color: #aaaaaa !important;
                }
                [data-testid="metric-container"] div {
                    color: #ffffff !important;
                }
                .stSpinner > div {
                    border-color: #4a90e2 transparent #4a90e2 transparent !important;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div style="text-align: center; padding: 1rem 0 0.5rem 0;">
                <h1 style="font-size: 2.8rem; font-weight: 700; color: #ffffff; letter-spacing: -1px; margin: 0;">
                    Analizador Lexico y Sintactico
                </h1>
                <p style="color: #aaaaaa; font-size: 1.1rem; font-weight: 300; margin-top: 0.25rem;">
                    Analisis de codigo fuente
                </p>
            </div>
        """, unsafe_allow_html=True)

        if 'codigo_analizar' not in st.session_state or not st.session_state.get('codigo_analizar'):
            st.markdown("""
            <div style="background: #1a5c7a; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4a90e2; margin-bottom: 1.5rem;">
                <h3 style="color: #ffffff; margin-top: 0;">Bienvenido al Analizador Lexico y Sintactico</h3>
                <p style="color: #e0e0e0; margin-bottom: 0.75rem;">
                    Para comenzar, puedes:
                </p>
                <ul style="color: #e0e0e0; margin-bottom: 0.75rem;">
                    <li><strong>Cargar un archivo</strong> desde la pestaña <strong>"Cargar Archivo"</strong></li>
                    <li><strong>Ingresar codigo manualmente</strong> desde la pestaña <strong>"Entrada Manual"</strong></li>
                </ul>
                <p style="color: #e0e0e0; margin-bottom: 0.75rem;">
                    El analisis mostrara:
                </p>
                <ul style="color: #e0e0e0; margin-bottom: 0.75rem;">
                    <li>Lista de tokens generados</li>
                    <li>Errores lexicos y sintacticos encontrados</li>
                    <li>Arbol sintactico</li>
                    <li>Reporte completo en formato JSON</li>
                </ul>
                <div style="background: #0e1117; border-radius: 8px; padding: 0.75rem 1rem; margin-top: 0.75rem; border: 1px solid #2d3138; font-size: 0.9rem; color: #aaaaaa;">
                    <strong style="color: #4a90e2;">Equipo de desarrollo:</strong><br>
                    RODRIGUEZ BELMAN DIEGO ALBERTO - 20031358<br>
                    ERICK EDUARDO HERNANDEZ ARIZA - 20031179<br>
                    OLIVER VASQUEZ SANTIAGO - 22031030
                </div>
            </div>
            """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Cargar Archivo", "Entrada Manual"])

        with tab1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<p class="card-title">Seleccionar archivo fuente</p>', unsafe_allow_html=True)
            
            extensiones_soportadas = ["txt", "java", "jav", "class", "jsp", "jspx", "properties", "xml", "html", "css", "js", "py"]
            
            archivo_subido = st.file_uploader(
                "Sube tu archivo",
                type=extensiones_soportadas,
                help=f"Formatos soportados: {', '.join(['.' + ext for ext in extensiones_soportadas])}"
            )
            
            if archivo_subido is not None:
                archivo = Archivo(archivo_subido)
                
                if not archivo.es_extension_soportada():
                    st.error(f"Extension no soportada: {archivo.obtener_extension()}")
                    st.info(f"Extensiones permitidas: {', '.join(['.' + ext for ext in archivo.EXTENSIONES_SOPORTADAS])}")
                else:
                    contenido = archivo.leer()
                    
                    if "Error" not in contenido:
                        info = archivo.obtener_info()
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Nombre", info['nombre'])
                        with col2:
                            st.metric("Extension", info['extension'])
                        with col3:
                            st.metric("Tipo", info['tipo'])
                        with col4:
                            lineas = len(contenido.split('\n'))
                            st.metric("Lineas", lineas)
                        
                        with st.expander("Vista previa del codigo", expanded=True):
                            lenguaje = info['extension'].replace('.', '')
                            if lenguaje in ['java', 'jav', 'class']:
                                lenguaje = 'java'
                            elif lenguaje in ['py']:
                                lenguaje = 'python'
                            elif lenguaje in ['js']:
                                lenguaje = 'javascript'
                            elif lenguaje in ['html']:
                                lenguaje = 'html'
                            elif lenguaje in ['css']:
                                lenguaje = 'css'
                            elif lenguaje in ['xml']:
                                lenguaje = 'xml'
                            elif lenguaje in ['properties']:
                                lenguaje = 'properties'
                            else:
                                lenguaje = 'text'
                            
                            st.code(contenido, language=lenguaje)
                            st.caption(f"Total: {len(contenido)} caracteres, {len(contenido.split('\n'))} lineas")
                        
                        if st.button("Analizar archivo", type="primary", use_container_width=True):
                            st.session_state['codigo_analizar'] = contenido
                            st.session_state['fuente_analisis'] = 'archivo'
                            st.rerun()
                    else:
                        st.error(contenido)
            
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<p class="card-title">Ingresar codigo manualmente</p>', unsafe_allow_html=True)
            
            codigo_manual = st.text_area(
                "Escribe o pega tu codigo:",
                height=300,
                placeholder="Ingrese su codigo fuente aqui...\n\nEjemplo:\npublic class Test {\n    public static void main(String[] args) {\n        int x = 5;\n        System.out.println(x);\n    }\n}",
                help="Puede escribir cualquier codigo para analizar",
                key="codigo_manual_textarea"
            )
            
            if st.button("Analizar codigo", type="primary", use_container_width=True):
                if codigo_manual.strip():
                    st.session_state['codigo_analizar'] = codigo_manual
                    st.session_state['fuente_analisis'] = 'manual'
                    st.rerun()
                else:
                    st.warning("Por favor, ingrese codigo para analizar")
            
            st.markdown('</div>', unsafe_allow_html=True)

        if 'codigo_analizar' in st.session_state and st.session_state.get('codigo_analizar'):
            codigo_a_analizar = st.session_state['codigo_analizar']
            
            st.markdown('<hr class="divider">', unsafe_allow_html=True)
            st.markdown('<h2 style="font-weight: 600; color: #ffffff;">Resultados del Analisis</h2>', unsafe_allow_html=True)
            
            fuente = st.session_state.get('fuente_analisis', 'desconocida')
            if fuente == 'archivo':
                st.caption(f"Analizando codigo desde archivo: {len(codigo_a_analizar)} caracteres")
            elif fuente == 'manual':
                st.caption(f"Analizando codigo ingresado manualmente: {len(codigo_a_analizar)} caracteres")
            
            try:
                self.analizador = AnalizadorLexico()
                
                with st.spinner("Analizando codigo..."):
                    self.analizador.analizar(codigo_a_analizar)
                
                tokens = self.analizador.obtener_tokens()
                errores_lexicos = self.analizador.obtener_errores()
                sintaxis_correcta = self.analizador.sintaxis_correcta()
                errores_sintacticos = self.analizador.obtener_errores_sintacticos()
                arbol_texto = self.analizador.obtener_arbol_sintactico()
                arbol_json = self.analizador.obtener_arbol_json()
                
                st.markdown("### Estadisticas del Analisis")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f"""
                        <div class="metric-container">
                            <div class="metric-value">{len(codigo_a_analizar)}</div>
                            <div class="metric-label">Caracteres</div>
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                        <div class="metric-container">
                            <div class="metric-value">{len(tokens)}</div>
                            <div class="metric-label">Tokens</div>
                        </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown(f"""
                        <div class="metric-container">
                            <div class="metric-value">{len(errores_lexicos)}</div>
                            <div class="metric-label">Errores Lexicos</div>
                        </div>
                    """, unsafe_allow_html=True)
                with col4:
                    estado = "Valido" if sintaxis_correcta else "Invalido"
                    color = "#4caf50" if sintaxis_correcta else "#ef5350"
                    st.markdown(f"""
                        <div class="metric-container">
                            <div class="metric-value" style="color: {color}; font-size: 1.5rem;">{estado}</div>
                            <div class="metric-label">Sintaxis</div>
                        </div>
                    """, unsafe_allow_html=True)
                
                tab_tokens, tab_errores, tab_arbol, tab_reporte = st.tabs([
                    "Tokens", 
                    "Errores",
                    "Arbol Sintactico",
                    "Reporte"
                ])
                
                with tab_tokens:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<p class="card-title">Tokens generados</p>', unsafe_allow_html=True)
                    
                    if tokens:
                        df_tokens = pd.DataFrame(tokens)
                        st.dataframe(df_tokens, use_container_width=True, height=400)
                        st.caption(f"Total de tokens: {len(tokens)}")
                    else:
                        st.info("No se generaron tokens")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with tab_errores:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<p class="card-title">Errores Encontrados</p>', unsafe_allow_html=True)
                    
                    if errores_lexicos:
                        st.markdown("**Errores Lexicos:**")
                        df_errores = pd.DataFrame(errores_lexicos)
                        st.dataframe(df_errores, use_container_width=True)
                    else:
                        st.success("No hay errores lexicos")
                    
                    if errores_sintacticos > 0:
                        st.markdown("**Errores Sintacticos:**")
                        st.warning(f"Se encontraron {errores_sintacticos} errores de sintaxis")
                    else:
                        st.success("No hay errores sintacticos")
                    
                    total_errores = len(errores_lexicos) + errores_sintacticos
                    if total_errores > 0:
                        st.info(f"Total de errores: {total_errores} ({len(errores_lexicos)} lexicos, {errores_sintacticos} sintacticos)")
                    else:
                        st.success("No se encontraron errores. El codigo es valido.")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with tab_arbol:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<p class="card-title">Arbol Sintactico</p>', unsafe_allow_html=True)
                    
                    if arbol_json:
                        # Mostrar árbol en formato JSON
                        with st.expander("Ver árbol en formato JSON", expanded=True):
                            st.json(arbol_json)
                        
                        # Mostrar árbol en formato texto (toStringTree de ANTLR)
                        with st.expander("Ver árbol en formato texto"):
                            st.code(arbol_texto, language="text")
                        
                        # Descargar árbol como JSON
                        arbol_json_str = json.dumps(arbol_json, indent=2, ensure_ascii=False)
                        st.download_button(
                            label="Descargar Arbol Sintactico (JSON)",
                            data=arbol_json_str,
                            file_name="arbol_sintactico.json",
                            mime="application/json",
                            use_container_width=True
                        )
                        
                        # Intentar mostrar una visualización jerárquica
                        with st.expander("Ver árbol en formato jerárquico"):
                            def mostrar_nodo(nodo, nivel=0):
                                indent = "  " * nivel
                                if 'texto' in nodo:
                                    st.text(f"{indent}├── {nodo['tipo']}: {nodo['texto']}")
                                else:
                                    st.text(f"{indent}├── {nodo['tipo']}")
                                    if 'hijos' in nodo:
                                        for hijo in nodo['hijos']:
                                            mostrar_nodo(hijo, nivel + 1)
                            
                            if arbol_json:
                                mostrar_nodo(arbol_json)
                    else:
                        st.info("No se pudo generar el árbol sintáctico. Verifica que el código sea válido.")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with tab_reporte:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<p class="card-title">Reporte Completo</p>', unsafe_allow_html=True)
                    
                    tipos_unicos = len(set(t['token'] for t in tokens)) if tokens else 0
                    
                    reporte = {
                        "analisis": {
                            "total_tokens": len(tokens),
                            "tipos_unicos": tipos_unicos,
                            "errores_lexicos": len(errores_lexicos),
                            "errores_sintacticos": errores_sintacticos,
                            "sintaxis_correcta": sintaxis_correcta
                        },
                        "estadisticas": {
                            "caracteres": len(codigo_a_analizar),
                            "lineas": len(codigo_a_analizar.split('\n'))
                        },
                        "fuente": fuente,
                        "arbol_sintactico": arbol_json if arbol_json else arbol_texto,
                        "tokens_muestra": tokens[:5] if tokens else []
                    }
                    
                    st.json(reporte)
                    
                    reporte_json = json.dumps(reporte, indent=2, ensure_ascii=False)
                    st.download_button(
                        label="Descargar Reporte (JSON)",
                        data=reporte_json,
                        file_name=f"reporte_analisis_{fuente}.json",
                        mime="application/json",
                        use_container_width=True
                    )
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<hr class="divider">', unsafe_allow_html=True)
                
                col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
                with col_btn2:
                    if st.button("Nuevo Analisis", type="secondary", use_container_width=True):
                        if 'codigo_analizar' in st.session_state:
                            del st.session_state['codigo_analizar']
                        if 'fuente_analisis' in st.session_state:
                            del st.session_state['fuente_analisis']
                        st.rerun()
                
            except Exception as e:
                st.error(f"Error durante el analisis: {str(e)}")
                st.exception(e)
                
                if st.button("Reintentar", use_container_width=True):
                    if 'codigo_analizar' in st.session_state:
                        del st.session_state['codigo_analizar']
                    st.rerun()

        st.markdown("""
            <div class="footer">
                <p>Analizador Lexico y Sintactico · Desarrollado con Streamlit</p>
                <p style="font-size: 0.75rem; color: #444444 !important; margin-top: 0.25rem;">
                    Soporte para archivos: .txt, .java, .jav, .class, .jsp, .jspx, .properties, .xml, .html, .css, .js, .py
                </p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app = App()
    app.ejecutar()