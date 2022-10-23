from payment import Payment

class Bank_Slip_Manager:
    def __init__(self, invoice):
        self.invoice = invoice
        self.total_paid = 0

    def register_bank_slip(self, bank_slip):
        new_payment = Payment(bank_slip.date, bank_slip.value, "BOLETO")

        self.invoice.add_payment(new_payment)

