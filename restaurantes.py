from smolagents import CodeAgent, OpenAIServerModel, VisitWebpageTool, DuckDuckGoSearchTool
from smolagents.tools import Tool
import os
from bs4 import BeautifulSoup

api_key = os.environ["OPENAI_API_KEY"]

modelo_openai = OpenAIServerModel(model_id="o3-mini", api_key=api_key)

class RatingExtractorTool(Tool):
    name = "rating_extractor"
    description = "Extrae nombres y calificaciones de restaurantes de una página de resultados de búsqueda de Yelp."
    inputs = {"html": {"type": "string", "description": "El contenido HTML de la página."}}
    output_type = "array"
    
    def forward(self, html: str) -> list:
        """
        Extrae nombres y calificaciones de restaurantes de una página de resultados de búsqueda de Yelp.

        Args:
            html (str): El contenido HTML de la página.

        Returns:
            list: Una lista de diccionarios, cada uno con las claves 'name' (nombre del restaurante), 'rating' (calificación numérica), 'cuisine', 'location' (ubicación).
        """
        # Crear objeto BeautifulSoup para parsear el HTML
        soup = BeautifulSoup(html, 'html.parser')
        
        # Lista para almacenar los restaurantes extraídos
        restaurants = []
        
        # Buscar todos los elementos que representan un restaurante
        for item in soup.find_all('div', class_='restaurant'):
            name = ""
            rating = 0.0
            cuisine = ""
            location = ""
            
            # Intentar extraer el nombre (puede estar en diferentes elementos)
            name_tag = item.find('h2')
            if not name_tag:
                name_tag = item.find('span', class_='name')
            
            # Extraer la calificación
            rating_tag = item.find('span', class_='rating')
            
            # Extraer la cocina (puede estar en diferentes elementos)
            cuisine_tag = item.find('p')
            if cuisine_tag and "Cocina:" in cuisine_tag.text:
                cuisine = cuisine_tag.text.replace("Cocina:", "").strip()
            
            # Extraer la ubicación
            location_tag = item.find('span', class_='location')
            
            # Verificar que los elementos necesarios existan
            if name_tag and rating_tag:
                name = name_tag.text.strip()
                
                try:
                    # Convertir el texto de la calificación a un número flotante
                    rating = float(rating_tag.text.strip())
                except ValueError:
                    # Si no se puede convertir a número, usar el valor predeterminado (0.0)
                    pass
                
                if location_tag:
                    location = location_tag.text.strip()
                
                # Agregar el restaurante a la lista como un diccionario
                restaurants.append({
                    'name': name, 
                    'rating': rating,
                    'cuisine': cuisine,
                    'location': location
                })
        
        print("Restaurantes extraidos:")
        print(restaurants)
        return restaurants

tools = [VisitWebpageTool(), DuckDuckGoSearchTool(), RatingExtractorTool()]

agent = CodeAgent(tools=tools, model=modelo_openai, additional_authorized_imports=["bs4"])

task = "Encuentra el mejor restaurante italiano en Ciudad de México con al menos 4.5 estrellas."

result = agent.run(task)

print(result)