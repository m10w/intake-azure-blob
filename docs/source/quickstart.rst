Quickstart
==========

``intake-azure-blob`` provides quick and easy access to data stored in Azure Blob Storage.

.. Azure Blob Storage: https://azure.microsoft.com/en-us/services/storage/blobs/

Installation
------------

To use this plugin for `intake`_, install with the following command::

   conda install -c hamed2005 intake-azure-blob

.. _intake: https://github.com/ContinuumIO/intake

Usage
-----

Ad-hoc
~~~~~~

After installation, the function ``intake.open_azure_blob``
will become available. They can be used to open Azure Blobs.

Creating Catalog Entries
~~~~~~~~~~~~~~~~~~~~~~~~

Catalog entries must specify ``driver: azure-blob``.


Using a Catalog
~~~~~~~~~~~~~~~

