# COMPATIBILIDAD

## Adaptación del proyecto a las bibliotecas modernas

**Última actualización:** Julio de 2026
> **Nota**
>
> Este documento no forma parte del material original del curso.
> Fue elaborado durante la actualización del proyecto para mantener su compatibilidad con las versiones modernas de Gemini, Cohere y LangChain disponibles en julio de 2026.
> Roberto Hernández A.
---

# Introducción

Este repositorio corresponde al curso:

> **Gemini y Python: orquestando LLMs con LangChain**

El contenido original fue desarrollado utilizando versiones de LangChain, Gemini y Cohere que, al momento de esta actualización (julio de 2026), presentan incompatibilidades o han sido reemplazadas por versiones más recientes.

El objetivo de este documento es registrar todas las modificaciones necesarias para ejecutar correctamente el proyecto utilizando las bibliotecas modernas.

Todas las soluciones descritas aquí fueron implementadas y verificadas durante el desarrollo del curso.

---

# Estado del proyecto

Estado general:

✅ Completamente funcional

Se verificó correctamente el funcionamiento de:

- generación de texto
- análisis de imágenes
- PromptTemplate
- ChatPromptTemplate
- StrOutputParser
- JsonOutputParser
- BaseTool
- AgentExecutor
- create_react_agent
- herramientas personalizadas
- integración con Gemini
- integración con Cohere

---

# Entorno utilizado

Las pruebas fueron realizadas utilizando:

| Componente | Versión |
|------------|----------|
| Sistema operativo | Windows 11 |
| Python | 3.11.9 |
| VS Code | Julio 2026 |
| LangChain | versión vigente |
| langchain-core | versión vigente |
| langchain-google-genai | versión vigente |
| Cohere SDK | 5.21.1 |

---

# Instalación recomendada

Se recomienda utilizar un entorno virtual.

## Crear el entorno

```bash
python -m venv .venv-gemini-3
```

## Activar el entorno

Windows

```powershell
.venv-gemini-3\Scripts\activate
```

Actualizar pip

```bash
python -m pip install --upgrade pip
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Cambios realizados

---

# Gemini

## Problema

Los modelos utilizados por el curso fueron retirados de la API.

Código original

```python
GEMINI_FLASH = "gemini-1.5-flash"
GEMINI_PRO = "gemini-1.5-pro"
```

Al ejecutar el proyecto se obtiene un error similar a:

```
404 models/gemini-1.5-flash is not found
```

## Solución

Actualizar el archivo

```
my_models.py
```

por

```python
GEMINI_FLASH = "gemini-2.5-flash"
GEMINI_PRO = "gemini-2.5-pro"
```

---

# Verificación de modelos disponibles

Puede utilizarse el siguiente script para consultar los modelos disponibles:

```python
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

for model in genai.list_models():
    print(model.name)
```

---

# Advertencia de google.generativeai

Durante la ejecución aparece:

```
FutureWarning

All support for google.generativeai has ended...
```

## Causa

La advertencia es generada internamente por:

```
langchain_google_genai
```

El proyecto continúa funcionando correctamente.

No requiere ninguna modificación adicional.

---

# Cohere

## Problema

El curso utiliza

```python
from langchain_cohere import ChatCohere
```

Con las bibliotecas actuales aparece:

```
ImportError

cannot import name 'ChatResponse'
```

## Causa

Existe una incompatibilidad entre:

- langchain-cohere
- SDK moderno de Cohere

---

# Solución adoptada

Se eliminó completamente ChatCohere.

En su lugar se utiliza el SDK oficial.

Antes

```python
llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY
)
```

Ahora

```python
import cohere

co = cohere.ClientV2(
    api_key=COHERE_API_KEY
)
```

---

# Cambio importante

ClientV2 NO es un Runnable de LangChain.

Por esta razón ya no puede utilizarse:

```python
prompt | llm | parser
```

Debe utilizarse directamente:

```python
response = co.chat(...)
```

---

# HerramientaExplicar

Esta herramienta fue modificada completamente.

Antes

```
PromptTemplate
        │
        ▼
ChatCohere
        │
        ▼
StrOutputParser
```

Ahora

```
PromptTemplate
        │
        ▼
prompt.format(...)
        │
        ▼
ClientV2.chat(...)
        │
        ▼
response.message.content[0].text
```

---

# HerramientaAnalisisImagen

No fue necesario modificar la lógica.

Únicamente utiliza los nuevos modelos de Gemini.

---

# Agentes

Se verificó el correcto funcionamiento de:

- AgentExecutor

- create_react_agent

- Tool

- BaseTool

No requirieron modificaciones.

---

# LangSmith

Puede aparecer la advertencia:

```
LangSmithMissingAPIKeyWarning
```

No es un error.

Simplemente indica que no se configuró una API Key para LangSmith.

Puede ignorarse.

---

# Compatibilidad de archivos

| Archivo | Estado | Observaciones |
|----------|---------|--------------|
| my_models.py | Modificado | Nuevos modelos Gemini |
| lang_chain.py | Modificado | Migración de Cohere |
| herramienta_explicar.py | Modificado | SDK oficial ClientV2 |
| herramienta_analisis_imagen.py | Compatible | Sin cambios importantes |
| orquestador.py | Compatible | Sin cambios |
| detalles_imagen.py | Compatible | Sin cambios |
| main.py | Compatible | Sin cambios |

---

# Bibliotecas verificadas

Se verificó compatibilidad con:

- langchain

- langchain-core

- langchain-google-genai

- pydantic

- typing

- AgentExecutor

- PromptTemplate

- ChatPromptTemplate

- JsonOutputParser

- StrOutputParser

- BaseTool

---

# Recomendaciones

Se recomienda utilizar:

- Python 3.11
- Entorno virtual
- SDK oficial de Cohere
- Gemini 2.5 o superior

No se recomienda intentar utilizar los modelos Gemini 1.5, ya que dejaron de estar disponibles.

---

# Trabajo futuro

En futuras actualizaciones de este repositorio se documentarán nuevas incompatibilidades que puedan aparecer con:

- LangChain
- Gemini
- Cohere
- Pydantic
- Python

---

# Referencias

Google Gemini

https://ai.google.dev/

LangChain

https://python.langchain.com/

Cohere

https://docs.cohere.com/

---

# Créditos

Documento elaborado durante la adaptación del proyecto a las bibliotecas modernas.

Fecha de adaptación:

**Julio de 2026**

Todas las modificaciones descritas fueron implementadas, probadas y verificadas mediante la ejecución satisfactoria del proyecto completo.