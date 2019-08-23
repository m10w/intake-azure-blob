#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
import versioneer

here = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, here)

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')

with open(requirements_path) as requirements_file:
    requires = requirements_file.readlines()

setup(
    name='intake_azure_blob',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Azure Blob plugin for Intake',
    url='https://github.com/hamed2005/intake-azure-blob',
    maintainer='Hamed Borhani',
    maintainer_email='hamed2005@gmail.com',
    license='BSD',
    py_modules=['intake_azure_blob'],
    packages=find_packages(),
    package_data={'': ['*.csv', '*.yml', '*.html']},
    include_package_data=True,
    install_requires=requires,
    long_description=open('README.md').read(),
    zip_safe=False,
    entry_points={
        'intake.drivers': [
            'azure_blob = intake_azure_blob.azure_blob.AzureBlobSource'
        ]
    },
)
