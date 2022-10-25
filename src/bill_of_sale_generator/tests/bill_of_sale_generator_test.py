import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from app.bill_of_sale_generator import BillOfSaleGenerator
from app.invoice import Invoice
from app.bill_of_sale import BillOfSale

class TesteBillOfSaleGenerator(unittest.TestCase):
  @patch('app.smtp.SMTP')
  @patch('app.sap.SAP')
  @patch('app.bill_of_sale_dao.BillOfSaleDAO')
  def test_invalid_param_to_generate(self, MockSMTP, MockSAP, MockBillOfSaleDAO):
    generator = BillOfSaleGenerator(MockSMTP(), MockSAP(), MockBillOfSaleDAO())
    with self.assertRaises(Exception):
      generator.generate('Invoice')

  @patch('app.smtp.SMTP')
  @patch('app.sap.SAP')
  @patch('app.bill_of_sale_dao.BillOfSaleDAO')
  def test_generate_bill_of_sale(self, MockSMTP, MockSAP, MockBillOfSaleDAO):
    invoiceConsultancy = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'CONSULTANCY', 200)
    generator = BillOfSaleGenerator(MockSMTP(), MockSAP(), MockBillOfSaleDAO())
    
    result = generator.generate(invoiceConsultancy)
    
    expected_client_name = 'Arthur'
    expected_value = 200
    expected_tax_value = 50
    
    self.assertTrue(isinstance(result, BillOfSale))
    self.assertEqual(result.client_name, expected_client_name)
    self.assertEqual(result.value, expected_value)
    self.assertEqual(result.tax_value, expected_tax_value)

  @patch('app.smtp.SMTP')
  @patch('app.sap.SAP')
  @patch('app.bill_of_sale_dao.BillOfSaleDAO')
  def test_calc_tax_value(self, MockSMTP, MockSAP, MockBillOfSaleDAO):
    invoiceConsultancy = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'CONSULTANCY', 200)
    invoiceTraining = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'TRAINING', 200)
    invoiceOther = Invoice('Arthur', '9840 International Dr, Orlando, Florida, US', 'OTHER', 200)

    generator = BillOfSaleGenerator(MockSMTP(), MockSAP(), MockBillOfSaleDAO())

    self.assertEqual(generator.calc_tax_value(invoiceConsultancy.service_type, invoiceConsultancy.value), 50)
    self.assertEqual(generator.calc_tax_value(invoiceTraining.service_type, invoiceTraining.value), 30)
    self.assertEqual(generator.calc_tax_value(invoiceOther.service_type, invoiceOther.value), 12)
