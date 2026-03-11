app.api.payments
================

.. py:module:: app.api.payments


Attributes
----------

.. autoapisummary::

   app.api.payments.router


Functions
---------

.. autoapisummary::

   app.api.payments.process_payment


Module Contents
---------------

.. py:function:: process_payment(amount: float, currency: str = 'USD') -> dict
   :async:


   Process a new payment transaction.

   This endpoint initiates a payment process through our simulated gateway.
   It validates the amount and currency before proceeding.

   Args:
       amount (float): The total amount to be charged. Must be positive.
       currency (str): The ISO currency code (e.g., USD, EUR). Defaults to USD.

   Returns:
       dict: A confirmation message with the transaction_id and status.

   Raises:
       HTTPException:
           - **400**: If the amount is less than or equal to zero.


.. py:data:: router

