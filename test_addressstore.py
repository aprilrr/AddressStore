# test_addressstore.py
"""
Tests for AddressStore module.
"""

import unittest
from addressstore import AddressStore

class TestAddressStore(unittest.TestCase):
    """Test cases for AddressStore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AddressStore()
        self.assertIsInstance(instance, AddressStore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AddressStore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
