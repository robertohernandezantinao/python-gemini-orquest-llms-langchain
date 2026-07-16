# Compatibilidad (Actualizado a julio de 2026)

## Entorno utilizado

- Windows 11
- Python 3.11.9
- LangChain 0.3.7
- langchain-google-genai 2.0.4
- google-generativeai 0.8.6
- Cohere 5.21.1

---

# Cambios necesarios

## 1. Modelos Gemini

Antes:

GEMINI_FLASH = "gemini-1.5-flash"
GEMINI_PRO   = "gemini-1.5-pro"

Ahora:

GEMINI_FLASH = "gemini-2.5-flash"
GEMINI_PRO   = "gemini-2.5-pro"

Motivo:
Los modelos Gemini 1.5 dejaron de estar disponibles para la API utilizada actualmente.

Error que aparecía:

404 models/gemini-1.5-flash is not found...

Solución:
Usar los modelos listados por la API.

---

## 2. LangChain + Cohere

Problema:

ImportError:
cannot import name 'ChatResponse'

Motivo:

langchain-cohere intenta importar una clase que ya no existe
en el SDK actual de Cohere.

Solución adoptada:

Usar el SDK oficial:

import cohere

co = cohere.ClientV2(...)

en lugar de ChatCohere.

---

## 3. Advertencia google.generativeai

FutureWarning...

Motivo:

Google está migrando al paquete google.genai.

Estado:

No afecta al funcionamiento actual, pero será necesario migrar en el futuro.

---

## 4. Creación del entorno virtual

...

---

## 5. Instalación de dependencias

...

---

## 6. Problemas encontrados

...

---

## 7. Soluciones aplicadas

...