import sys
sys.path.insert(1, "../app")
import unittest
import datetime
from invoice import Invoice

class Invoice_Test(unittest.TestCase):
    def test_invoice_object_is_created_correctly(self):
        random_date = datetime.datetime.now()
        random_value = 4398.20
        client_name = "Felipe"
        curr_invoice = Invoice(random_date, random_value, client_name)
        self.assertIsInstance(curr_invoice, Invoice)

if __name__ == '__main__':
    unittest.main()
