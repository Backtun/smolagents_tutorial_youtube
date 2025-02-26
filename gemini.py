from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import os

# Necesitarás tu clave de API de Gemini
# Asegúrate de tenerla configurada como variable de entorno o pásala directamente
api_key = os.environ["GEMINI_API_KEY"]

# Paso 1: Configuramos el modelo de Gemini
# Usaremos "gemini/gemini-2.0-flash-thinking-exp-01-21" como ejemplo
modelo = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash-thinking-exp-01-21",
    api_key=api_key
)

# Paso 2: Creamos el agente
# CodeAgent es el tipo de agente que escribe acciones en código Python
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()], # Lista de herramientas disponibles para el agente
    model=modelo # El modelo de Gemini que usará el agente
)

# Paso 3: Ejecutamos el agente con la tarea
agent.run("Últimos avances en computación cuantica")