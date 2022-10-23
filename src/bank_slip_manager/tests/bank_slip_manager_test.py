import datetime
import sys
sys.path.insert(1, "../app")
import unittest
from invoice import Invoice
from bank_slip_manager import Bank_Slip_Manager

class Bank_Slip_Manager_Tests(unittest.TestCase):
    def test_bank_slip_manager_object_is_created_correctly(self):
        random_date = datetime.datetime.now()
        target_invoice = Invoice(random_date, 5345.12, "Felipe")
        

        bank_slip_manager = Bank_Slip_Manager(target_invoice)
        self.assertIsInstance(bank_slip_manager, Bank_Slip_Manager)


if __name__ == "__main__":
    unittest.main()
