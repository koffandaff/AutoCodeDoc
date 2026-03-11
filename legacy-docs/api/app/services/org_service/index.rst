app.services.org_service
========================

.. py:module:: app.services.org_service


Functions
---------

.. autoapisummary::

   app.services.org_service.create_organization


Module Contents
---------------

.. py:function:: create_organization(name: str, account_type: app.models.core.organization.AccountType, contact_emails: List[str]) -> app.models.core.organization.Organization
   :async:


   Creates a new enterprise organization in the system.

   Args:
       name: The legal name of the entity.
       account_type: The subscription level chosen.
       contact_emails: List of initial contact addresses.

   Returns:
       Organization: The fully formed organization record.


