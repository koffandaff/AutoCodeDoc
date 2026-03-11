app.models.auth
===============

.. py:module:: app.models.auth


Classes
-------

.. autoapisummary::

   app.models.auth.Token


Module Contents
---------------

.. py:class:: Token(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Authentication token details.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: access_token
      :type:  str
      :value: None



   .. py:attribute:: expires_in
      :type:  int
      :value: None



   .. py:attribute:: token_type
      :type:  str
      :value: None



