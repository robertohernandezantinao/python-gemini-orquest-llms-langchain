from langchain.tools import BaseTool
import cohere
from langchain.prompts import PromptTemplate
from my_keys import COHERE_API_KEY
import ast


class HerramientaExplicar(BaseTool):

    name: str = "HerramientaExplicar"

    description: str = """
Utiliza esta herramienta siempre que sea solicitada la explicación
de un contenido a las personas.

# ENTRADA REQUERIDA
- 'tema' (str)
"""

    return_direct: bool = True

    def _run(self, accion):

        accion = ast.literal_eval(accion)

        tema_parametro = accion.get("tema", "")

        co = cohere.ClientV2(
            api_key=COHERE_API_KEY
        )

        template_respuesta = PromptTemplate(
            template="""
Asume el papel de un profesor con aspectos de didáctica.

1. Explica el tema {tema}.
2. Utiliza ejemplos sencillos.
3. Si es posible utiliza ejemplos colombianos.
4. Si escribes código utiliza Python.

Tema:
{tema}
""",
            input_variables=["tema"]
        )

        prompt = template_respuesta.format(
            tema=tema_parametro
        )

        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content[0].text