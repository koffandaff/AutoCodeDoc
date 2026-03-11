app.api.auth
============

.. py:module:: app.api.auth


Attributes
----------

.. autoapisummary::

   app.api.auth.router


Functions
---------

.. autoapisummary::

   app.api.auth.login


Module Contents
---------------

.. py:function:: login(username: str, password: str) -> dict
   :async:


   Authenticate a user and return an access token.

   Verifies the provided credentials against the active database.
   If valid, a JWT token is generated for subsequent requests.

   Args:
       username (str): The login identifier.
       password (str): The secret password for the user.

   Returns:
       dict: containing the `access_token` and `token_type`.

   Raises:
       HTTPException:
           - 401: If credentials are not valid.


.. py:data:: router

