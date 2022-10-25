import unittest

from app.bill_of_sale_generator import BillOfSaleGenerator
from app.invoice import Invoice

class TesteBillOfSaleGenerator(unittest.TestCase):
  def test_invalid_param_to_generate(self):
    generator = BillOfSaleGenerator()
    with self.assertRaises(Exception):
      generator.generate('Invoice')

  def test_calc_tax_value(self):
    invoiceConsultancy = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'CONSULTANCY', 200)
    invoiceTraining = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'TRAINING', 200)
    invoiceOther = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'OTHER', 200)

    generator = BillOfSaleGenerator()

    self.assertEqual(generator.calc_tax_value(invoiceConsultancy.service_type, invoiceConsultancy.value), 50)
    self.assertEqual(generator.calc_tax_value(invoiceTraining.service_type, invoiceTraining.value), 30)
    self.assertEqual(generator.calc_tax_value(invoiceOther.service_type, invoiceOther.value), 12)
