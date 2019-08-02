# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os
import pytest
from unittest.mock import patch
from intake import open_catalog
import dask.dataframe as dd


@pytest.fixture
def local_prefix_cat():
    path = os.path.dirname(__file__)
    return open_catalog(os.path.join(path, 'data', 'local.catalog.yaml'))


def test_local_prefix_catalog(local_prefix_cat):
    source = local_prefix_cat['test_azure_blob'].get()
    ds = source.read()
    assert isinstance(ds, pd.DataFrame)
    assert len(ds) == 622007


def test_azure_prefix_catalog():

    orig_read_csv = dd.read_csv

    def read_csv(path, *args, **kwargs):
        return orig_read_csv(_azure_uri_to_local(path), *args, **kwargs)

    def _azure_uri_to_local(url):
        return url.replace('abfs://', './tests/data/')

    def opener(url, mode='r'):
        return open(_azure_uri_to_local(url), mode)

    with patch('dask.dataframe.read_csv') as mock_read_csv:
        # patch('intake_s3_manifests.s3_manifest') as s3_manifest,

        mock_read_csv.side_effect = read_csv
        path = os.path.dirname(__file__)
        azure_prefix_cat = open_catalog(os.path.join(path, 'data', 'azure.catalog.yaml'))
        source = azure_prefix_cat['test_azure_blob'].get()
        ds = source.read()
        assert isinstance(ds, pd.DataFrame)
        assert len(ds) == 622007
