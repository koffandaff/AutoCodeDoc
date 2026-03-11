app.models.vehicle
==================

.. py:module:: app.models.vehicle


Classes
-------

.. autoapisummary::

   app.models.vehicle.Vehicle
   app.models.vehicle.VehicleCreate


Module Contents
---------------

.. py:class:: Vehicle(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A motorized vehicle registered in the system.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: make
      :type:  str
      :value: None



   .. py:attribute:: model
      :type:  str
      :value: None



   .. py:attribute:: vin
      :type:  str
      :value: None



   .. py:attribute:: year
      :type:  int
      :value: None



.. py:class:: VehicleCreate(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Payload to register a new vehicle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: make
      :type:  str
      :value: None



   .. py:attribute:: model
      :type:  str
      :value: None



   .. py:attribute:: vin
      :type:  str
      :value: None



   .. py:attribute:: year
      :type:  int
      :value: None



