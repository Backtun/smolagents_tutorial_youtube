from smolagents import CodeAgent, HfApiModel, Tool
import os
import shutil
from datetime import datetime
import re
import argparse
import string
import time

# Configurar argparse para aceptar un prompt personalizado y número de imágenes
parser = argparse.ArgumentParser(description='Genera imágenes a partir de un prompt utilizando IA.')
parser.add_argument('--prompt', type=str, help='Prompt para generar la imagen', default='A rabbit wearing a space suit')
parser.add_argument('--count', type=int, help='Número de imágenes a generar', default=1)
args = parser.parse_args()

# Obtener el prompt para la generación de imágenes y el número de imágenes
user_prompt = args.prompt
image_count = max(1, args.count)  # Asegurar al menos 1 imagen

# Verificar que la carpeta images existe, si no, crearla
if not os.path.exists("images"):
    os.makedirs("images")

image_generation_tool = Tool.from_space(
    space_id="black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt"
)

# Modificar la inicialización del modelo para usar el parámetro token correctamente
model = HfApiModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct", 
    token=os.environ["HUGGINGFACE_API_KEY"]
)

agent = CodeAgent(tools=[image_generation_tool], model=model)

# Crear variaciones del prompt para múltiples imágenes
variations = [
    "", 
    " with more details", 
    " in a dramatic lighting", 
    " with a dynamic pose", 
    " in a futuristic style", 
    " with a cinematic feel", 
    " with vibrant colors", 
    " in a minimalist style", 
    " with high contrast", 
    " from a different angle"
]

for i in range(image_count):
    # Seleccionar una variación para el prompt (si hay suficientes)
    variation = variations[i % len(variations)] if i > 0 else ""
    current_prompt = user_prompt + variation
    
    # Generar un nombre para la imagen basado en el prompt y la fecha/hora
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Convertir el prompt en un nombre de archivo válido (tomar las primeras palabras)
    prompt_words = re.sub(r'[^\w\s]', '', user_prompt).lower().split()
    prompt_filename = '_'.join(prompt_words[:3] if len(prompt_words) > 2 else prompt_words)
    # Añadir un contador si se están generando múltiples imágenes
    counter_suffix = f"_{i+1}" if image_count > 1 else ""
    image_filename = f"{prompt_filename}{counter_suffix}_{timestamp}.webp"
    image_path = os.path.join("images", image_filename)
    
    print(f"Generando imagen {i+1}/{image_count} para el prompt: '{current_prompt}'")
    
    # Ejecutar el agente y capturar el resultado
    result = agent.run(
        "Improve this prompt, then generate an image of it.", additional_args={'user_prompt': current_prompt}
    )
    
    # Buscar la ruta del archivo temporal en el resultado
    if isinstance(result, str):
        # Intentar extraer la ruta del archivo temporal usando expresiones regulares
        temp_image_path_match = re.search(r'C:\\Users\\.*\.webp', result)
        
        if temp_image_path_match:
            temp_image_path = temp_image_path_match.group(0)
            
            # Copiar el archivo a la carpeta images
            shutil.copy2(temp_image_path, image_path)
            print(f"Imagen guardada en: {image_path}")
        else:
            print("No se pudo encontrar la ruta de la imagen temporal en el resultado.")
            print("Resultado completo:", result)
    else:
        print("El resultado no es una cadena de texto como se esperaba.")
        print("Tipo de resultado:", type(result))
        print("Resultado:", result)
    
    # Esperar un poco entre generaciones si hay más imágenes por generar
    if i < image_count - 1:
        print("Esperando unos segundos antes de generar la siguiente imagen...")
        time.sleep(2)