# SmolaAgents Tutorial

Este repositorio contiene ejemplos de uso de SmolaAgents para diferentes aplicaciones de IA.

## Contenido

- **Generación de Imágenes**: Utiliza IA para generar imágenes a partir de prompts de texto
- **Atención al Cliente**: Sistema automatizado para responder preguntas frecuentes
- **Finanzas**: Consulta de precios de acciones en tiempo real
- **Gemini**: Integración con la API de Gemini para búsquedas avanzadas

## Requisitos

Para ejecutar estos ejemplos necesitarás:

```
smolagents
yfinance
```

Y las siguientes claves API (configuradas en un archivo .env):
- OPENAI_API_KEY
- GEMINI_API_KEY

## Uso

Cada script puede ejecutarse de forma independiente:

```bash
# Generación de imágenes
python image_generation.py --prompt "Un conejo con traje espacial" --count 2

# Consulta financiera
python finanzas.py

# Atención al cliente
python atencion_cliente.py

# Búsqueda con Gemini
python gemini.py
```

## Notas

Este repositorio es parte de un tutorial de YouTube sobre el uso de agentes de IA pequeños para tareas específicas.
