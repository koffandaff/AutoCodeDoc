app.api.inventory
=================

.. py:module:: app.api.inventory

.. autoapi-nested-parse::

   Inventory API Endpoints
   =======================

   Provides endpoints for managing physical inventory and system status across
   multiple warehouse facilities.



Attributes
----------

.. autoapisummary::

   app.api.inventory.router


Functions
---------

.. autoapisummary::

   app.api.inventory.get_inventory_status
   app.api.inventory.map_inventory_location


Module Contents
---------------

.. py:function:: get_inventory_status()
   :async:


   Retrieve the current operational status of the inventory system.

   This endpoint performs a heartbeat check on the warehouse management
   subsystem and returns a summary of active nodes.

   :param None:

   :returns: A dictionary containing:
             - status (str): System health ("operational", "degraded", "offline").
             - active_warehouses (int): Count of connected warehouse facilities.
             - last_sync (str): ISO timestamp of the last database sync.
   :rtype: :py:class:`dict`


.. py:function:: map_inventory_location(sku: str, aisle: str, shelf: str, bin_num: str)
   :async:


   Map an inventory item to a specific physical warehouse location.

   This endpoint heavily utilizes the nested WarehouseLocation model.

   Args:
       sku (str): The unique stock keeping unit identifier.
       aisle (str): The warehouse aisle.
       shelf (str): The shelf level.
       bin_num (str): The specific storage bin.

   Returns:
       InventoryItem: The updated item with its mapped physical location.


.. py:data:: router

