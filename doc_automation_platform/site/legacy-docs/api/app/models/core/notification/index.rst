app.models.core.notification
============================

.. py:module:: app.models.core.notification


Classes
-------

.. autoapisummary::

   app.models.core.notification.Notification
   app.models.core.notification.NotificationCreate


Module Contents
---------------

.. py:class:: Notification(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Notification model for system alerts and user messages.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: message
      :type:  str
      :value: None



   .. py:attribute:: read
      :type:  bool
      :value: None



   .. py:attribute:: type
      :type:  Literal['email', 'sms', 'push']
      :value: None



   .. py:attribute:: user_id
      :type:  int
      :value: None



.. py:class:: NotificationCreate(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Payload to trigger a new notification.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: message
      :type:  str
      :value: None



   .. py:attribute:: type
      :type:  Literal['email', 'sms', 'push']
      :value: None



   .. py:attribute:: user_id
      :type:  int
      :value: None



