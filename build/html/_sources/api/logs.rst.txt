/logs
========================

.. http:post:: /api/logs (Ejemplo)

   Recupera las transacciones del usuario y devuelve los datos en formato JSON.

   **Requiere Autenticación**:

   Este endpoint requiere que el usuario esté autenticado. Si no lo está, devolverá un error 401.

   **Parámetros de Respuesta**:
   
   - `id` (string) -- El identificador único del usuario autenticado.

   .. warning::
    Este endpoint es para uso interno y requiere que el usuario esté autenticado previamente. No exponer públicamente sin las medidas de seguridad apropiadas.


   **Respuestas**:

   :statuscode 200: OK - Devuelve los datos de las transacciones del usuario.
   :statuscode 401: No Autorizado - Si el usuario no está autenticado.
   :statuscode 500: Error Interno del Servidor - Si ocurre un error al recuperar los datos de las transacciones.

   **Ejemplo de uso**:

   .. code-block:: javascript

      // Este ejemplo supone que el usuario ya ha sido autenticado y tiene un 'id' válido.
      fetch('/api/logs', {
          method: 'POST',
          headers: {
              // Se requieren las cabeceras de autenticación adecuadas
          }
      })
      .then(response => {
          if (response.ok) {
              return response.json();
          }
          throw new Error('Network response was not ok.');
      })
      .then(data => console.log(data))
      .catch(error => console.error('Error al recuperar transacciones:', error));

   .. note::
      El manejo de errores sigue un patrón estándar de JSON para las respuestas. Cualquier error del servidor se devuelve como un mensaje JSON con una propiedad `error`.
