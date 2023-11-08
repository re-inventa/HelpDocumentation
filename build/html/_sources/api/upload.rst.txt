/upload
========================

.. http:post:: /api/upload (Ejemplo)

   Gestiona la carga de archivos a un contenedor de Azure Blob Storage.

   **Cabeceras Requeridas**:

   - `container-name` (string) -- El nombre del contenedor donde se guardará el archivo.
   - `azure-token` (string) -- El token SAS para la autenticación con Azure Blob Storage.

   **Parámetros del Formulario**:
   
   - `file` (archivo) -- El archivo a subir.

   .. warning::
      Asegúrate de que el token SAS y el nombre del contenedor son válidos para evitar errores de autenticación.

   **Respuestas**:

   :statuscode 401: No autorizado - Si el usuario no está autenticado.
   :statuscode 400: Solicitud Incorrecta - Si las cabeceras requeridas no están presentes.
   :statuscode 303: Vea Otros - Redirección tras una carga exitosa.
   :statuscode 500: Error Interno del Servidor - Si ocurre un error durante la carga del archivo.

   **Ejemplo de uso**:

   .. literalinclude:: examples/upload-example.js
      :language: javascript
      :linenos:
      :emphasize-lines: 3,5,7-10,15-20,30-35

   .. note::
      Este ejemplo utiliza el middleware ``auth.js`` para asegurar que el usuario esté autenticado antes de permitir la carga del archivo.
