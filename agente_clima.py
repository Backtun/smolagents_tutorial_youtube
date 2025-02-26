from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel
import os

# Configurar la clave de API
api_key = os.environ["OPENAI_API_KEY"]

# Crear el modelo OpenAI
modelo = OpenAIServerModel(
    model_id="gpt-4o",
    api_key=api_key
)

web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=modelo,
    name="web_search"
)

manager_agent = CodeAgent(
    tools=[],
    model=modelo,
    managed_agents=[web_agent]
)

manager_agent.run("")