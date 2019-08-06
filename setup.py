# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer

requires = open('requirements.txt').read().strip().split('\n')

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
