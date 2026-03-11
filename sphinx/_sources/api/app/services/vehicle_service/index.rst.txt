app.services.vehicle_service
============================

.. py:module:: app.services.vehicle_service


Functions
---------

.. autoapisummary::

   app.services.vehicle_service.register_vehicle


Module Contents
---------------

.. py:function:: register_vehicle(vin: str, make: str, model: str, year: int) -> Dict[str, Any]
   :async:


   Registers a new vehicle in the system database.

   Args:
       vin: Vehicle Identification Number.
       make: The manufacturer.
       model: The car model.
       year: The manufacturing year.

   Returns:
       dict: The registered vehicle data with a success status.


