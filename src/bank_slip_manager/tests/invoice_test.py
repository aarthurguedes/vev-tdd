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

    def test_invoice_is_paid_method(self):
        now = datetime.datetime.now()
        payment_type = "BOLETO"

        payment1 = Payment(now, 2000, payment_type)
        payment2 = Payment(now, 2398.20, payment_type)
        payment3 = Payment(now, 1234, payment_type)

        invoice1 = self.create_invoice()

        invoice1.add_payment(payment1)
        invoice1.add_payment(payment2)

        self.assertTrue(invoice1.is_paid())

        invoice2 = self.create_invoice()

        invoice2.add_payment(payment1)
        invoice2.add_payment(payment3)

        self.assertFalse(invoice2.is_paid())


if __name__ == '__main__':
    unittest.main()
