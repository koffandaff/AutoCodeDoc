app.models.ecommerce.billing.invoice
====================================

.. py:module:: app.models.ecommerce.billing.invoice


Classes
-------

.. autoapisummary::

   app.models.ecommerce.billing.invoice.Invoice
   app.models.ecommerce.billing.invoice.InvoiceItem


Module Contents
---------------

.. py:class:: Invoice(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A billing invoice for an organization.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: invoice_id
      :type:  str
      :value: None



   .. py:attribute:: is_paid
      :type:  bool
      :value: None



   .. py:attribute:: items
      :type:  List[InvoiceItem]
      :value: None



   .. py:attribute:: organization
      :type:  app.models.core.organization.Organization
      :value: None



   .. py:attribute:: total_amount
      :type:  float
      :value: None



.. py:class:: InvoiceItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Line item on an enterprise invoice.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: quantity
      :type:  int
      :value: None



   .. py:attribute:: unit_price
      :type:  float
      :value: None



