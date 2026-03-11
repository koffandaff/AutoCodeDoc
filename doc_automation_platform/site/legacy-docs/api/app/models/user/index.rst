app.models.user
===============

.. py:module:: app.models.user


Classes
-------

.. autoapisummary::

   app.models.user.Product
   app.models.user.User


Module Contents
---------------

.. py:class:: Product(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simplified Product model.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: id
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: price
      :type:  float
      :value: None



.. py:class:: User(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Simplified User model for ER diagram stress testing.

   We have removed the nested Address model and other metadata
   to see if the ER diagram shrinks and simplifies automatically.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: email
      :type:  str
      :value: None



   .. py:attribute:: id
      :type:  int
      :value: None



   .. py:attribute:: username
      :type:  str
      :value: None



