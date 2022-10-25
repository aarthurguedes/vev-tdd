from app.invoice import Invoice
from app.bill_of_sale import BillOfSale

class BillOfSaleGenerator():
  def __init__(self, smtp_service, sap_service, dao):
    self.smtp_service = smtp_service
    self.sap_service = sap_service
    self.dao = dao

  def generate(self, invoice):
    if not isinstance(invoice, Invoice):
      raise TypeError('invoice (param) must be Invoice')
    
    bill_of_sale = BillOfSale(invoice.client_name, invoice.value, self.calc_tax_value(invoice.service_type, invoice.value))

    self.smtp_service.send(bill_of_sale)
    self.sap_service.send(bill_of_sale)
    self.dao.save(bill_of_sale)

    return bill_of_sale
  
  def calc_tax_value(self, invoice_service_type, invoice_value):
    match invoice_service_type:
      case 'CONSULTANCY':
        tax_rate = 0.25
        return round(tax_rate * invoice_value, 2)
      case 'TRAINING':
        tax_rate = 0.15
        return round(tax_rate * invoice_value, 2)
      case _:
        tax_rate = 0.06
        return round(tax_rate * invoice_value, 2)

