app.api.billing
===============

.. py:module:: app.api.billing


Attributes
----------

.. autoapisummary::

   app.api.billing.router


Functions
---------

.. autoapisummary::

   app.api.billing.create_invoice


Module Contents
---------------

.. py:function:: create_invoice(org_id: str)
   :async:


   Create a new invoice.

   Generates the monthly invoice for the specified organization.

   Args:
       org_id (str): The unique identifier of the organization to bill.

   Returns:
       Invoice: The generated, unpaid invoice object.


.. py:data:: router

