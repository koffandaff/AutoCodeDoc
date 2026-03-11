app.api.organizations
=====================

.. py:module:: app.api.organizations


Attributes
----------

.. autoapisummary::

   app.api.organizations.router


Functions
---------

.. autoapisummary::

   app.api.organizations.register_organization


Module Contents
---------------

.. py:function:: register_organization(name: str, account_type: app.models.core.organization.AccountType, emails: List[str])
   :async:


   Register a new Organization.

   This endpoint initializes a new tenant space for enterprise customers.

   Args:
       name (str): The legal name of the organization.
       account_type (AccountType): The subscription tier (Basic, Premium, Enterprise).
       emails (List[str]): List of administrative contact email addresses.

   Returns:
       Organization: The newly created organization record


.. py:data:: router

