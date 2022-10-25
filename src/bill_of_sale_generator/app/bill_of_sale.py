class BillOfSale:
  def __init__(self, client_name, value, tax_value):
    self.client_name = client_name
    self.value = value
    self.tax_value = tax_value

  def to_string(self):
    return f'Cliente: {self.client_name} | Valor: {self.value} | Valor do Imposto: {self.tax_value}'