import datetime
import sys
sys.path.insert(1, "../app")
import unittest
from payment import Payment

class Payment_Tests(unittest.TestCase):
    def test_payment_object_is_created_correctly(self):
        random_date = datetime.datetime.now()
        value = 5937
        payment_type = "BOLETO"


        curr_payment = Payment(random_date, value, payment_type)
        self.assertIsInstance(curr_payment, Payment)


if __name__ == "__main__":
    unittest.main()
