app.api.users
=============

.. py:module:: app.api.users


Attributes
----------

.. autoapisummary::

   app.api.users.router


Functions
---------

.. autoapisummary::

   app.api.users.create_user
   app.api.users.delete_user
   app.api.users.get_user


Module Contents
---------------

.. py:function:: create_user(user_data: app.models.user.UserCreate) -> app.models.user.User
   :async:


   Create a new user within the system.

   Accepts username and email payload to provision a new active user.

   Args:
       user_data (UserCreate): The incoming JSON payload representing setup parameters.

   Returns:
       User: The created User instance containing the assigned ID.


.. py:function:: delete_user(user_id: int)
   :async:


   Deactivate a user account.

   This is a soft-delete operation that updates the 'is_active' flag.


.. py:function:: get_user(user_id: int) -> app.models.user.User
   :async:


   Retrieve a user from the database by their unique ID.

   This endpoint queries the active database for a user matching the provided ID.
   If the user has been deactivated or does not exist, a 404 is returned.

   Args:
       user_id (int): The unique identifier of the user to retrieve.

   Returns:
       User: The user object containing profile details.

   Raises:
       HTTPException:
           - 404: If the user does not exist.


.. py:data:: router

