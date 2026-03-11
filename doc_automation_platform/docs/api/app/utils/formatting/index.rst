app.utils.formatting
====================

.. py:module:: app.utils.formatting


Functions
---------

.. autoapisummary::

   app.utils.formatting.format_currency


Module Contents
---------------

.. py:function:: format_currency(amount: float, currency_code: str = 'USD') -> str

   Formats a raw float amount into a localized currency string.

   Args:
       amount: The float value.
       currency_code: ISO-4217 standard currency code.

   Returns:
       str: Human-readable currency string.


