import openai
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
env_path = r"C:\Users\theot\Desktop\uso_ia\key.env"
load_dotenv(env_path)

# Obtener la clave API desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_respuesta_chat(prompt):
    try:
        # Enviar la solicitud usando la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # O GPT-4 según tu caso
            messages=[ 
                {"role": "system", "content": "Actúa como un experto en marketing y redes sociales especializado en la promoción de marcas deportivas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150  # Limite de tokens para la respuesta
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Prompt del ejercicio 1 (adaptado)
prompt_ejercicio1 = """
Contexto:  
Actúa como un experto en marketing y redes sociales especializado en la promoción de marcas deportivas.  
Instrucción:  
Crea un texto detallado para una publicación en redes sociales (LinkedIn, Instagram, Twitter) para promocionar una colaboración entre la marca de zapatillas deportivas SkyStep y el atleta de baloncesto Brichard.  
El texto debe incluir un resumen conciso pero informativo sobre las ventajas técnicas y las características increíbles del modelo de zapatillas **Lotus**.  
Destaca sus innovaciones tecnológicas, como la suela antideslizante, la comodidad durante largos entrenamientos y su soporte para movimientos rápidos, saltos altos y resistencia. Resalta cómo estas características están diseñadas para optimizar el rendimiento en el baloncesto y mejorar la experiencia del atleta.  
El tono debe ser inspirador y dinámico, captando la atención de los usuarios de redes sociales con un enfoque en el rendimiento deportivo y la innovación.  
Input:  
1. La colaboración es entre la marca SkyStep y el atleta Brichard.  
2. El modelo de zapatillas se llama Lotus.  
3. El tono debe ser inspirador y dinámico.  
4. El texto debe incluir hashtags relevantes (#baloncesto, #estilodeportivo, etc.) y emojis para captar la atención.  
Output esperado:  
Un texto detallado que resuma las increíbles características de las zapatillas Lotus, explicando cómo su diseño y tecnología benefician a los atletas, especialmente en el baloncesto, y cómo pueden mejorar el rendimiento deportivo de los usuarios.
"""

# Ejemplo de llamada con el prompt del ejercicio 1
respuesta = generar_respuesta_chat(prompt_ejercicio1)
print("Respuesta generada:", respuesta)
