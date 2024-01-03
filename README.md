# Ejecutar Repositorio con Streamlit

## 1. Configuración del Ambiente de Desarrollo

### Clonar el Repositorio
```bash
git clone git@github.com:jonanfu/curso_big_data.git
cd curso_big_data

Crear un Entorno Virtual (Opcional, pero recomendado)

bash

python -m venv venv

Activar el Entorno Virtual

    En Windows:

bash

.\venv\Scripts\activate

    En Linux/Mac:

bash

source venv/bin/activate

2. Instalación de Librerías
Instalar Dependencias con Pip

bash

pip install -r requirements.txt

3. Ejecutar la Aplicación
Comando para Ejecutar Streamlit

bash

streamlit run main.py

Esto iniciará la aplicación Streamlit y abrirá tu navegador web predeterminado con la interfaz de la aplicación. Si hay algún problema con el puerto predeterminado, Streamlit sugerirá automáticamente un puerto alternativo.
4. Desactivar el Entorno Virtual (Opcional)

bash

deactivate