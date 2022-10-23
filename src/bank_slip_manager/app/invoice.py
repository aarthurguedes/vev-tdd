class Invoice:
    def __init__(self, date, value, client_name):
        self.date = date
        self.value = value
        self.client_name = client_name
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)
