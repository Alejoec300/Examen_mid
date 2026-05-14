# Examen_mid

Auth API Hashing - Proyecto Midterm

API de autenticación segura desarrollada con FastAPI, SQLModel, bcrypt y Pepper.

1. Instalación y Requisitos

Sigue estos pasos en orden para configurar el entorno correctamente:

Entrar a la carpeta del proyecto:
cd midterm

Crear el entorno virtual:
python -m venv venv

Activar el entorno virtual:
Windows (PowerShell): .\venv\Scripts\activate
Windows (CMD): venv\Scripts\activate

Instalar dependencias necesarias:
pip install fastapi uvicorn sqlmodel bcrypt python-dotenv

2. Configuración de Seguridad (Pepper)

El programa utiliza una variable de entorno para el Pepper. Debes crear el archivo de configuración:

Crea un archivo llamado .env en la carpeta midterm/.

Dentro del archivo, escribe lo siguiente:
PEPPER=TuClaveSecretaSuperSegura

3. Cómo ejecutar el programa

Para iniciar el servidor en modo desarrollo, asegúrate de tener el entorno virtual (venv) activo y ejecuta:

fastapi dev Examen.py

El servidor estará disponible en: http://127.0.0.1:8000

4. Pruebas en la API (Swagger)

FastAPI genera documentación automática. Puedes probar el registro y el login aquí:
http://127.0.0.1:8000/docs

Instrucciones de prueba:

Haz clic en el botón "Try it out".

Envía los datos en formato JSON:
{
"username": "usuario123",
"password": "mi_password"
}

Revisa la respuesta del servidor para confirmar el éxito.

Nota Técnica: Este sistema incluye un recorte automático de 72 bytes para las contraseñas, garantizando compatibilidad total con el algoritmo Bcrypt y evitando errores de longitud.
