app.utils.validation
====================

.. py:module:: app.utils.validation


Functions
---------

.. autoapisummary::

   app.utils.validation.sanitize_metadata
   app.utils.validation.validate_enterprise_email


Module Contents
---------------

.. py:function:: sanitize_metadata(data: dict) -> dict

   Sanitize metadata by removing null values and casting all values to strings.

   Ensures consistent, serialization-safe metadata output for
   downstream consumers including logging and analytics pipelines.

   Args:
       data (dict): Raw metadata dictionary, potentially containing None values.

   Returns:
       dict: Cleaned metadata with all values cast to strings.


.. py:function:: validate_enterprise_email(email: str) -> bool

   Validates that an email belongs to an approved enterprise domain.

   Args:
       email: The email string to check.

   Returns:
       bool: True if strictly valid, False otherwise.


