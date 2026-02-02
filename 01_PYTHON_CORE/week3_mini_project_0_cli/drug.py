class Drug:
  def __init__(self, name, quantity, price):
    self.name = name
    self.quantity = quantity
    self.price = price
  def get_display_info(self):
    self.name
    self.quantity
    price = self.price
    final_info = f"Tên: {self.name} | Tồn kho: {self.quantity} | Giá: {price}"
    return final_info