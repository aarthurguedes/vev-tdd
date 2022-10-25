import unittest

from app.bill_of_sale_generator import BillOfSaleGenerator

class TesteBillOfSaleGenerator(unittest.TestCase):
  def test_invalid_param_to_generate(self):
    generator = BillOfSaleGenerator()
    with self.assertRaises(Exception):
      generator.generate('Invoice')
