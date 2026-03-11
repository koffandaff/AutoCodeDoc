app.services.user_service
=========================

.. py:module:: app.services.user_service


Attributes
----------

.. autoapisummary::

   app.services.user_service.FAKE_DB


Functions
---------

.. autoapisummary::

   app.services.user_service.create_user
   app.services.user_service.deactivate_user
   app.services.user_service.fetch_user_by_id


Module Contents
---------------

.. py:function:: create_user(user_id: int, username: str, email: str, bio: Optional[str] = None) -> app.models.user.User
   :async:


   Create a new user and add to the database.

   Args:
       user_id (int): The assigned ID.
       username (str): The desired username.
       email (str): The email address.
       bio (Optional[str]): Operational biography for the new user.

   Returns:
       User: The newly populated user.


.. py:function:: deactivate_user(user_id: int) -> bool
   :async:


   Mark a user as inactive in the database.

   This feature ensures logical deletion while preserving history.

   Args:
       user_id (int): The ID of the user to deactivate.

   Returns:
       bool: True if deactivated, False if user not found.


.. py:function:: fetch_user_by_id(user_id: int) -> Optional[app.models.user.User]
   :async:


   Retrieve a user from the simulated database by ID.

   Args:
       user_id (int): The unique identifier.

   Returns:
       Optional[User]: The user instance if found, otherwise None.


.. py:data:: FAKE_DB

