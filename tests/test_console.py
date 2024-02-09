#!/usr/bin/python3
"""
"""


import unittest
import sys
sys.path.append('../')

import console

class TestConsole(unittest.TestCase):
    
    def setUp(self):
        self.console = console.HBNBCommand()
    
    def test_create(self):
        pass

