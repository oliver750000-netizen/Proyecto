import os

# Extensiones de archivo soportadas
EXTENSIONES_SOPORTADAS = [".txt", ".java", ".jav", ".class", ".jsp", ".jspx"]

# Extensiones de texto plano
EXTENSIONES_TEXTO = [".txt", ".java", ".jav", ".jsp", ".properties", ".xml", ".html", ".css", ".js", ".py"]


# Creamos la clase Archivo
class Archivo:

    # Constructor de la clase
    def __init__(self, archivo_subido):

        # Guardamos el archivo que viene desde Streamlit
        self.archivo_subido = archivo_subido

        # Guardamos el nombre del archivo
        self.nombre = archivo_subido.name

    # Metodo para obtener la extension del archivo
    def obtener_extension(self):

        # Separamos el nombre del archivo y obtenemos la extension
        return os.path.splitext(self.nombre)[1].lower()

    # Metodo para obtener el nombre sin extensión
    def obtener_nombre_base(self):

        # Obtenemos el nombre sin la extensión
        return os.path.splitext(self.nombre)[0]

    # Metodo para validar si la extensión es soportada
    def es_extension_soportada(self):

        # Verificamos si la extensión está en la lista de soportadas
        return self.obtener_extension() in EXTENSIONES_SOPORTADAS

    # Metodo para validar si es un archivo de texto
    def es_txt(self):

        # Verificamos si la extensión está en la lista de texto
        return self.obtener_extension() in EXTENSIONES_TEXTO

    # Metodo para leer el contenido del archivo
    def leer(self):

        try:
            # Leemos el archivo como bytes
            contenido_bytes = self.archivo_subido.read()

            # Intentamos decodificar como UTF-8
            contenido_texto = contenido_bytes.decode("utf-8")

            # Retornamos el texto del archivo
            return contenido_texto

        except UnicodeDecodeError:
            # Si falla UTF-8, intentamos con latin-1
            try:
                contenido_texto = contenido_bytes.decode("latin-1")
                return contenido_texto
            except:
                return "Error: No se pudo leer el archivo como texto"

    # Metodo para obtener el tipo de archivo
    def obtener_tipo(self):

        extension = self.obtener_extension()

        tipos = {
            ".txt": "Archivo de texto",
            ".java": "Código Java",
            ".jav": "Código Java",
            ".class": "Bytecode Java",
            ".jsp": "Java Server Pages",
            ".jspx": "Java Server Pages XML",
            ".properties": "Archivo de propiedades",
            ".xml": "XML",
            ".html": "HTML",
            ".css": "CSS",
            ".js": "JavaScript",
            ".py": "Python"
        }

        return tipos.get(extension, f"Tipo desconocido ({extension})")

    # Metodo para regresar informacion del archivo
    def obtener_info(self):

        # Retornamos un diccionario con informacion detallada
        return {
            "nombre": self.nombre,
            "nombre_base": self.obtener_nombre_base(),
            "extension": self.obtener_extension(),
            "tipo": self.obtener_tipo(),
            "es_soportado": self.es_extension_soportada(),
            "es_texto": self.es_txt()
        }