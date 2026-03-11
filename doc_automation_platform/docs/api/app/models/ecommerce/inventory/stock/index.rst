app.models.ecommerce.inventory.stock
====================================

.. py:module:: app.models.ecommerce.inventory.stock


Classes
-------

.. autoapisummary::

   app.models.ecommerce.inventory.stock.InventoryItem
   app.models.ecommerce.inventory.stock.WarehouseLocation


Module Contents
---------------

.. py:class:: InventoryItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An item stored in the warehouse.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: location
      :type:  Optional[WarehouseLocation]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: sku
      :type:  str
      :value: None



   .. py:attribute:: status
      :type:  Literal['available', 'reserved', 'shipped']
      :value: None



   .. py:attribute:: weight_kg
      :type:  Union[float, int]
      :value: None



.. py:class:: WarehouseLocation(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A physical storage location.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: aisle
      :type:  str
      :value: None



   .. py:attribute:: bin
      :type:  str
      :value: None



   .. py:attribute:: shelf
      :type:  str
      :value: None



