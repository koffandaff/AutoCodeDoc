app.services.payment_service
============================

.. py:module:: app.services.payment_service


Functions
---------

.. autoapisummary::

   app.services.payment_service.create_transaction


Module Contents
---------------

.. py:function:: create_transaction(amount: float, currency: str) -> dict
   :async:


   Create a payment transaction record in the simulated gateway.

   Args:
       amount (float): The payment amount.
       currency (str): The currency used for the transaction.

   Returns:
       dict: The created transaction record including a unique UUID.


