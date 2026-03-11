app.api.vehicles
================

.. py:module:: app.api.vehicles


Attributes
----------

.. autoapisummary::

   app.api.vehicles.router


Functions
---------

.. autoapisummary::

   app.api.vehicles.create_vehicle


Module Contents
---------------

.. py:function:: create_vehicle(vehicle: app.models.vehicle.VehicleCreate) -> dict
   :async:


   Register a new vehicle into the platform.

   This endpoint takes vehicle details and processes them through the
   vehicle service layer for permanent registration.

   Args:
       vehicle (VehicleCreate): The vehicle registration payload containing VIN, make, model, and year.

   Returns:
       dict: A confirmation message with registration status and vehicle details.


.. py:data:: router

