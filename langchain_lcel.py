from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.globals import set_debug
from my_keys import GEMINI_API_KEY
from my_models import GEMINI_FLASH
from my_helper import encode_image
from detalles_imagen_modelo import detallesimagenModelo

# Desactiva logs de depuración
set_debug(False)

# Instancia el modelo LLM con las credenciales y configuración adecuadas
llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

# Codifica la imagen en base64
imagen = encode_image("datos/ejemplo_grafico.jpg")

# Template para análisis de la imagen
template_analisador = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Asume que eres un analizador de imágenes. Tu tarea es analizar la imagen
            y extraer información de forma objetiva.

            # FORMATO DE SALIDA
            Descripción de la Imagen: 'Inserta aquí tu descripción'
            Etiquetas: 'Inserta tres términos clave separados por comas'
            """
        ),
        (
            "user",
            [
                {"type": "text", "text": "Describe la imagen:"},
                {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,{imagen_informada}"}}
            ]
        )
    ]
)

# Cadena de análisis de la imagen: Template -> Modelo -> Salida en texto
cadena_analise_imagen = template_analisador | llm | StrOutputParser()

# Parser para transformar la salida final en un formato JSON validado por el modelo detallesimagenModelo
parser_json_imagen = JsonOutputParser(pydantic_object=detallesimagenModelo)

# Template para generar un resumen final, estructurando el resultado en JSON
template_respuesta = PromptTemplate(
    template=""" 
    Genera un resumen en lenguaje claro y objetivo, enfocado en el público latinoamericano.
    La comunicación debe ser simple, pensando en consultas futuras.

    # Resultado de la imagen
    {respuesta_cadena_analise_imagen}

    # FORMATO DE SALIDA
    {formato_salida}
    """,
    input_variables=["respuesta_cadena_analise_imagen"],
    partial_variables={
        "formato_salida": parser_json_imagen.get_format_instructions()
    }
)

# Cadena para resumir el resultado anterior en JSON
cadena_resumo = template_respuesta | llm | parser_json_imagen

# Combina las dos cadenas: primero análisis de la imagen, luego resumen formateado
cadena_completa = cadena_analise_imagen | cadena_resumo

# Ejecuta la cadena completa con la imagen proporcionada
respuesta = cadena_completa.invoke({"imagen_informada": imagen})

# Imprime la respuesta final estructurada en JSON
print(respuesta)