import unittest

from app.bill_of_sale_generator import BillOfSaleGenerator
from app.invoice import Invoice
from app.bill_of_sale import BillOfSale

class TesteBillOfSaleGenerator(unittest.TestCase):
  def test_invalid_param_to_generate(self):
    generator = BillOfSaleGenerator()
    with self.assertRaises(Exception):
      generator.generate('Invoice')

  def test_generate_bill_of_sale(self):
    invoiceConsultancy = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'CONSULTANCY', 200)
    generator = BillOfSaleGenerator()
    
    result = generator.generate(invoiceConsultancy)
    
    expected_client_name = 'Arthur'
    expected_value = 200
    expected_tax_value = 50
    
    self.assertTrue(isinstance(result, BillOfSale))
    self.assertEqual(result.client_name, expected_client_name)
    self.assertEqual(result.value, expected_value)
    self.assertEqual(result.tax_value, expected_tax_value)

  def test_calc_tax_value(self):
    invoiceConsultancy = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'CONSULTANCY', 200)
    invoiceTraining = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'TRAINING', 200)
    invoiceOther = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'OTHER', 200)

    generator = BillOfSaleGenerator()

    self.assertEqual(generator.calc_tax_value(invoiceConsultancy.service_type, invoiceConsultancy.value), 50)
    self.assertEqual(generator.calc_tax_value(invoiceTraining.service_type, invoiceTraining.value), 30)
    self.assertEqual(generator.calc_tax_value(invoiceOther.service_type, invoiceOther.value), 12)
