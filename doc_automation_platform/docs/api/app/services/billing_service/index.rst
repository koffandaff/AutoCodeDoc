app.services.billing_service
============================

.. py:module:: app.services.billing_service


Functions
---------

.. autoapisummary::

   app.services.billing_service.generate_invoice


Module Contents
---------------

.. py:function:: generate_invoice(org: app.models.core.organization.Organization, items: List[app.models.ecommerce.billing.invoice.InvoiceItem]) -> app.models.ecommerce.billing.invoice.Invoice
   :async:


   Generates a billing invoice for an organization.

   Calculates the total amount based on unit prices and quantities.

   Args:
       org: The target organization.
       items: List of billable items.

   Returns:
       Invoice: The generated, unpaid invoice.


