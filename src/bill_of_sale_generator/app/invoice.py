class Invoice:
  def __init__(self, client_name, client_address, service_type, invoice_value):
    self.client_name = client_name
    self.client_address = client_address
    self.service_type = service_type
    self.value = invoice_value