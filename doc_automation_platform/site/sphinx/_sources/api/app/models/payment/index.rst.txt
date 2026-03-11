app.models.payment
==================

.. py:module:: app.models.payment


Classes
-------

.. autoapisummary::

   app.models.payment.PaymentRequest
   app.models.payment.PaymentResponse


Module Contents
---------------

.. py:class:: PaymentRequest(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model used to initiate a payment transaction.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: amount
      :type:  float
      :value: None



   .. py:attribute:: currency
      :type:  str
      :value: None



   .. py:attribute:: payment_method
      :type:  str
      :value: None



.. py:class:: PaymentResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Response returned after a payment attempt.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: status
      :type:  str
      :value: None



   .. py:attribute:: transaction_id
      :type:  str
      :value: None



