app.models.core.organization
============================

.. py:module:: app.models.core.organization


Classes
-------

.. autoapisummary::

   app.models.core.organization.AccountType
   app.models.core.organization.BaseEntity
   app.models.core.organization.Organization


Module Contents
---------------

.. py:class:: AccountType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of enterprise accounts.

   Initialize self.  See help(type(self)) for accurate signature.


   .. py:attribute:: BASIC
      :value: 'basic'



   .. py:attribute:: ENTERPRISE
      :value: 'enterprise'



   .. py:attribute:: PREMIUM
      :value: 'premium'



.. py:class:: BaseEntity(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for all enterprise entities.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: created_at
      :type:  str
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  Optional[Dict[str, Any]]
      :value: None



.. py:class:: Organization(/, **data: Any)

   Bases: :py:obj:`BaseEntity`


   An enterprise organization.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. py:attribute:: account_type
      :type:  AccountType
      :value: None



   .. py:attribute:: contact_emails
      :type:  List[str]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: parent_org_id
      :type:  Optional[str]
      :value: None



