# 📘 Documentación de Re-Inventa

Se alojará la documentación y ayuda para usar las herramientas desarrolladas por Re-Inventa de forma abierta.

## 🤝 Cómo Colaborar

Para colaborar en la actualización e implementación de documentación en este proyecto es necesario conocer o usar un editor de Markdown para elaborar la documentación.

A continuación se dará una serie de instrucción que ayudará a como comenzar a colaborar en este proyecto.

Si los cambios son relativamente pequeños, se pueden hacer directamente desde la GUI de GitHub, es decir, editar los ficheros directamente aquí, y posteriormente solo hacer un commit que realizará un push automaticamente. Si este es el caso, leea sólo la sección '¡Manos a la Obra! ✍️' y 'Donde agregar imagenes u otros ficheros 💻'.

### Requisitos Previos 🚀

1. [Instala GitHub Desktop](https://desktop.github.com/) e incia sesión con tu cuenta.
2. Clona la rama `main` a un directorio de tu preferencia.
3. [Instala Python](https://apps.microsoft.com/detail/python-3-12/9NCVDN91XZQP) en su versión 3.12.

### Configuración del Entorno de Trabajo 🔧

Vamos a crear un entorno virtual para evitar conflictos entre paquetes y versiones de los mismos.

1. Crea un entorno virtual en la raiz del proyecto.
   ```
   python -m venv venv
   ```
2. Activa el entorno virtual de Python.
   ```
   ./venv/Scripts/activate
   ```
3. Instala todas las dependencias del proyecto.
   ```
   pip install -r requirements.txt
   ```

### ¡Manos a la Obra! ✍️

En el directorio `/source` se encuentran todos los ficheros que va ha utilizar para generar la build (los ficheros HTML).

Las secciones que puedes ver en la pagina web se realizan mediante carpetas en el codigo. Dentro se puede alojar tanto ficheros Markdown (`.md`) como Restructured Text (`.rst`), este último se considera más avanzado y es el que utiliza Sphinx por defecto.

Cada vez que añadas o cambies de nombre un fichero o carpeta, tendrás que actualizarlo manualmente en el toctree, dentro del fichero `index.rst`, si no, el fichero será ilocalizable en el menú.

### Donde agregar imagenes u otros ficheros 💻

En directorio `source/_static` es utilizado para el almacenamiento de ficheros que luego se utilizará en la pagina web, ya sea imagenes, sonidos, videos...

Ten en cuenta los limites de GitHub:

| **Aspecto**                                | **GitHub Free**                                                                                                    | **GitHub Team**                                                         | **GitHub Enterprise**                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Límite de Tamaño de Fichero Individual** | 2 GB                                                                                                               | 2 GB                                                                    | 5 GB                                                                      |
| **Límite de Tamaño de Repositorio**        | No limitado explícitamente, pero se recomienda mantenerlo por debajo de 5 GB para evitar problemas de rendimiento. | No especificado                                                         | No especificado                                                           |
| **Espacio de Almacenamiento de Paquetes**  | 500 MB                                                                                                             | 2 GB                                                                    | 50 GB                                                                     |
| **CI/CD Minutes/Month**                    | 2,000 (Gratis para repositorios públicos)                                                                          | 3,000 (Gratis para repositorios públicos)                               | 50,000 (Gratis para repositorios públicos)                                |
| **Precio**                                 | Gratis                                                                                                             | $4 por usuario/mes (Descuento a $3.67 por usuario/mes en el primer año) | $21 por usuario/mes (Descuento a $19.25 por usuario/mes en el primer año) |

> Cabe destacar que, aunque GitHub no limita explícitamente el tamaño total de los repositorios en su plan gratuito, recomiendan mantenerlos por debajo de 1 GB para optimizar el rendimiento y advierten que superar los 5 GB podría resultar en un contacto por parte del soporte de GitHub. Además, cada fichero individual no debe superar los 2 GB en los planes gratuitos y de Team, y 5 GB en el plan Enterprise.

### Como revisar los cambios 🔍

Con el entorno virtual activado:

- `./make.bat html` para generar los nuevos ficheros html, el resultado se pondrá en la carpeta `build/html`.
- `./make.bat clean` para eliminar los ficheros generados y evitar que entre en conflicto con anteriores versiones.

### Como subir los cambios 📤

Simplemente con un `push origin` desde la aplicación de GitHub Desktop los cambios se subirán al repositorio y GitHub Actions entrará en acción.

Procesará los ficheros HTML junto con las dependencias que se encuentran en `requirements.txt`, donde luego se exportará a la rama `gh-pages` para que lo pueda utilizar GitHub Pages.
