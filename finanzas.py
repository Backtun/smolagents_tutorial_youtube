import os
from smolagents import CodeAgent, OpenAIServerModel, tool
import yfinance as yf

@tool
def fetch_stock_price(query: str) -> str:
    """
    Obtiene el precio actual de una acción utilizando la librería yfinance.

    Args:
        query: query (str): El query (simbolo) de la acción.

    Returns:
        str: El precio actual de la acción.
    """
    try:
        stock = yf.Ticker(query)
        data = stock.history(period="1d")
        if data.empty:
            return "No se pudo obtener el precio."
        current_price = data['Close'].iloc[-1]
        return f"El precio actual de {query} es ${current_price:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

# Configuramos el modelo para conectarse a un endpoint OpenAI (o similar)
model = OpenAIServerModel(
    model_id="o3-mini",
    api_base="https://api.openai.com/v1/",
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Inicializamos el agente con la herramienta financiera autorizando la importación de yfinance
agent = CodeAgent(
    tools=[fetch_stock_price],
    model=model,
    additional_authorized_imports=["yfinance"]
)

# Ejemplo: consultar el precio de Apple Inc. (AAPL)
result = agent.run("Obtén el precio actual de Apple usando la librería yfinance")
print("Precio de la acción:", result)
