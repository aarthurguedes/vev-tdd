import unittest
from app.bill_of_sale import BillOfSale

class TestBillOfSale(unittest.TestCase):
  def test_missing_constructor_attrs(self):
    with self.assertRaises(Exception):
      BillOfSale()