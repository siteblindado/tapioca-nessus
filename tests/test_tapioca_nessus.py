# coding: utf-8

import unittest

from tapioca_nessus import Nessus


class TestTapiocaNessus(unittest.TestCase):

    def setUp(self):
        self.wrapper = Nessus()


if __name__ == '__main__':
    unittest.main()
