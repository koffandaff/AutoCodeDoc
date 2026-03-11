app.services.notification_service
=================================

.. py:module:: app.services.notification_service


Attributes
----------

.. autoapisummary::

   app.services.notification_service.notification_service


Classes
-------

.. autoapisummary::

   app.services.notification_service.NotificationService


Module Contents
---------------

.. py:class:: NotificationService

   Service handling notification delivery logic.


   .. py:method:: send_notification(user_id: int, notif_type: str, message: str) -> bool
      :async:


      Dispatch a notification to a specific user.

      Args:
          user_id: The recipient's user ID.
          notif_type: The channel (email, sms, push).
          message: The content to deliver.

      Returns:
          bool: True if dispatched successfully, False otherwise.

      Raises:
          ValueError: If an unsupported notification type is provided.



.. py:data:: notification_service

