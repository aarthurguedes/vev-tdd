import unittest
from app.bill_of_sale import BillOfSale

class TestBillOfSale(unittest.TestCase):
  def test_missing_constructor_attrs(self):
    with self.assertRaises(Exception):
      BillOfSale()
  
  def test_creating(self):
    client_name = 'Arthur'
    value = 199.99
    tax_value = 49.99
    
    bill_of_sale = BillOfSale(client_name, value, tax_value)
    
    self.assertEqual(bill_of_sale.client_name, client_name)
    self.assertEqual(bill_of_sale.value, value)
    self.assertEqual(bill_of_sale.tax_value, tax_value)
  
  def test_attrs_in_to_string(self):
    client_name = 'Arthur'
    value = 199.99
    tax_value = 49.99
    
    bill_of_sale = BillOfSale(client_name, value, tax_value)
    container = bill_of_sale.to_string()

    self.assertIn(client_name, container)
    self.assertIn(str(value), container)
    self.assertIn(str(tax_value), container)
