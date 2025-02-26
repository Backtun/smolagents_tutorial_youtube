import os
from smolagents import CodeAgent, OpenAIServerModel, tool

api_key = os.environ["OPENAI_API_KEY"]

modelo_openai = OpenAIServerModel(model_id="o3-mini", api_key=api_key)

@tool
def base_de_conocimiento(query: str) -> str:
    """
    Simula una búsqueda en una base de conocimientos (FAQ) interna.
    En un escenario real, esta función consultará una base de datos o servicio de FAQ.
    
    Args:
        query: La consulta del usuario para buscar en la base de conocimientos.
    
    Returns:
        str: La respuesta encontrada en la base de conocimientos o un mensaje predeterminado.
    """
    faq_db = {
        "problema de conexión": "Para resolver problemas de conexión, reinicia tu router y verifica la configuración de red.",
        "error 404": "El error 404 indica que la página solicitada no se encontró en nuestro servidor.",
        "facturación": "Para consultas de facturación, por favor contacta a soporte al 123-456-7890."
    }
    # Busca coincidencias simples (puedes mejorar con NLP)
    for key, answer in faq_db.items():
        if key in query.lower():
            return answer
    return "Lo siento, no encontré información relevante en nuestra base de conocimientos."

agent = CodeAgent(
    tools=[base_de_conocimiento],
    model=modelo_openai
)

# Ejemplo: el cliente consulta sobre un error de conexión
result = agent.run("problema de conexión")
print("Respuesta del agente:", result)