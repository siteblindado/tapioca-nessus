# coding: utf-8
import os
import json
import unittest
from hashlib import sha256

import requests_mock

from tapioca_nessus import Nessus

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')


class TestScanners(unittest.TestCase):

    def setUp(self):
        self.wrapper = Nessus()

    def test_list_scanners(self):
        access_key = sha256().hexdigest()
        secret_key = sha256().hexdigest()
        headers = {
            'X-ApiKeys': f'accessKey={access_key}; secretKey={secret_key};'}
        file_contents = open(
            os.path.join(
                PROJECT_ROOT, 'tests/test_files/list_scanners.json')).read()
        with requests_mock.Mocker() as m:
            m.get('https://localhost:8834/scanners',
                  text=file_contents,
                  headers=headers)
            self.assertEqual(
                self.wrapper.list_scanners().get(
                    headers=headers, verify=False)().data,
                json.loads(file_contents)
            )

    def test_get_scanner_key(self):
        access_key = sha256().hexdigest()
        secret_key = sha256().hexdigest()
        headers = {
            'X-ApiKeys': f'accessKey={access_key}; secretKey={secret_key};'}
        expected_result = {"key": "9550264f6eb759da9ea5d6e6ebb8db022ea386331fce0331e8b547e59d3a0886"}
        with requests_mock.Mocker() as m:
            m.get('https://localhost:8834/scanners',
                  text=json.dumps(expected_result),
                  headers=headers)
            self.assertEqual(
                self.wrapper.list_scanners().get(
                    headers=headers, verify=False)().data,
                expected_result
            )


if __name__ == '__main__':
    unittest.main()
