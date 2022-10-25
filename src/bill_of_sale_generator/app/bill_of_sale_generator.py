from app.invoice import Invoice

class BillOfSaleGenerator():
  def __init__(self):
    pass

  def generate(invoice):
    if not isinstance(invoice, Invoice):
      raise TypeError('invoice (param) must be Invoice')