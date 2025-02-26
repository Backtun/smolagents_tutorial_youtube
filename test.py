from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
import os

# Necesitarás tu clave de API de OpenRouter
# Asegúrate de tenerla configurada como variable de entorno o pásala directamente
api_key = os.environ["OPENROUTER_API_KEY"]

# Paso 1: Configuramos el modelo de openrouter
# Usaremos "DEEPSEEK-R1:FREE" como ejemplo
modelo = OpenAIServerModel(
    model_id="deepseek/deepseek-r1:free",
    api_key=api_key,
    api_base="https://openrouter.ai/api/v1"
)

# Paso 2: Creamos el agente
# CodeAgent es el tipo de agente que escribe acciones en código Python
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()], # Lista de herramientas disponibles para el agente
    model=modelo # El modelo de OpenAI que usará el agente
)

# Paso 3: Ejecutamos el agente con la tarea
agent.run("¿Cuál es el último modelo de IA lanzado por Anthropic?")