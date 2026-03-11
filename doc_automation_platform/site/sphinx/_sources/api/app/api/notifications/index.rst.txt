app.api.notifications
=====================

.. py:module:: app.api.notifications


Attributes
----------

.. autoapisummary::

   app.api.notifications.router


Functions
---------

.. autoapisummary::

   app.api.notifications.trigger_notification


Module Contents
---------------

.. py:function:: trigger_notification(payload: app.models.core.notification.NotificationCreate)
   :async:


   Trigger a new system notification.

   This endpoint accepts a notification payload and dispatches it through the appropriate channel
   (email, SMS, or push) to the specified user.

   Args:
       payload: The NotificationCreate model containing target user and message data.

   Returns:
       Dict: A confirmation object indicating success or failure.

   Raises:
       HTTPException:
           400: If the notification service rejects the payload.


.. py:data:: router

