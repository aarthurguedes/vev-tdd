import datetime
import sys
sys.path.insert(1, "../app")
import unittest
from invoice import Invoice
from bank_slip_manager import Bank_Slip_Manager
from bank_slip import Bank_Slip
from payment import Payment

class Bank_Slip_Manager_Tests(unittest.TestCase):
    def test_bank_slip_manager_object_is_created_correctly(self):
        random_date = datetime.datetime.now()
        target_invoice = Invoice(random_date, 5345.12, "Felipe")
        

        bank_slip_manager = Bank_Slip_Manager(target_invoice)
        self.assertIsInstance(bank_slip_manager, Bank_Slip_Manager)

    def test_register_bank_slip_method(self):
        now = datetime.datetime.now()
        invoice = Invoice(now, 5345.12, "Felipe")

        bank_slip_manager = Bank_Slip_Manager(invoice)

        bank_slip = Bank_Slip("001", now, 5345.12)

        bank_slip_manager.register_bank_slip(bank_slip)

        self.assertEqual(len(invoice.payments), 1)

        invoice_payment = invoice.payments[0]

        self.assertEqual(invoice_payment.type, "BOLETO")
        self.assertEqual(invoice_payment.date, now)
        self.assertTrue(invoice.is_paid())


if __name__ == "__main__":
    unittest.main()
