import sys
sys.path.insert(1, "../app")
import unittest
import datetime
from invoice import Invoice
from payment import Payment

class Invoice_Test(unittest.TestCase):
    def create_invoice(self):
        random_date = datetime.datetime.now()
        random_value = 4398.20
        client_name = "Felipe"
        return Invoice(random_date, random_value, client_name)

    def test_invoice_object_is_created_correctly(self):
        curr_invoice = self.create_invoice()
        self.assertIsInstance(curr_invoice, Invoice)

    def test_invoice_add_payment_method(self):
        now = datetime.datetime.now()
        payment_value = 100
        payment_type = "BOLETO"

        new_payment = Payment(now, payment_type, payment_value)
        new_invoice = self.create_invoice()

        new_invoice.add_payment(new_payment)

        all_payments = len(new_invoice.payments)

        self.assertEqual(all_payments, 1)


if __name__ == '__main__':
    unittest.main()
