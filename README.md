# 📰 Blog de Noticias Interactivo

¡Hola! Soy **Miguel Trombotto** y este es mi proyecto final para la Etapa 2 del **Informatorio 2024**. Armé un blog de noticias interactivo donde vas a poder leer, buscar y comentar sobre las últimas novedades.

## 🚀 Funcionalidades Principales

Este blog te ofrece una experiencia completa para que estés siempre al tanto:

-   **Buscador de Noticias:** Encontrá rápidamente lo que te interesa. Buscá por palabras clave en el título o el contenido de las noticias.
-   **Filtros por Categoría:** Organizá tu lectura. Filtrá las noticias por categorías específicas como "Tecnología", "Deportes", etc.
-   **Sistema de Comentarios:** Si estás logueado, podés dejar tu opinión y sumarte a la conversación en cada noticia.
-   **Panel de Administración:** Como administrador, tenés el control total. Gestioná noticias, categorías y comentarios de forma sencilla e intuitiva.
-   **Diseño Responsivo:** Desarrollado con **Bootstrap 5** para que la experiencia sea óptima desde cualquier dispositivo: tu celu, tablet o computadora.

## 🛠️ Stack Tecnológico

Para construir este proyecto, usé las siguientes herramientas y tecnologías:

-   **Lenguaje:** Python
-   **Framework:** Django
-   **Base de Datos:** SQLite (ideal para el desarrollo y despliegues rápidos)
-   **Estilos:** Bootstrap 5
-   **Despliegue:** PythonAnywhere

## ⚙️ Instalación y Ejecución Local

Si querés probar este proyecto en tu máquina, seguí estos pasos:

1.  **Cloná el repositorio:**
    ```bash
    git clone https://github.com/miguelrtrombotto/blog-django-final.git
    cd blog-django-final # Asegurate de entrar a la carpeta del proyecto
    ```
2.  **Activá el entorno virtual:**
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate # Usá esto si estás en Git Bash o Linux/macOS
    # Para CMD en Windows: .venv\Scripts\activate
    ```
3.  **Instalá las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ejecutá las migraciones:**
    ```bash
    python manage.py migrate
    ```
5.  **Iniciá el servidor:**
    ```bash
    python manage.py runserver
    ```
    Después de esto, abrí tu navegador y andá a `http://127.0.0.1:8000/` para ver el blog.

---

### 🌐 Link del Proyecto en Vivo

Podés ver el blog funcionando online en: [http://miguelrtrombotto.pythonanywhere.com/](http://miguelrtrombotto.pythonanywhere.com/)