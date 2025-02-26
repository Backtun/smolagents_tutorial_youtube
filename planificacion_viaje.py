from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
import os

# Necesitarás tu clave de API de OpenAI
# Asegúrate de tenerla configurada como variable de entorno o pásala directamente
api_key = os.environ["OPENAI_API_KEY"]

# Paso 1: Configuramos el modelo de OpenAI
# Usaremos "o3-mini" como ejemplo, pero puedes usar otros como "o3-mini", "o1" o "gpt-4o"
modelo_openai = OpenAIServerModel(model_id="o3-mini", api_key=api_key)

# Paso 2: Añadimos una herramienta útil
# Aquí usamos DuckDuckGoSearchTool para que el agente pueda buscar en la web si lo necesita
herramientas = [DuckDuckGoSearchTool()]

# Paso 3: Creamos el agente
# CodeAgent es el tipo de agente que escribe acciones en código Python
agente = CodeAgent(
    tools=herramientas,  # Lista de herramientas disponibles para el agente
    model=modelo_openai  # El modelo de OpenAI que usará el agente
)

# Paso 4: Definimos una tarea para el agente
# Vamos a pedirle que Planifique un viaje de fin de semana a la Ciudad de Mexico
tarea = "Planifique un viaje de fin de semana a la Ciudad de Mexico"

# Paso 5: Ejecutamos el agente con la tarea
resultado = agente.run(tarea)

# Paso 6: Imprimimos el resultado
print("Resultado:")
print(resultado)