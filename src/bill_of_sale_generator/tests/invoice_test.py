import unittest
from app.invoice import Invoice

class TestInvoice(unittest.TestCase):
  def test_missing_constructor_attrs(self):
    with self.assertRaises(Exception):
      Invoice()
  
  def test_creating(self):
    client_name = 'Arthur'
    client_address = '9840 International Dr, Orlando, Florida, US'
    service_type = 'CONSULTANCY'
    value = 199.99
    
    invoice = Invoice(client_name, client_address, service_type, value)
    
    self.assertEqual(invoice.client_name, client_name)
    self.assertEqual(invoice.client_address, client_address)
    self.assertEqual(invoice.service_type, service_type)
    self.assertEqual(invoice.value, value)
