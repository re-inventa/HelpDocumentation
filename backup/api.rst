API Documentation 1
===================

.. http:get:: /users/(int:user_id)/posts/(tag)

   Fetches a list of all user's posts filtered by tag.

   **Example request**:

   .. sourcecode:: http

      GET /users/123/posts/web HTTP/1.1
      Host: example.com

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "post_id": 1,
          "title": "Best practices in Web Development"
        }
      ]
