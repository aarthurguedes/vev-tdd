import sys
sys.path.insert(1, "../app")
import datetime
import unittest
from bank_slip import Bank_Slip

class Bank_Slip_Tests(unittest.TestCase):
    def test_bank_slip_object_is_created_correctly(self):
        code = "kabe3nY68Bf23"
        date = datetime.datetime.now()
        value = 200

        curr_bank_slip = Bank_Slip(code, date, value)
        self.assertIsInstance(curr_bank_slip, Bank_Slip)


if __name__ == '__main__':
    unittest.main()
