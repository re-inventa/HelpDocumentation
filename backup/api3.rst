API3 Documentation3
===================

.. toctree::
   :maxdepth: 2

Introduction
------------

Esta es la documentación de la API para la aplicación NextJS.

.. http:get:: /users/(int:id)

   Obtiene la información de un usuario específico por su ID.

   :param id: El ID único del usuario.
   :>json string username: El nombre de usuario.
   :>json string email: La dirección de correo electrónico del usuario.
   :>json string: El nombre completo del usuario.
   :status 200: cuando el usuario se encuentra correctamente.
   :status 404: cuando el usuario no se encuentra.

   **Ejemplo de solicitud**:

   .. sourcecode:: http

      GET /users/123 HTTP/1.1
      Host: example.com

   **Ejemplo de respuesta**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "username": "xekro",
        "email": "xekro@example.com",
        "name": "Xekro User"
      }

.. http:post:: /users/

   Crea un nuevo usuario.

   :<json string username: El nombre de usuario deseado.
   :<json string email: La dirección de correo electrónico del usuario.
   :<json string password: La contraseña del usuario.
   :>json int id: El ID del usuario recién creado.
   :status 201: cuando el usuario se crea correctamente.
   :status 400: cuando la solicitud no tiene el formato correcto.

   **Ejemplo de solicitud**:

   .. sourcecode:: http

      POST /users/ HTTP/1.1
      Host: example.com
      Content-Type: application/json

      {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword123"
      }

   **Ejemplo de respuesta**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json

      {
        "id": 124
      }
