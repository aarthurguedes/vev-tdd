import unittest
from app.invoice import Invoice

class TestInvoice(unittest.TestCase):
  def test_missing_constructor_attrs(self):
    with self.assertRaises(Exception):
      Invoice()
