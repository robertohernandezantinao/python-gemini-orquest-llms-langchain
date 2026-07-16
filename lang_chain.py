from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY, COHERE_API_KEY
from my_helper import encode_image
import cohere
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#llm con GEMINI_FLASH
llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)


imagen = encode_image('datos/ejemplo_grafico.jpg')

#pregunta = "Describe la imagen:"

# mensaje = HumanMessage(
#     content = [
#         {
#             "type": "text",
#             "text": pregunta
#         },
#         {
#             "type": "image_url",
#             "image_url": f"data:image/jpeg;base64,{imagen}"
#         }
#     ]
# )

template_analisis = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Asume que eres analista de imágenes. Tu principal tarea consiste en: analizar una imagen para extraer las informaciones más relevantes de manera objetiva.
            """
        ),
        (
            "user",
            [
                {
                    "type": "texto",
                    "text": "Describe la imagen:"
                },
                {
                    "type": "image_url",
                    "image_url": "data:image/jpeg;base64,{imagen_informada}"
                }
            ]
        )
    ]
)

cadena_analisis = template_analisis | llm | StrOutputParser()

respuesta_analisis = cadena_analisis.invoke({"imagen_informada": imagen})

print(respuesta_analisis)

# respuesta = llm.invoke([mensaje])
# print(respuesta)

# respuesta = llm.invoke("Cuáles canales colombianos de youtube me recomiendas para saber más sobre teléfonos inteligentes?")
# print(f"Gemini: ",respuesta.content)

#ll con Cohere
# co = cohere.ClientV2(api_key=COHERE_API_KEY)

# response = co.chat(
#     model="command-a-03-2025",
#     messages=[
#         {
#             "role": "user",
#             "content": "¿Qué canales colombianos de YouTube recomiendas sobre teléfonos inteligentes?"
#         }
#     ]
# )

# print(response.message.content[0].text)

